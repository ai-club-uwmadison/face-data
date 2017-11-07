import os
from glob import glob
import shutil

NAMES = ['alliot','david','krittisak','nat']

def move():
    if not os.path.exists('final_data/'):
        os.makedirs('final_data/')

    for name in NAMES:
        frames_dir = name + '/frames/'
        for folder in os.listdir(frames_dir):
            print(folder)
            if not os.path.exists('final_data/' + name):
                os.makedirs('final_data/' + name)
            for filename in os.listdir(frames_dir + folder):
                old_name = frames_dir + folder + '/' + filename
                new_name = 'final_data/' + name + '/' + folder + "__" + filename
                print("{} copied to {}.".format(old_name, new_name))
                shutil.copy2(old_name, new_name)

if __name__ == '__main__':
    move()