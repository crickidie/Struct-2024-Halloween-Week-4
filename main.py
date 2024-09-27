##############################################################
# created by: Deborah Sanchez
# email: debsanchez.business@outlook.com
# date: 9-27-2024
# desc: This sample Python project teaches you how to make 
# ascii art out of an image. This project is week 1 of a 5 week 
# project which can be downloaded at https://github.com/crickidie.
##############################################################

##############################################################
# This sample code uses the 'ascii-magic' object.
# To install this object, open terminal within
# your python session and run 'pip install ascii-magic'
##############################################################

import os
from ascii_magic import AsciiArt as am

def img_to_ascii(image_path) -> str:

    aa = am.from_image(image_path)

    return aa.to_ascii()

def main():
    os.system('cls')

    img = img_to_ascii('mask.png')
    print(img)

    input("Press enter to exit.")

if __name__ == "__main__":
    main()
