from movements import movements
from random import choice


class algorithms(movements):
    def __init__(self, main_board):
        super().__init__(main_board)

    def max_alpha_beta(self, alpha, beta):
        max_v = float('-inf')
        px = None
        py = None

        player_win, score = self.is_end_out_bead()
        if player_win == self.player1:
            return score * 10, 0, 0

        elif player_win == self.player2:
            return score * -10, 0, 0

        elif player_win is None:
            return 0, 0, 0

        lst_white_piece = self.get_all_color_piece('white')[8: 10]
        for i, pos in enumerate(lst_white_piece):
            r, c = pos[0], pos[1]
            # self.main_board[r][c].color = self.player1.color
            button = self.main_board[r][c]

            self.player1.turn = 1
            self.player2.turn = 0

            self.insert(button, 0)
            # self.switch_turn()

            m, min_i, min_j = self.min_alpha_beta(alpha, beta)
            if m > max_v:
                max_v = m
                px = min_i
                py = min_j

            # self.main_board[r][c].color = 'white'
            # self.switch_turn()
            # self.player1.turn = 1
            # self.player2.turn = 0
            # self.undo_insert(button)
            self.player1.number_bead += 1
            button.color = 'white'
            self.player1.alive_bead -= 1

            if max_v >= beta:
                return max_v, px, py

            if max_v > alpha:
                alpha = max_v

        return max_v, px, py

    def min_alpha_beta(self, alpha, beta):
        min_v = float('inf')
        qx = None
        qy = None

        player_win, score = self.is_end_out_bead()
        if player_win == self.player1:
            return score * 10, 0, 0

        elif player_win == self.player2:
            return score * -10, 0, 0

        elif player_win is None:
            return 0, 0, 0

        lst_white_piece = self.get_all_color_piece('white')[0: 2]
        for i, pos in enumerate(lst_white_piece):
            r, c = pos[0], pos[1]
            # self.main_board[r][c].color = self.player2.color
            button = self.main_board[r][c]
            self.player1.turn = 0
            self.player2.turn = 1

            self.insert(button, 0)
            # self.switch_turn()

            m, max_i, max_j = self.max_alpha_beta(alpha, beta)
            if m < min_v:
                min_v = m
                qx = max_i
                qy = max_j
            # self.main_board[r][c].color = 'white'
            # self.switch_turn()
            # self.player2.turn = 1
            # self.player1.turn = 0
            # self.undo_insert(button)
            self.player2.number_bead += 1
            button.color = 'white'
            self.player2.alive_bead -= 1

            if min_v <= alpha:
                return min_v, qx, qy

            if min_v < beta:
                beta = min_v

        return min_v, qx, qy

    def random(self, color, lst=None):
        if color:
            lst_color_piece = self.get_all_color_piece(color)
            return choice(lst_color_piece)
        else:
            return choice(lst)