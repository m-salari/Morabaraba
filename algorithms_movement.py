from copy import deepcopy

from movements import movements
from random import choice


class algorithms(movements):
    def __init__(self, main_board):
        super().__init__(main_board)
        self.best_movement_insert = None
        self.best_movement_start_choice = None

    def random(self, color, lst=None):
        if color:
            lst_color_piece = self.get_all_color_piece(color)
            return choice(lst_color_piece)
        else:
            return choice(lst)

    def is_end_out_bead(self):
        if self.player1.alive_bead - self.player2.alive_bead >= 2:
            return self.player1, (self.player1.alive_bead - self.player1.alive_bead) * 10

        elif self.player2.alive_bead - self.player1.alive_bead >= 1:
            return self.player2, (self.player2.alive_bead - self.player1.alive_bead) * -10

        else:
            return False, 0

    def get_neighbors_white_piece_minimax(self, row, col):
        lst_white_piece = []
        button = self.main_board[row][col]
        for neighbor in button.neighbors:
            child_button = self.main_board[neighbor[0]][neighbor[1]]

            if child_button.color == 'white':
                lst_white_piece.append((child_button.row, child_button.col))

        return lst_white_piece

    def minimax(self, depth: int, maximizingPlayer: bool, alpha=float('-inf'), beta=float('inf')):

        player_win, score = self.is_end_out_bead()
        if depth == 0 or player_win:
            return score, None
        # if depth == 0:
        #     return -10, None

        if maximizingPlayer:
            value = float('-inf')
            lst_red = self.get_all_color_piece('red')
            for piece_red in lst_red:
                possible_moves = self.get_neighbors_white_piece_minimax(piece_red[0], piece_red[1])
                for move in possible_moves:
                    button = self.main_board[move[0]][move[1]]

                    self.player1.turn = 1
                    self.player2.turn = 0

                    self.insert(button, 0)

                    tmp = self.minimax(depth - 1, False, alpha, beta)[0]
                    if tmp > value:
                        value = tmp
                        self.best_movement_insert = move

                    if value >= beta:
                        break
                    alpha = max(alpha, value)

            return value, self.best_movement_insert

        else:
            value = float('inf')
            lst_blue = self.get_all_color_piece('blue')
            for piece_blue in lst_blue:
                possible_moves = self.get_neighbors_white_piece_minimax(piece_blue[0], piece_blue[1])
                for move in possible_moves:
                    button = self.main_board[move[0]][move[1]]

                    self.player2.turn = 1
                    self.player1.turn = 0

                    self.insert(button, 0)

                    tmp = self.minimax(depth - 1, True, alpha, beta)[0]
                    if tmp < value:
                        value = tmp
                        self.best_movement_insert = move

                    if value <= alpha:
                        break
                    beta = min(beta, value)

            return value, self.best_movement_insert

    def eval_minimax_move(self):
        if self.player_win == self.player1:
            return True, self.total_score_moving

        elif self.player_win == self.player2:
            return True, self.total_score_moving * -1

        return False, 0

    def eval_minimax_end(self, pos_button):
        button = self.main_board[pos_button[0]][pos_button[1]]
        player = self.get_turn_player()
        enemy = self.get_enemy_player()

        for neighbor in button.neighbors:

            neighbor = self.main_board[neighbor[0]][neighbor[1]]
            if neighbor.color == 'white':

                r, c = neighbor.row, neighbor.col

                self.main_board[r][c].color = player.color
                self.check_score()
                if self.flag_remove:
                    self.flag_remove = False
                    return player, 100, (r, c)

                self.main_board[r][c].color = enemy.color
                if self.flag_remove:
                    self.flag_remove = False
                    return enemy, 50, (r, c)

                self.main_board[r][c].color = 'white'

        return False, 0, (None, None)

                # else:
                #     self.main_board[r][c].color = 'white'

    def minimax_move(self, depth: int, maximizingPlayer: bool, alpha=float('-inf'), beta=float('inf')):

        # todo: change evaluation
        player_win, score = self.eval_minimax_move()

        if depth == 0 or player_win:
            s = deepcopy(self.total_score_moving)
            self.player_win = None
            self.total_score_moving = 0
            return s, None

        # if depth == 0:
        #     return -10, None

        if maximizingPlayer:
            value = float('-inf')
            lst_red = self.get_all_color_piece('red')
            # for move in lst_red:
            for i in range(len(lst_red)):
                move = choice(lst_red)

                lst_neighbors = self.check_neighbors(move[0], move[1])
                if not lst_neighbors:
                    continue

                button = self.main_board[move[0]][move[1]]

                self.player1.turn = 1
                self.player2.turn = 0

                copy_board_red = self.get_copy_main_board()
                self.bot_evaluation_series(button, lst_neighbors, self.player1)
                self.set_copy_main_board(copy_board_red)

                tmp = self.minimax_move(depth - 1, False, alpha, beta)[0]
                if tmp > value:
                    value = tmp
                    self.best_movement_start_choice = move

                if value >= beta:
                    break
                alpha = max(alpha, value)

            return value, self.best_movement_start_choice

        else:

            value = float('inf')
            lst_blue = self.get_all_color_piece('blue')
            # for move in lst_blue:
            for i in range(len(lst_blue)):
                move = choice(lst_blue)

                lst_neighbors = self.check_neighbors(move[0], move[1])
                if not lst_neighbors:
                    continue

                button = self.main_board[move[0]][move[1]]

                self.player2.turn = 1
                self.player1.turn = 0

                copy_board_blue = self.get_copy_main_board()
                self.bot_evaluation_series(button, lst_neighbors, self.player2)
                self.set_copy_main_board(copy_board_blue)

                tmp = self.minimax_move(depth - 1, True, alpha, beta)[0]
                if tmp < value:
                    value = tmp
                    self.best_movement_start_choice = move

                if value <= alpha:
                    break
                beta = min(beta, value)

            return value, self.best_movement_start_choice

    # def minimax_end_choice(self, button, depth: int, maximizingPlayer: bool, alpha=float('-inf'), beta=float('inf')):
    #
    #     # todo: change evaluation
    #     player_win, score = self.is_end_out_bead()
    #     if depth == 0 or player_win:
    #         return score, None
    #
    #     # if depth == 0:
    #     #     return -10, None
    #
    #     if maximizingPlayer:
    #         value = float('-inf')
    #         lst_neighbors = self.check_neighbors(button.row, button.col)
    #         for move in lst_neighbors:
    #
    #             button = self.main_board[move[0]][move[1]]
    #
    #             self.player1.turn = 1
    #             self.player2.turn = 0
    #             self.choice_end_bead_to_move(button, 0)
    #
    #             tmp = self.minimax_end_choice(button, depth - 1, False, alpha, beta)[0]
    #             if tmp > value:
    #                 value = tmp
    #                 self.best_movement_end_choice = move
    #
    #             if value >= beta:
    #                 break
    #             alpha = max(alpha, value)
    #
    #         return value, self.best_movement_end_choice
    #
    #     else:
    #
    #         value = float('inf')
    #         lst_neighbors = self.check_neighbors(button.row, button.col)
    #         for move in lst_neighbors:
    #
    #             button = self.main_board[move[0]][move[1]]
    #
    #             self.player2.turn = 1
    #             self.player1.turn = 0
    #             self.choice_end_bead_to_move(button, 0)
    #
    #             tmp = self.minimax_end_choice(button, depth - 1, True, alpha, beta)[0]
    #             if tmp < value:
    #                 value = tmp
    #                 self.best_movement_end_choice = move
    #
    #             if value <= alpha:
    #                 break
    #             beta = min(beta, value)
    #
    #         return value, self.best_movement_end_choice
