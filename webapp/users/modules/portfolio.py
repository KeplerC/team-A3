import os
from flask import url_for

def get_user_description(user_id):
    print("from user.modules.portfolio: get_user_description is not implemented yet. please implement it")
    return "Hi, I am user No.{}. balabalabala".format(user_id)

default_photo = "default.jpg"

def get_user_photo(user_id, user_imgs_path):
    '''
    for debugging, consider using this library:
    "http://i.pravatar.cc/500?img=1"
    '''
    print("from user.modules.portfolio: get_user_photo is not implemented yet. please implement it")
    all_imgs_names = os.listdir(user_imgs_path)
    # print("user photos", all_imgs_names)
    # file_name = user_photos.get(user_id, default_photo)
    file_name = default_photo
    for img_name in all_imgs_names:
        img_id = img_name.split('.')[0]
        if len(img_id) and str(img_id) == str(user_id):
            file_name = img_name

    return file_name

def remove_previous_image(user_id, user_imgs_path):
    print("from user.modules.portfolio: remove_previous_image is not completely implemented yet. please implement it")
    all_imgs_names = os.listdir(user_imgs_path)
    for img_name in all_imgs_names:
        img_id = img_name.split('.')[0]
        if len(img_id) and str(img_id) == str(user_id):
            os.remove(os.path.join(user_imgs_path, img_name))
            '''
            in fact it'll be very expensive to loop through everyone when user size is large
            so we should keep a user portfolio indicating clearly which photo to use
            '''

