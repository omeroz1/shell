import codecs
import sys

if len(sys.argv) > 1:
    if sys.argv[1].__contains__("."):
        bin_data = open(sys.argv[1], 'rb').read()
        hex_data = codecs.encode(bin_data, "hex_codec")
        print(hex_data)
        # if the input contains a file, it will print the hex code of the file given.
    else:
        print(hex(int(sys.argv[1])))
        # if the input contains a binary number, it will change it to hex.
else:
    bin_data = open('GOPR6801.JPG', 'rb').read()
    hex_data = codecs.encode(bin_data, "hex_codec")
    print(hex_data)
    # if the input is only 'Hexdump.py', it will print the hex code of my photo.
