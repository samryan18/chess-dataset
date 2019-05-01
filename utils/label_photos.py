import os
import re


LABELS_TEXTFILE_PATH = 'labels2.txt'
PATH_TO_PHOTOS = 'photos_unlabeled'


with open(LABELS_TEXTFILE_PATH) as f:
    labels = f.readlines()

# strip bad chars from labels
rep = {'\n':'', ' ':'','\t':''}
rep = dict((re.escape(k), v) for k, v in rep.items())
pattern = re.compile("|".join(rep.keys()))
labels = [pattern.sub(lambda m: rep[re.escape(m.group(0))], x.strip()) 
                    for x in labels]


print(f'Found {len(labels)} labels.')

filename_labels = []
label_counts = {}
for label in labels:
    new_label = label
    if label in label_counts.keys():
        label_counts[label] = label_counts[label]+1
        new_label = f'{new_label}_{label_counts[label]}'
    else:
        label_counts[label] = 1

    filename_labels.append(new_label)


print(f'Made the {len(filename_labels)} labels unique.')

directory_list = os.listdir(PATH_TO_PHOTOS)
directory_list = [x for x in directory_list if ('jpg' in x 
                                                or 'png' in x 
                                                or 'JPG' in x 
                                                or 'jpeg' in x 
                                                or 'PNG' in x)]
print(str(len(directory_list)) + ' is the length of directory_list')
directory_list.sort()
print(directory_list)

if not (len(directory_list)==len(filename_labels)):
    raise Exception(f'ya messed up wrong num files/labels '
                    f'{len(directory_list)} files'
                    f'len(filename_labels) labels')

for i,fname in enumerate(directory_list):
    ext = fname.split('.')[-1]
    src = f'{PATH_TO_PHOTOS}/{fname}'
    label = (filename_labels[i]).replace('/','-')
    dest = (f'{PATH_TO_PHOTOS}/{label}.{ext}')
    print(dest)
    os.rename(src, dest)

print(f'successfully renamed {len(directory_list)} files')