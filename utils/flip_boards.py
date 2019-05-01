import cv2
import os

'''

Not used

'''

path_to_photos = 'labeled_preprocessedc'
dest_path = 'flipped_photos/'
directory_list = os.listdir(path_to_photos)
directory_list = [x for x in directory_list if ('jpg' in x 
                                                      or 'png' in x 
                                                      or 'JPG' in x 
                                                      or 'jpeg' in x 
                                                      or 'PNG' in x)]
#print(str(len(directory_list)) + ' is the length of directory_list')

for img in directory_list:
    image = cv2.imread(img)
    f_image = cv2.flip(image, -1)
    cv2.imshow(' ',image)
    f_label = img.split('.')[0][::-1]
    cv2.imwrite(dest_path + f_label + '.png', f_image)