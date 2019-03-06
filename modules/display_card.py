from PIL import Image
import io
import pathlib
import json
import os
import sys

sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'modules\cards_img'))
print(sys.path)

# cardSize = ( 50 , 67 )
# h_gap = 40
# v_gap1 = 24
# v_gap2 = 25
#
# row = 1
# column = 2
#
# img = Image.open("cards_img.plateau.png")
# card = Image.open("1.jpg")
#
# position1 = (column*(h_gap+cardSize[0])+h_gap , v_gap1+row*(v_gap2+cardSize[1]) )
# position2 = (position1[0]+cardSize[0], position1[1]+cardSize[1])
# print (position1)
# print (position2)
#
# img.paste(card, position1+position2)
#
# img.show()
# img.close()
# print("Everything is okay")
# os.system("pause")
#
# if __name__ == __main__:
#     pass
