from bot import Bot


class game_loop(Bot):
    def __init__(self, main_board):
        super().__init__(main_board)

    def main(self, row, col):
        result_player_movement = self.handler_player(row, col)

        # if you may play with your friend comment it.
        # then uncomment "if self.player1.number_bead > 0 or self.player2.number_bead > 0:" and
        # comment it "if self.player1.turn and self.player1.number_bead > 0:" in handler player
        if result_player_movement:
            self.bot_handler()



