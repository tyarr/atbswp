import os, shutil

src= 'D:\\wnk2'

dst= 'C:\\Users\\tyya\\Pictures\\wnkpc'

def copy(src, dst):
    if os.path.isdir(dst):
        dst = os.path.join(dst, os.path.basename(src))
    shutil.copy(src, dst)