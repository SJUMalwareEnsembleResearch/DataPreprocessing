
import r2pipe
from os import listdir
import os

def iterate(foldername):
    for f in listdir(foldername):
            print(f)
    
##any command that runs in the r2 shell can be pased to the cmd method
def extract_write(filename):
    r = r2pipe.open(filename)
    s = r.cmd("pD 64")
    
    ##creating new text file
    slash = filename.rfind("/")
    txt_file = filename[slash + 1:] + ".txt"
    directory = "/Users/gavinwong/Desktop/Repos/SJUMalwareEnsembleResearch/ByteSequences/"
    print(txt_file)
    
    f = open(os.path.join(directory, txt_file), "w+")
    f.write("DOS Header")
    f.write(s)
    f.close()
    return(str(directory + txt_file))


if __name__ == "__main__":
    s = (extract_write("/Users/gavinwong/Desktop/v001/VirusShare_0a2e87dcc632209c21f66d0128042302"))
    print(s)
    
    
    
    