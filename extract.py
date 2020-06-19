import r2pipe
from os import listdir
import os

def iterate(foldername):
    for f in listdir(foldername):
            print(f)
    
##any command that runs in the r2 shell can be pased to the cmd method
def extract_write(filename):
    r = r2pipe.open(filename)
    x = r.cmd("ie")
    last = x.rfind("entrypoints")
    print(x[last - 2])

    s = r.cmd("p8 64")
    
    ##creating new text file
    slash = filename.rfind("/")
    txt_file = filename[slash + 1:] + ".txt"
    directory = "/Users/gavinwong/Desktop/Repos/SJUMalwareEnsembleResearch/ByteSequences/ProcessedData/"
    # print(txt_file)
    
    f = open(os.path.join(directory, txt_file), "w+")
    f.write("DOS Header\n")
    f.write(s+"\n")
    f.write("PE Header\n")

    byteSpecfied = r.cmd("px 1 @ 0x3c")
    hexStart = byteSpecfied.rfind("0x")
    byteSpecfied = byteSpecfied[hexStart + 12:]
    pe = r.cmd("p8 264 @0x"+byteSpecfied)
    f.write(pe)


    f.close()
    return(str(directory + txt_file))


if __name__ == "__main__":
    s = (extract_write("/Users/gavinwong/Documents/dataset/v001-part5/VirusShare_fffb1996a5b7c4c716931af2842712e3"))
    s = (extract_write("/Users/gavinwong/Documents/dataset/v001-part5/VirusShare_fff8dcd61fb36a828dda906c9ecf2263"))
