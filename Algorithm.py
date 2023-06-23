import sys
from rules_game import rules,player

class Algorithm:
    def __init__(self,alpha=sys.maxsize,beta=-sys.maxsize):
        self.alpha = alpha
        self.beta = beta

    def minimax(self,button):
        blank_lst = self.rules.get_all_color_piece('white')
        # لیست خونه های خالی رو برای حرکت بگیریم
        for i in blank_lst: # برای تموم خونه های خالی مونده حرکت هارو بررسی کنه تا بهترین انتخاب شه
            #play next move
            self.rules.allow_to_move(i[0],i[1])
            if self.player.player1.turn == 1:
                self.player.player1.turn = 0
                self.player.player2.turn = 1

            elif self.player.player2.turn == 1:
                self.player.player2.turn = 0
                self.player.player1.turn = 1

            next = self.minimax(self.alpha,self.beta)

            if self.player.player1.turn == 1:
                if next[2] > self.alpha:
                    self.alpha = next[2]
                    row = i[0]
                    column = i[1]

            else:
                if next[2] < self.beta:
                    self.betaeta = next[2]
                    row = i[0]
                    column = i[1]


            # برای برگردوندن حرکت به قبل انجام میشه که اینا کامنته همش اصلا روی گرافیک نمیاد
            #turn the color to white
            # next.bead_move = button
            # next.color_change_bead = button.color
            #
            # next.color = 'white'
            # next.change_button_color()

            if self.alpha >= self.beta:
                break

        if self.player.player1.turn == 1:
            return [row,column,self.alpha]
        else:
            return [row,column,self.beta]

        # بالا که نوشته بودم next[2] منظورم این آلفا و بتا بود که ریترن میشه. برای عایدی بهترین حرکت