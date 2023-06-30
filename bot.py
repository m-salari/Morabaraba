from algorithms_movement import algorithms
from copy import deepcopy

class Bot(algorithms):
    def __init__(self, main_board, bot_color='blue'):
        super().__init__(main_board)
        self.bot_color = bot_color

    def bot_insert(self):

        random_insert = self.random('white')
        button = self.main_board[random_insert[0]][random_insert[1]]

        if self.player2.number_bead <= 10:
            lst_score_now = deepcopy(self.lst_scores_now)
            value, qx, qy = self.min_alpha_beta(float('-inf'), float('inf'))
            print('valueeeeeeeeeee:', value)
            print('insert random choice :', (qx, qy))
            self.lst_scores_now = lst_score_now
            button = self.main_board[qx][qy]

        self.player2.turn = 1
        self.player1.turn = 0

        self.insert(button, 1)
        self.switch_turn()

    def bot_choice_start_bead_to_move(self):
        random_start_bead_to_move = self.random(self.bot_color)
        self.lst_neighbors = self.get_all_white_piece_for_min_bead('white')
        if not self.lst_neighbors:
            self.lst_neighbors = self.check_neighbors(random_start_bead_to_move[0], random_start_bead_to_move[1])
        while True:
            if self.lst_neighbors:
                break
            random_start_bead_to_move = self.random(self.bot_color)
            self.lst_neighbors = self.check_neighbors(random_start_bead_to_move[0], random_start_bead_to_move[1])

        button = self.main_board[random_start_bead_to_move[0]][random_start_bead_to_move[1]]
        return self.choice_start_bead_to_move(button)

    def bot_choice_end_bead_to_move(self):
        random_end_bead_to_move = self.random(None, self.lst_neighbors)
        button = self.main_board[random_end_bead_to_move[0]][random_end_bead_to_move[1]]

        if self.choice_end_bead_to_move(button):
            if not self.flag_remove:
                self.switch_turn()

    def bot_remove_bead(self):
        random_remove_piece = self.random('red')
        print('position random remove:', random_remove_piece)
        return self.remove_bead(random_remove_piece[0], random_remove_piece[1])

    def bot_handler(self):
        if not self.player2.turn:
            return True

        if self.player2.turn and self.player2.number_bead > 0:
            self.bot_insert()

        elif self.player1.number_bead == 0 and self.player2.number_bead == 0:
            result_choice_start_bead = self.bot_choice_start_bead_to_move()

            if result_choice_start_bead:
                self.bot_choice_end_bead_to_move()

        if self.flag_remove:
            result_remove_bead = self.bot_remove_bead()
            if result_remove_bead:
                return True