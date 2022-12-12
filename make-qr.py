import qrcode
import PIL
import sys

if __name__ == '__main__':
    image = qrcode.make(sys.argv[1])
    image.save('a.png')
