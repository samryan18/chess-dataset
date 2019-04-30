import os

with open('labels.txt') as f:
    labels = f.readlines()
labels = [x.strip().replace('\n','').replace(' ','').replace('\t','') 
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

path_to_photos = 'good_ass_labels'
directory_list = os.listdir(path_to_photos)
directory_list = [x for x in directory_list if ('jpg' in x or 'png' in x or 'JPG' in x or 'jpeg' in x or 'PNG' in x)]
print(str(len(directory_list)) + ' is the length of directory_list')
directory_list.sort()
print(directory_list)

if not (len(directory_list)==len(filename_labels)):
    print('get fucked wrong num files')

for i,fname in enumerate(directory_list):
    ext = fname.split('.')[-1]
    src = f'{path_to_photos}/{fname}'
    label = (filename_labels[i]).replace('/','-')
    dest = (f'{path_to_photos}/{label}.{ext}')
    print(dest)
    os.rename(src, dest)

print('successfully renamed files')