from rules_game import RulesGame


class movements(RulesGame):
    def __init__(self, main_board):
        super().__init__(main_board)

    def handler_player(self, row, col):
        # button: piece = self.get_button(row, col)
        if not self.player1.turn:
            return True

        button = self.main_board[row][col]

        if self.flag_remove:
            result_remove_bead = self.remove_bead(row, col)
            if result_remove_bead:
                return True

        # insert
        # if self.player1.number_bead > 0 or self.player2.number_bead > 0:
        if self.player1.turn and self.player1.number_bead > 0:
            if button.color == 'white':
                self.insert(button, 1)
                self.switch_turn()
                return True

        # movement
        elif self.player1.number_bead == 0 and self.player2.number_bead == 0:
            if button.color != 'white':  # choice start goal to move bead
                self.choice_start_bead_to_move(button, 1)

            if button.color == 'white' and self.color_change_bead:  # choice end goal to move bead
                result_choice_end_bead = self.choice_end_bead_to_move(button, 1)
                if result_choice_end_bead:
                    if not self.flag_remove:
                        self.switch_turn()
                        return True

        return False

    def bot_evaluation_series(self, button_start, lst_neighbors, turn_player):

        change_color = self.choice_start_bead_to_move(button_start, 0)
        if not change_color:
            return False

        for i, end_piece in enumerate(lst_neighbors):

            button = self.main_board[end_piece[0]][end_piece[1]]
            self.color_change_bead = button.color

            self.choice_end_bead_to_move(button, 0)

            self.start_bead_move.color = 'yellow'
            # button_start.color = turn_player.color
            self.end_bead_move.color = 'white'

            if self.flag_remove:
                self.start_bead_move.color = 'white'
                self.end_bead_move.color = 'white'

                self.total_score_moving = 100
                self.player_win = turn_player
                # self.best_movement_end_choice.append(end_piece)
                self.flag_remove = False
                break

            # else:
            self.start_bead_move.color = 'white'
            self.end_bead_move.color = 'white'

    def get_copy_main_board(self):
        copy_board_color = []
        for i in range(len(self.main_board)):
            lst = []
            for j in range(len(self.main_board[i])):
                if self.main_board[i][j]:
                    lst.append(self.main_board[i][j].color)
                else:
                    lst.append(None)
            copy_board_color.append(lst)
        return copy_board_color

    def set_copy_main_board(self, copy_main_board):
        for i in range(len(self.main_board)):
            for j in range(len(self.main_board)):
                if self.main_board[i][j]:
                    self.main_board[i][j].color = copy_main_board[i][j]