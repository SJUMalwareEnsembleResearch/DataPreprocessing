import os
import subprocess

# os.system("hexdump -n64 VirusShare_fff8dcd61fb36a828dda906c9ecf2263")
# print()
DOS = str(subprocess.check_output('''hexdump -n64 -e '16/1 "%02x " "\n"' /Users/gavinwong/Documents/dataset/v001-part5/VirusShare_fffb1996a5b7c4c716931af2842712e3''', shell=True))
byte60 = str(subprocess.check_output("hexdump -n1 -s60 /Users/gavinwong/Documents/dataset/v001-part5/VirusShare_fffb1996a5b7c4c716931af2842712e3", shell=True))
x = byte60.find(" ")
byte60 = byte60[x + 1: x + 3]


peStart = int(byte60, 16)
PE = str(subprocess.check_output('''hexdump -n264 -s''' + str(peStart) +''' -e '16/1 "%02x " "\n"' /Users/gavinwong/Documents/dataset/v001-part5/VirusShare_fffb1996a5b7c4c716931af2842712e3''', shell=True))
DOS = DOS.replace(" ", "")
DOS = DOS.replace("\\n", "")
DOS = DOS.replace("*", "")
DOS = DOS.replace("*", "")
DOS = DOS.replace("'", "")
DOS = DOS[1:]

PE = PE.replace(" ", "")
PE = PE.replace("\\n", "")
PE = PE.replace("*", "")
PE = PE.replace("'", "")
PE = PE[1:]



filename = "VVirusShare_fffb1996a5b7c4c716931af2842712e3"
slash = filename.rfind("/")
txt_file = filename[slash + 1:] + ".txt"
directory = "/Users/gavinwong/Desktop/Repos/SJUMalwareEnsembleResearch/ByteSequences/ProcessedData/"

f = open(os.path.join(directory, txt_file), "w+")
f.write("DOS Header\n")
f.write(DOS+"\n")
f.write("PE Header\n")
f.write(PE)


print(DOS)
print("------------")
print(PE)
# peStart = os.system("hexdump -n1 -s60 VirusShare_fff8dcd61fb36a828dda906c9ecf2263")
# print("--------")
# print(peStart)

# os.system("cd..")
# os.system("ls")
# os.system("cd Documents/")
