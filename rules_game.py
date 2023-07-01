import numpy as np


class Player:
    def __init__(self, name, color, turn=0, number_bead=12):
        self.name = name
        self.color = color
        self.turn = turn
        self.score = 0
        self.number_bead = number_bead
        self.alive_bead = 0


main_board_lst = [['white', None, None, 'white', None, None, 'white'],  # a
                  [None, 'white', None, 'white', None, 'white', None],  # b
                  [None, None, 'white', 'white', 'white', None, None],  # c
                  ['white', 'white', 'white', None, 'white', 'white', 'white'],  # d
                  [None, None, 'white', 'white', 'white', None, None],  # e
                  [None, 'white', None, 'white', None, 'white', None],  # f
                  ['white', None, None, 'white', None, None, 'white']]  # g


class RulesGame:
    def __init__(self, main_board):
        self.main_board = main_board

        self.total_score_moving = 0
        self.player_win = None
        self.best_movement_end_choice = []
        print('created!')

        self.player1 = Player('player1', 'red', 1)
        self.player2 = Player('player2', 'blue')

        self.min_bead_for_game = 3
        self.lst_scores_now = []
        self.lst_neighbors = []
        self.flag_remove = False

        self.start_bead_move = None
        self.end_bead_move = None
        self.color_change_bead = None

        # self.flag_bot = 0
        # self.len_lst_score_now = 0
        # self.count_of_score_red = 0
        # self.count_of_score_blue = 0

    def insert(self, button, flag_change_color_insert):
        if self.player1.turn:
            if self.player1.number_bead > 0:
                self.player1.number_bead -= 1

                button.color = self.player1.color
                self.main_board[button.row][button.col].color = self.player1.color
                # self.main_board_lst[button.row][button.col] = self.player1.color

                self.player1.alive_bead += 1
                if flag_change_color_insert:
                    button.change_button_color()
                self.check_score()
                # return self.main_board

        elif self.player2.turn:
            if self.player2.number_bead > 0:
                self.player2.number_bead -= 1

                button.color = self.player2.color
                self.main_board[button.row][button.col].color = self.player2.color
                # self.main_board_lst[button.row][button.col] = self.player2.color

                self.player2.alive_bead += 1
                if flag_change_color_insert:
                    button.change_button_color()
                self.check_score()
                # return self.main_board

        print('count of bead red: ', self.player1.number_bead)
        print('count of bead blue: ', self.player2.number_bead)
        print("***********************\n")

    def choice_start_bead_to_move(self, button, flag_change_color_choice_start):
        row, col = button.row, button.col

        self.lst_neighbors = self.get_all_white_piece_for_min_bead('white')
        if not self.lst_neighbors:
            self.lst_neighbors = self.check_neighbors(row, col)

        if self.lst_neighbors:  # if neighbors white exist

            if self.player1.turn and button.color == self.player1.color:

                print('change color !!!!!!!! to yellow')
                self.start_bead_move = button
                self.color_change_bead = button.color

                self.start_bead_move.color = 'yellow'
                if flag_change_color_choice_start:
                    self.start_bead_move.change_button_color()

                print('success change color yellow')
                return True

            elif self.player2.turn and button.color == self.player2.color:
                print('change color !!!!!!!! to yellow')
                self.start_bead_move = button
                self.color_change_bead = button.color

                self.start_bead_move.color = 'yellow'
                if flag_change_color_choice_start:
                    self.start_bead_move.change_button_color()

                print('success change color yellow')
                return True
        return False

    def choice_end_bead_to_move(self, button, flag_change_color_choice_end):
        if (button.row, button.col) not in self.lst_neighbors:  # check state end goal exist in list allowed move
            return False

        self.end_bead_move = button
        self.end_bead_move.color = self.color_change_bead

        if flag_change_color_choice_end:
            self.end_bead_move.change_button_color()

        self.start_bead_move.color = 'white'
        if flag_change_color_choice_end:
            self.start_bead_move.change_button_color()

        self.color_change_bead = None
        self.lst_neighbors = []
        self.check_score()

        return True

    def switch_turn(self):
        if not self.flag_remove:
            if self.player1.number_bead == 0 and self.player2.number_bead == 0:
                if self.player1.turn:
                    self.player1.turn = 0
                    self.player2.turn = 1

                elif self.player2.turn:
                    self.player2.turn = 0
                    self.player1.turn = 1

            #  then if still enemy bead exist OR last bead player --> switch
            elif self.player1.turn and self.player2.number_bead > 0:
                self.player1.turn = 0
                self.player2.turn = 1

            #  then if still enemy bead exist OR last bead player --> switch
            elif self.player2.turn and self.player1.number_bead > 0:
                self.player2.turn = 0
                self.player1.turn = 1

    def get_turn_player(self):
        if self.player1.turn:
            return self.player1
        return self.player2

    def check_neighbors(self, row, col):
        lst_neighbors = []
        button = self.main_board[row][col]

        for row, col in button.neighbors:
            if self.main_board[row][col].color == 'white':
                lst_neighbors.append((row, col))

        return lst_neighbors

    def get_all_white_piece_for_min_bead(self, color):

        if self.player1.turn:
            enemy = self.player1
        else:
            enemy = self.player2

        if enemy.alive_bead <= self.min_bead_for_game:
            return self.get_all_color_piece(color)

    def get_all_color_piece(self, color):
        lst_all_color_piece = []

        for row in range(len(self.main_board)):
            for col in range(len(self.main_board[row])):
                if self.main_board[row][col]:
                    if self.main_board[row][col].color == color:
                        lst_all_color_piece.append((row, col))

        return lst_all_color_piece

    def check_score(self):
        # check latest scores is change --> delete from list score
        for i, score in enumerate(self.lst_scores_now):
            a = int(score[0])
            b = int(score[1])
            c = int(score[2])
            d = int(score[3])
            e = int(score[4])
            f = int(score[5])

            if not (self.main_board[a][b].color == self.main_board[c][d].color == self.main_board[e][f].color):
                del self.lst_scores_now[i]

        if self.main_board[0][0].color == self.main_board[0][3].color == self.main_board[0][6].color != 'white' \
                and '000306' not in self.lst_scores_now:
            # print('0')
            self.lst_scores_now.append('000306')
            self.flag_remove = True

        if self.main_board[1][1].color == self.main_board[1][3].color == self.main_board[1][5].color != 'white' \
                and '111315' not in self.lst_scores_now:  # row b
            # print('1')
            self.lst_scores_now.append('111315')
            self.flag_remove = True

        if self.main_board[2][2].color == self.main_board[2][3].color == self.main_board[2][4].color != 'white' \
                and '222324' not in self.lst_scores_now:  # row c
            # print('2')
            self.lst_scores_now.append('222324')
            self.flag_remove = True

        if self.main_board[3][0].color == self.main_board[3][1].color == self.main_board[3][2].color != 'white' \
                and '303132' not in self.lst_scores_now:  # row d1
            # print('3')
            self.lst_scores_now.append('303132')
            self.flag_remove = True

        if self.main_board[3][4].color == self.main_board[3][5].color == self.main_board[3][6].color != 'white' \
                and '343536' not in self.lst_scores_now:  # row d2
            # print('4')
            self.lst_scores_now.append('343536')
            self.flag_remove = True

        if self.main_board[4][2].color == self.main_board[4][3].color == self.main_board[4][4].color != 'white' \
                and '424344' not in self.lst_scores_now:  # row e
            # print('5')
            self.lst_scores_now.append('424344')
            self.flag_remove = True

        if self.main_board[5][1].color == self.main_board[5][3].color == self.main_board[5][5].color != 'white' \
                and '515355' not in self.lst_scores_now:  # row f
            # print('6')
            self.lst_scores_now.append('515355')
            self.flag_remove = True

        if self.main_board[6][0].color == self.main_board[6][3].color == self.main_board[6][6].color != 'white' \
                and '606366' not in self.lst_scores_now:  # row g
            # print('7')
            self.lst_scores_now.append('606366')
            self.flag_remove = True

        # **  full row **

        if self.main_board[0][0].color == self.main_board[3][0].color == self.main_board[6][0].color != 'white' \
                and '003060' not in self.lst_scores_now:
            # print('8')
            self.lst_scores_now.append('003060')
            self.flag_remove = True

        if self.main_board[1][1].color == self.main_board[3][1].color == self.main_board[5][1].color != 'white' \
                and '113151' not in self.lst_scores_now:
            # print('9')
            self.lst_scores_now.append('113151')
            self.flag_remove = True

        if self.main_board[2][2].color == self.main_board[3][2].color == self.main_board[4][2].color != 'white' \
                and '223242' not in self.lst_scores_now:
            # print('10')
            self.lst_scores_now.append('223242')
            self.flag_remove = True

        if self.main_board[0][3].color == self.main_board[1][3].color == self.main_board[2][3].color != 'white' \
                and '031323' not in self.lst_scores_now:
            # print('11')
            self.lst_scores_now.append('031323')
            self.flag_remove = True

        if self.main_board[4][3].color == self.main_board[5][3].color == self.main_board[6][3].color != 'white' \
                and '435363' not in self.lst_scores_now:
            # print('12')
            self.lst_scores_now.append('435363')
            self.flag_remove = True

        if self.main_board[2][4].color == self.main_board[3][4].color == self.main_board[4][4].color != 'white' \
                and '243444' not in self.lst_scores_now:
            # print('13')
            self.lst_scores_now.append('243444')
            self.flag_remove = True

        if self.main_board[1][5].color == self.main_board[3][5].color == self.main_board[5][5].color != 'white' \
                and '153555' not in self.lst_scores_now:
            # print('14')
            self.lst_scores_now.append('153555')
            self.flag_remove = True

        if self.main_board[0][6].color == self.main_board[3][6].color == self.main_board[6][6].color != 'white' \
                and '063666' not in self.lst_scores_now:
            # print('15')
            self.lst_scores_now.append('063666')
            self.flag_remove = True

        # ** full col **

        if self.main_board[0][0].color == self.main_board[1][1].color == self.main_board[2][2].color != 'white' \
                and '001122' not in self.lst_scores_now:
            # print('16')
            self.lst_scores_now.append('001122')
            self.flag_remove = True

        if self.main_board[0][6].color == self.main_board[1][5].color == self.main_board[2][4].color != 'white' \
                and '061524' not in self.lst_scores_now:
            # print('17')
            self.lst_scores_now.append('061524')
            self.flag_remove = True

        if self.main_board[6][0].color == self.main_board[5][1].color == self.main_board[4][2].color != 'white' \
                and '605142' not in self.lst_scores_now:
            # print('18')
            self.lst_scores_now.append('605142')
            self.flag_remove = True

        if self.main_board[6][6].color == self.main_board[5][5].color == self.main_board[4][4].color != 'white' \
                and '665544' not in self.lst_scores_now:
            # print('19')
            self.lst_scores_now.append('665544')
            self.flag_remove = True

            # ** full skew **
            # self.flag_remove = self.remove_from_out_bead(self.flag_remove)
        self.remove_from_out_bead()

    def remove_from_out_bead(self):
        if self.flag_remove:
            if self.player1.turn and self.player2.number_bead > 0:
                self.player2.number_bead -= 1
                self.flag_remove = False

            elif self.player2.turn and self.player1.number_bead > 0:
                self.player1.number_bead -= 1
                self.flag_remove = False

    def remove_bead(self, row, col):

        button = self.main_board[row][col]
        player_turn = self.get_turn_player()

        if (player_turn.color != button.color) and (button.color != 'white'):
            button.color = 'white'
            button.change_button_color()
            self.flag_remove = False

            if player_turn == self.player1:
                self.player2.alive_bead -= 1
                # self.flag_bot = 3
                # self.bot()
                self.switch_turn()

            else:
                self.player1.alive_bead -= 1
                # self.flag_bot = 0
                self.switch_turn()
            self.check_win()

            return True

        else:
            print('can not delete this bead')

        return False

    def check_win(self):
        if self.player1.alive_bead < self.min_bead_for_game:
            print('player 2 is winner')

        elif self.player2.alive_bead < self.min_bead_for_game:
            print('player 1 is winner')

    def get_enemy_player(self):
        if self.player1.turn:
            return self.player2
        else:
            return self.player1
