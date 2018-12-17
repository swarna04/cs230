import os
import shutil
#----------------------------------------
PATH = f'/home/nik/data/Animals_with_Attributes2/'
CLASSFILE = '/home/nik/data/Animals_with_Attributes2/trainclasses.txt'
SRC_FOLDER = r'train'
DEST_FOLDER = r'valid'
PERCENT = 0.1
#-----------------------------------------

assert (os.path.getsize(CLASSFILE) != 0), "OUTFILE should not be empty!"

#Open file
with open(CLASSFILE) as f:
    class_name_list = list(f)

class_name_list = [item.rstrip('\n') for item in class_name_list]

print("Classes in the source:", class_name_list)

for cls_name in class_name_list:
    srcdir = os.path.join(PATH, SRC_FOLDER, cls_name)
    destdir = os.path.join(PATH, DEST_FOLDER, cls_name)
    assert (os.path.isdir(srcdir)), "Source should be a directory"
    print(srcdir)

    if not os.path.exists(destdir):
        os.makedirs(destdir)

    for _, _, files in os.walk(srcdir):
        count = 1
        num_files = len(files)
        assert (num_files != 0), "Number of files should not be 0"
        COUNT = int(PERCENT*num_files) 
        for fname in files:
            shutil.move(os.path.join(srcdir, fname), os.path.join(destdir, fname))
            if (count == COUNT):
                break
            count = count + 1
        print("Copied ", count, " files to destination", destdir)

