from movements import movements
from random import choice


class algorithms(movements):
    def __init__(self, main_board):
        super().__init__(main_board)

    def minimax(self):
        pass

    def random(self, color, lst=None):
        if color:
            lst_color_piece = self.get_all_color_piece(color)
            return choice(lst_color_piece)
        else:
            return choice(lst)