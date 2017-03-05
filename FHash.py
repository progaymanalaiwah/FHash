#!/usr/bin/env python3

#Import Lib Python
import hashlib
import os
from optparse import OptionParser

#Start Function

def logo():#Function Logo Tool V1
    print("""
       /$$$$$$$$ /$$   /$$                     /$$       
      | $$_____/| $$  | $$                    | $$       
      | $$      | $$  | $$  /$$$$$$   /$$$$$$$| $$$$$$$  
      | $$$$$   | $$$$$$$$ |____  $$ /$$_____/| $$__  $$    
      | $$__/   | $$__  $$  /$$$$$$$|  $$$$$$ | $$  \ $$ 
      | $$      | $$  | $$ /$$__  $$ \____  $$| $$  | $$ 
      | $$      | $$  | $$|  $$$$$$$ /$$$$$$$/| $$  | $$ 
      |__/      |__/  |__/ \_______/|_______/ |__/  |__/ 
                                                         
      Programmed Name  : Ayman Mahmoud Alaiwah
      facebook         : http://www.fb.com/ProgAymanAlaiwah
      Tool Name        : FHash
      Verssion         :1.0.0
      ###################################################
      """)
def hashfile(fdir,typeHash,save):#Function Hash File
    if typeHash == None:
        typeHash = 'md5'
    movefile = fdir.split(',')
    print("----------------------[Information File]----------------------")
    for i in range(len(movefile)):
        pathFile = movefile[i]
        name_file = pathFile.split('/')[-1]
        sizeFile = os.stat(pathFile)
        sizeFile = sizeFile.st_size / 1000 / 1000
        HASH = hashlib.new(typeHash)
        with open(pathFile,'rb') as openfile:
            readSize = 0
            while readSize != b'':
                readSize = openfile.read(1024)
                HASH.update(readSize)
        HASH = HASH.hexdigest()
        print("""
        NumberFile: {4}
        NameFile:   {0}
        SizeFile:   {1} MB
        TypeHash:   {3}
        HashFile:   {2}
        -------------------------------
          """.format(name_file,int(sizeFile),HASH,typeHash,i+1))
        if save != None:
            save = save.split('/')[-1]
            with open(save,'a') as saveFile:
                saveFile.write("""
    NumberFile: {4}
    NameFile:   {0}
    SizeFile:   {1} MB
    TypeHash:   {3}
    HashFile:   {2}
    -------------------------------
                               """.format(name_file,int(sizeFile),HASH,typeHash,i+1))

logo()
parser = OptionParser("""
                      
    pyhton3 FHash.py -f File Dirctory Or Add More Then File Options
    pyhton3 FHash.py -f File Dirctory Or Add More Then File  -t Type Hash  Default Hash Md5 Options
    pyhton3 FHash.py -f File Dirctory Or Add More Then File  -s Name File Or Dirctory Options
    
                      """)
#  Option 
parser.add_option('-f','--file',dest='fdir',help='Dirctory File')
parser.add_option('-t','--hash',dest='hash',help='Add Type Hash default MD5')
parser.add_option('-s','--save',dest='save',help='Save Hash File In FHash.txt')
(options,args) = parser.parse_args()

# Value
fdir = options.fdir
typeHash = options.hash
save = options.save


#Function
if fdir != None:
    hashfile(fdir,typeHash,save)
else:
    exit()
