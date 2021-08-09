from PIL import Image
import os


def logo_adder(logo_name, logo_size=(100, 100)):
    """
    This function takes a file name -> str , and a logo_size -> tuple (100 , 100) by default,
    pastes the logo on the right bottom corner of all the images in the folder and saves them in withLogo directory
    """

    os.mkdir('withLogo')
    logo = Image.open(logo_name)
    logo = logo.resize(logo_size)

    logoWidth, logoHeight = logo.size

    for filename in os.listdir('.'):
        notImage = not (filename.endswith('.png') or filename.endswith(
            'jpg') or filename.endswith('.PNG') or filename.endswith('.JPG'))
        if notImage or filename == logo_name:
            continue

        image = Image.open(filename)
        imageWidth, imageHeight = image.size

        # pasting in the right bottom corner
        image.paste(logo, (imageWidth - logoWidth,
                    imageHeight - logoHeight), logo)
        image.save(os.path.join('withLogo', filename))


def main():
    logo_adder('logo.png')


main()
