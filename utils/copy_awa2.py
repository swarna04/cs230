import os
import shutil
#----------------------------------------
PATH_SRC = f'/home/nik/data/Animals_with_Attributes2/JPEGImages'
PATH_DEST = f'/home/nik/data/Animals_with_Attributes2/train'
CLASSFILE = '/home/nik/data/Animals_with_Attributes2/trainclasses.txt'
COUNT = 2000
#-----------------------------------------
assert (os.path.getsize(CLASSFILE) != 0), "OUTFILE should not be empty!"

#Open file
with open(CLASSFILE) as f:
    class_name_list = list(f)

class_name_list = [item.rstrip('\n') for item in class_name_list]

print("Classes in the source:", class_name_list)

for cls_name in class_name_list:
    srcdir = os.path.join(PATH_SRC, cls_name)
    destdir = os.path.join(PATH_DEST, cls_name)
    assert (os.path.isdir(srcdir)), "Source should be a directory"
    print(srcdir)
    
    if not os.path.exists(destdir):
        os.makedirs(destdir)

    for _, _, files in os.walk(srcdir):
        count = 1
        for fname in files:
            shutil.move(os.path.join(srcdir, fname), os.path.join(destdir, fname))
            if (count == COUNT):
                break
            count = count + 1
        print("Copied ", count, " files to destination", destdir)
