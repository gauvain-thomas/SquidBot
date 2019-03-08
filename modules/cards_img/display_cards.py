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


def load_card(cardTuple):
    cardPath = get_folder()+ "\\" + cardTuple[1] + ".jpg"
    return Image.open(cardPath)

def load_stack():
    stack_path = get_folder() + "\\stack.png"
    return  Image.open(stack_path)

def get_position(row, column, card_index = None, cards_number = None):

    card_width = 50
    card_height = 67
    horizontal_gap = 40
    vertical_gap1 = 24
    vertical_gap2 = 25
    cards_disparity = 30

    if card_index == None or cards_number == None:


        position1 = (column*(horizontal_gap+card_width) + horizontal_gap, row*(vertical_gap2+card_height) + vertical_gap1)
        position2 = (position1[0] + card_width, position1[1] + card_height)

    else:

        position1 = (int(column*(horizontal_gap+card_width)  + horizontal_gap + ((cards_number - card_index - 1)* 30 / (cards_number - 1))), row*(vertical_gap2+card_height) + vertical_gap1)
        position2 = (position1[0] + card_width, position1[1] + card_height)

    print(position1+position2)
    return position1 + position2


def get_current_round(up_last_card, middle_last_card, down_last_card):

    if up_last_card[0] > middle_last_card[0] and up_last_card[0] > down_last_card[0]:

        return up_last_card[0]

    elif middle_last_card[0] > down_last_card[0]:

        return middle_last_card[0]

    else:

        return down_last_card[0]


def paste_card(cardTuple, position, stack):
    card_image = load_card(cardTuple)
    stack.paste(card_image,position)
    return stack

def create_image(up_row, middle_row, down_row):

    stack = load_stack()

    current_round = get_current_round(up_row[-1], middle_row[-1], down_row[-1])

    print('appelle de paste_middle_row:\n')
    stack = paste_middle_row(middle_row, current_round, stack)
    print('appelle de paste_down_row:\n')
    stack = paste_border_row(down_row, 2, current_round, stack)
    stack = paste_border_row(up_row, 0, current_round, stack)
    stack.show()
    print(current_round)
    print(middle_row)

def paste_middle_row(middle_row, current_round, stack):

    row = 1

    for index in range(-1, -5, -1):

        card_tuple = middle_row[index]
        column = 3 - (current_round - card_tuple[0])

        if column <= 3 and column >= 0:

            stack = paste_card(card_tuple, get_position(row, column), stack)

    return stack

def paste_border_row(row_list, row_number, current_round, stack):

    stop_round = current_round - 4
    index = -1

    while index >= -len(row_list):


        previous_index = index
        card_tuple = row_list[index]
        card_round = card_tuple[0]

        if card_tuple[0] < stop_round:

            break

        while card_round == card_tuple[0]:

            index = index - 1
            if index < -len(row_list):

                break

            card_tuple = row_list[index]


        print(index)
        print(previous_index)
        column = 3 - (current_round - card_round)
        for x in range(previous_index, index, -1):


            card_tuple = row_list[x]
            stack = paste_card(card_tuple, get_position(row_number, column), stack)

    return stack


if __name__ == '__main__':
    up_row = [(1, '3_Spades'),  (1, '5_Hearts'),  (3, '1_Spades'), (5, 'K_Diamonds')]
    middle_row = [(1, '3_Spades'),  (2, '5_Hearts'),  (3, '1_Spades'), (4, 'K_Diamonds')]
    down_row = [(3, '3_Spades'),  (4, '4_Hearts'),  (5, '8_Spades'), (5, 'K_Diamonds')]

    create_image(up_row, middle_row, down_row)
