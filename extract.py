import r2pipe
from os import listdir
import os

def iterate(foldername):
    for f in listdir(foldername):
            print(f)
    
##any command that runs in the r2 shell can be pased to the cmd method
def extract_write(filename):
    r = r2pipe.open(filename)
    s = r.cmd("p8 64")
    
    ##creating new text file
    slash = filename.rfind("/")
    txt_file = filename[slash + 1:] + ".txt"
    directory = "/Users/gavinwong/Desktop/Repos/SJUMalwareEnsembleResearch/ByteSequences/"
    print(txt_file)
    
    f = open(os.path.join(directory, txt_file), "w+")
    f.write("DOS Header\n")
    f.write(s+"\n")
    f.write("PE Header\n")

    byteSpecfied = r.cmd("px 1 @ 0x3c")
    hexStart = byteSpecfied.rfind("0x")
    print(byteSpecfied)
    byteSpecfied = byteSpecfied[hexStart + 12:]
    pe = r.cmd("p8 264 @0x"+byteSpecfied)
    f.write(pe)
    print(byteSpecfied)


    f.close()
    return(str(directory + txt_file))


if __name__ == "__main__":
    s = (extract_write("/Users/gavinwong/Desktop/v001/VirusShare_fffb1996a5b7c4c716931af2842712e3"))