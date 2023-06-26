from rules_game import RulesGame


class movements(RulesGame):
    def __init__(self, main_board):
        super().__init__(main_board)

    def handler_player(self, row, col):
        # button: piece = self.get_button(row, col)
        button = self.main_board[row][col]

        if self.flag_remove:
            result_remove_bead = self.remove_bead(row, col)
            if result_remove_bead:
                return True

        # insert
        # if self.player1.number_bead > 0 or self.player2.number_bead > 0:
        if self.player1.turn and self.player1.number_bead > 0:
            if button.color == 'white':
                self.insert(button)
                self.switch_turn()
                return True

        # movement
        elif self.player1.number_bead == 0 and self.player2.number_bead == 0:
            if button.color != 'white':  # choice start goal to move bead
                self.choice_start_bead_to_move(button)

            if button.color == 'white' and self.color_change_bead:  # choice end goal to move bead
                result_choice_end_bead = self.choice_end_bead_to_move(button)
                if result_choice_end_bead:
                    self.switch_turn()
                    return True

        return False
