from urllib.parse import quote
import base64
import sys

if __name__ == '__main__':
    png_file = sys.argv[1]
    with open(png_file, 'rb') as fp:
        image = fp.read()
        print(quote(base64.b64encode(image).decode()))

