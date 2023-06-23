import sys
from rules_game import rules,player

class Algorithm:
    def __init__(self,alpha=sys.maxsize,beta=-sys.maxsize):
        self.alpha = alpha
        self.beta = beta

    def minimax(self,button):
        blank_lst = self.rules.get_all_color_piece('white')
        for i in blank_lst:
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

            #turn the color to white
            next.bead_move = button
            next.color_change_bead = button.color

            next.color = 'white'
            next.change_button_color()

            if self.alpha >= self.beta:
                break

        if self.player.player1.turn == 1:
            return [row,column,self.alpha]
        else:
            return [row,column,self.beta]