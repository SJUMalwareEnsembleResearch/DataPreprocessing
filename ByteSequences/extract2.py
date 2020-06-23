
import r2pipe
from os import listdir
import os
import pathlib

def iterate(filename):
    for f in filename:
            iterateDataset(f)


def iterateDataset(filename):
    for i in range(1,6):
        file = "/Users/gavinwong/Documents/dataset/v001-part"+str(i)+"/VirusShare_0a2cca2202804bf99ec879adb7b7f9f0"
        success = extract_write(filename)
        if (success):
            break
    


    
##any command that runs in the r2 shell can be pased to the cmd method
def extract_write(filename):
    try:
        r = r2pipe.open(filename)
        x = r2pipe.cmd("ie")
        print(x)
        s = r.cmd("p8 64")
    
        ##creating new text file
        slash = filename.rfind("/")
        txt_file = filename[slash + 1:] + ".txt"
        directory = "/Users/gavinwong/Documents/processedData/adload_files"
        print(txt_file)
        
        f = open(os.path.join(directory, txt_file), "w+")
        f.write("MZ-DOS Header\n")
        f.write(s+"\n")
        f.write("PE Header\n")

        byteSpecfied = r.cmd("px 1 @ 0x3c")
        hexStart = byteSpecfied.rfind("0x")
        print(byteSpecfied)
        byteSpecfied = byteSpecfied[hexStart + 12:]
        pe = r.cmd("p8 264 @0x"+byteSpecfied)
        f.write(pe)

        f.close()

        return true
    except:
        print("return")
        return false
    
   


if __name__ == "__main__":
    s = (extract_write("/Users/gavinwong/Documents/dataset/v001-part2/VirusShare_0a0a6e36b3fd45302c245381364dc8e4"))
    # iterateDataset(5)
    #iterate("adload_files.txt")
    
    
    
    