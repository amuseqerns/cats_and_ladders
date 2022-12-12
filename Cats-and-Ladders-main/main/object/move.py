import pygame
from object.dice import Dice
from object.ladder import LadderSnake
dice = Dice()
laddersnake = LadderSnake()

def move(numplay,randomnum,cat,amount,screen):
        # if dice.isrolling:
        #     randomnum = dice.randonnum + 1
        # else:
        #     if randomnum > 0:
        #         print("more")
        #         cat[numplay].checkmove = True
        #         dice.randonnum = 0
        #         if cat[numplay].column > 9:
        #             if cat[numplay].jumpCount >= -12:
        #                 cat[numplay].y -= (cat[numplay].jumpCount * abs(cat[numplay].jumpCount)) * 0.1
        #                 cat[numplay].y -= 2.8
        #                 cat[numplay].jumpCount -= 1
        #             else:
        #                 cat[numplay].column = 1
        #                 cat[numplay].jumpCount = 12
        #                 cat[numplay].row += 1
        #                 randomnum -= 1
        #         else:
        #             if cat[numplay].jumpCount >= -12:
        #                 cat[numplay].y -= (cat[numplay].jumpCount * abs(cat[numplay].jumpCount)) * 0.1
        #                 cat[numplay].jumpCount -= 1
        #                 if cat[numplay].row % 2 == 0:
        #                     cat[numplay].x -= 2.8
        #                 else:
        #                     cat[numplay].x += 2.8
        #             else:
        #                 cat[numplay].jumpCount = 12
        #                 randomnum -= 1
        #                 cat[numplay].column += 1
        #         if randomnum == 0:
        #             cat[numplay].checkmove = False
        #             if numplay < amount - 1:
        #                 print("plus")
        #                 numplay += 1
        #             else:
        #                 numplay = 0
        #                 print("zero")
        #     else:
        #         laddersnake.move(cat[numplay].row,cat[numplay].column)
        #         cat[numplay].row = laddersnake.row_lad
        #         cat[numplay].column = laddersnake.column_lad
        #         cat[numplay].y = 623 - ((cat[numplay].row - 1) * 70)
        #         if cat[numplay].row % 2 == 0:
        #             cat[numplay].x = 700 - ((cat[numplay].column) * 70)
        #         else:
        #             cat[numplay].x = 0 + ((cat[numplay].column - 1) * 70)
        for i in range(amount):
            cat[i].x = i * 50
            cat[i].draw(screen)
        if not cat[numplay].checkmove:
            dice.dicing(screen)