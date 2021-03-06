import os
from shutil import copyfile

# As per README:
# All files of iteration 0-4 move to testing-spectrograms
# All files of iteration 5-49 move to training-spectrograms


def separate(source):
    for filename in os.listdir(source):
        first_split = filename.rsplit("_", 1)[1]
        second_split = first_split.rsplit(".", 1)[0]
        if int(second_split) <= 4:
            copyfile(source + "/" + filename, "exp_data/test/recordings" + "/" + filename)
        else:
            copyfile(source + "/" + filename, "exp_data/train/recordings" + "/" + filename)


separate('recordings')
