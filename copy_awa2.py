import os
import shutil
#----------------------------------------
PATH = f'~/data/Animals_with_Attributes2/JPEGImages'
PATH_DEST = f'~/data/Animals_with_Attributes2_small/train'
OUTFILE = 'awa2_classes_small.txt'
#SRC_FOLDER = r'train_split'
#DEST_FOLDER = r'valid_split'
COUNT = 300
#-----------------------------------------
print (os.path.getsize(OUTFILE))

#Open file
outfile = open(OUTFILE)
outfile_text = outfile.read()
print (outfile_text)

dir_list = outfile_text.split()
for dir in dir_list:
    srcfile = os.path.join(PATH,dir)
    destdir  = os.path.join(PATH_DEST,dir)
    print (os.path.isdir(srcfile))
    for empty1, empty2, filelist in os.walk(srcfile):
        count = 0
        for fname in filelist:
            #print(destdir)
            if not os.path.exists(destdir):
               os.mkdir(destdir)
            shutil.copy(os.path.join(srcfile,fname), os.path.join(destdir,fname))
            count=count+1
            print(fname + ' is being copied, count is ' + str(count))
            if (count ==COUNT ):
               break
