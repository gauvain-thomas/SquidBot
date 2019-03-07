from PIL import Image
import io
import pathlib
import json
import os
# import sys

# sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'modules/cards_img'))
# print(sys.path)

#return the position in the image of the card, given a row and a column


def get_folder():

    return os.path.dirname(__file__)

def get_position(row,column):

    card_width = 50
    card_height = 67
    horizontal_gap = 40
    vertical_gap1 = 24
    vertical_gap2 = 25

    position1 = (column*(horizontal_gap+card_width) + horizontal_gap, row*(vertical_gap2+card_height) + vertical_gap1)
    position2 = (position1[0] + card_width, position1[1] + card_height)

    return position1 + position2


def load_card(cardTuple):

    cardPath = get_folder()+ "\\" + cardTuple[1] + ".jpg"
    return Image.open(cardPath)

def load_stack():

    stackPath = get_folder() + "\\stack.png"
    return  Image.open(stackPath)



def paste_card(cardTuple,position,stack):

    card_image = load_card(cardTuple)
    stack.paste(card_image,position)
    return stack

stack = load_stack()
paste_card((1,"1_Clubs"),get_position(1,2),stack).show()


# def createImage(up,mid,down):
#
#     tour_max = len(mid)
#
#     if tour_max < 4:
#         count = tour_max
#     else:
#         count = 4
#
#         for x in range (-4,0):
#             tuple = mid[x]
#             card = tuple[1]
#             card_image = Image.open(dirname+"\\"+card+".jpg")
#             row = 1
#             column = tuple[0]
#             img.paste(card_image,
#             card_image.close()
