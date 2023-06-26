from random import choice
from movements import movements


class Bot(movements):
    def __init__(self, main_board, bot_color='blue'):
        super().__init__(main_board)
        self.bot_color = bot_color

    def bot_insert(self):
        lst_white_piece = self.get_all_color_piece('white')
        random_insert = choice(lst_white_piece)
        print('insert random choice :', random_insert)
        button = self.main_board[random_insert[0]][random_insert[1]]

        self.insert(button)
        self.switch_turn()

    def bot_choice_start_bead_to_move(self):
        lst_bot_color_piece = self.get_all_color_piece(self.bot_color)
        random_start_bead_to_move = choice(lst_bot_color_piece)

        self.lst_neighbors = self.get_all_white_piece_for_min_bead('white')
        if not self.lst_neighbors:
            self.lst_neighbors = self.check_neighbors(random_start_bead_to_move[0], random_start_bead_to_move[1])
        while True:
            if self.lst_neighbors:
                break

            lst_bot_color_piece.remove(random_start_bead_to_move)
            random_start_bead_to_move = choice(lst_bot_color_piece)
            self.lst_neighbors = self.check_neighbors(random_start_bead_to_move[0], random_start_bead_to_move[1])

        button = self.main_board[random_start_bead_to_move[0]][random_start_bead_to_move[1]]
        return self.choice_start_bead_to_move(button)

    def bot_choice_end_bead_to_move(self):
        random_end_bead_to_move = choice(self.lst_neighbors)
        button = self.main_board[random_end_bead_to_move[0]][random_end_bead_to_move[1]]

        if self.choice_end_bead_to_move(button):
            self.switch_turn()

    def bot_remove_bead(self):
        lst_enemy_piece = self.get_all_color_piece('red')
        random_remove_piece = choice(lst_enemy_piece)
        print('position random remove:', random_remove_piece)
        return self.remove_bead(random_remove_piece[0], random_remove_piece[1])

    def bot_handler(self):

        if self.flag_remove:
            result_remove_bead = self.bot_remove_bead()
            if result_remove_bead:
                return True

        if self.player2.turn and self.player2.number_bead > 0:
            self.bot_insert()

        elif self.player1.number_bead == 0 and self.player2.number_bead == 0:
            result_choice_start_bead = self.bot_choice_start_bead_to_move()

            if result_choice_start_bead:
                self.bot_choice_end_bead_to_move()
