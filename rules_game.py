class player:
    def __init__(self, name, color, turn=0, number_bead=12):
        self.name = name
        self.color = color
        self.turn = turn
        self.score = 0
        self.number_bead = number_bead
        self.alive_bead = 0


class rules:
    def __init__(self, main_board):
        self.main_board = main_board

        self.player = None
        self.player1 = player('player1', 'red', 1)
        self.player2 = player('player2', 'blue')

        self.min_bead_for_game = 3
        self.lst_scores_now = []
        self.lst_neighbors = []
        self.start_bead_move = None
        self.end_bead_move = None
        self.color_change_bead = None
        self.flag_remove = False

    def allow_to_move(self, row, col):
        # button: piece = self.get_button(row, col)
        button = self.main_board[row][col]


        if self.player1.number_bead > 0 or self.player2.number_bead > 0:
            if button.color == 'white':
                if self.player1.turn:
                    if self.player1.number_bead > 0:
                        self.player1.number_bead -= 1
                        self.player = self.player1

                        #  if last bead --> switch
                    if self.player2.number_bead > 0 or self.player1.number_bead == 0:  # switch turn
                        self.player1.turn = 0
                        self.player2.turn = 1

                elif self.player2.turn:
                    if self.player2.number_bead > 0:
                        self.player2.number_bead -= 1
                        self.player = self.player2
                        # if last bead --> switch
                    if self.player1.number_bead > 0 or self.player2.number_bead == 0:  # switch turn
                        self.player2.turn = 0
                        self.player1.turn = 1

                button.color = self.player.color
                button.change_button_color()
                self.player.alive_bead += 1
                self.check_score()
                # print(f'{self.button_row_b[0].color}, {self.button_row_b[1].color}, {self.button_row_b[2].color}')

                # print('player1 red number head out: ', self.player1.number_bead)
                # print('player2 blue number head out: ', self.player2.number_bead)

        elif self.player1.number_bead == 0 and self.player2.number_bead == 0:

            if button.color != 'white':  # choice start goal to move bead

                self.lst_neighbors = self.get_all_white_piece()
                if not self.lst_neighbors:
                    self.lst_neighbors = self.check_neighbors(row, col)

                if self.lst_neighbors:  # if neighbors white exist

                    flag_turn = False  # check color to is allowed
                    if self.player1.turn and button.color == self.player1.color:
                        self.player = self.player1
                        self.player1.turn = 0
                        self.player2.turn = 1
                        flag_turn = True

                    elif self.player2.turn and button.color == self.player2.color:
                        self.player = self.player2
                        self.player2.turn = 0
                        self.player1.turn = 1
                        flag_turn = True

                    if flag_turn:
                        self.start_bead_move = button
                        self.color_change_bead = button.color

                        self.start_bead_move.color = 'yellow'
                        self.start_bead_move.change_button_color()

            if button.color == 'white' and self.color_change_bead:  # choice end goal to move bead
                if (button.row, button.col) in self.lst_neighbors:  # check state end goal exist in list allowed move

                    self.end_bead_move = button
                    self.end_bead_move.color = self.color_change_bead
                    self.end_bead_move.change_button_color()

                    self.start_bead_move.color = 'white'
                    self.start_bead_move.change_button_color()

                    self.color_change_bead = None
                    self.lst_neighbors = []

                    self.check_score()

    def check_neighbors(self, row, col):
        lst_neighbors = []
        button = self.main_board[row][col]

        for row, col in button.neighbors:
            try:
                if self.main_board[row][col].color == 'white':
                    lst_neighbors.append((row, col))

            except:  # به خاطر اینکه هنوز صفحه کامل نیستو بعد از کامل شدن try برداشته شود
                pass

        return lst_neighbors

    def get_all_white_piece(self):
        lst_all_white_piece = []

        if self.player == self.player1:
            turn = self.player2
        else:
            turn = self.player1
        print('\nturnnnnn alive nead\n:', turn.alive_bead)
        if turn.alive_bead == self.min_bead_for_game:
            for row in range(len(self.main_board)):
                for col in range(len(self.main_board[row])):
                    if self.main_board[row][col]:
                        if self.main_board[row][col].color == 'white':
                            lst_all_white_piece.append((row, col))

            print('lst all white piece:', lst_all_white_piece)
        return lst_all_white_piece

    def check_score(self):
        try:
            # check latest scores is change --> delete lst score
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
                print('0')
                self.lst_scores_now.append('000306')
                self.flag_remove = True

            if self.main_board[1][1].color == self.main_board[1][3].color == self.main_board[1][5].color != 'white' \
                    and '111315' not in self.lst_scores_now:  # row b
                print('1')
                self.lst_scores_now.append('111315')
                self.flag_remove = True

            if self.main_board[2][2].color == self.main_board[2][3].color == self.main_board[2][4].color != 'white' \
                    and '222324' not in self.lst_scores_now:  # row c
                print('2')
                self.lst_scores_now.append('222324')
                self.flag_remove = True

            if self.main_board[3][0].color == self.main_board[3][1].color == self.main_board[3][2].color != 'white' \
                    and '303132' not in self.lst_scores_now:  # row d1
                print('3')
                self.lst_scores_now.append('303132')
                self.flag_remove = True

            if self.main_board[3][4].color == self.main_board[3][5].color == self.main_board[3][6].color != 'white' \
                    and '343536' not in self.lst_scores_now:  # row d2
                print('4')
                self.lst_scores_now.append('343536')
                self.flag_remove = True

            if self.main_board[4][2].color == self.main_board[4][3].color == self.main_board[4][4].color != 'white' \
                    and '424344' not in self.lst_scores_now:  # row e
                print('5')
                self.lst_scores_now.append('424344')
                self.flag_remove = True

            if self.main_board[5][1].color == self.main_board[5][3].color == self.main_board[5][5].color != 'white' \
                    and '515355' not in self.lst_scores_now:  # row f
                print('6')
                self.lst_scores_now.append('515355')
                self.flag_remove = True

            if self.main_board[6][0].color == self.main_board[6][3].color == self.main_board[6][6].color != 'white' \
                    and '606366' not in self.lst_scores_now:  # row g
                print('7')
                self.lst_scores_now.append('606366')
                self.flag_remove = True

            # **  full row **

            if self.main_board[0][0].color == self.main_board[3][0].color == self.main_board[6][0].color != 'white' \
                    and '003060' not in self.lst_scores_now:
                print('8')
                self.lst_scores_now.append('003060')
                self.flag_remove = True

            if self.main_board[1][1].color == self.main_board[3][1].color == self.main_board[5][1].color != 'white' \
                    and '113151' not in self.lst_scores_now:
                print('9')
                self.lst_scores_now.append('113151')
                self.flag_remove = True

            if self.main_board[2][2].color == self.main_board[3][2].color == self.main_board[4][2].color != 'white' \
                    and '223242' not in self.lst_scores_now:
                print('10')
                self.lst_scores_now.append('223242')
                self.flag_remove = True

            if self.main_board[0][3].color == self.main_board[1][3].color == self.main_board[2][3].color != 'white' \
                    and '031323' not in self.lst_scores_now:
                print('11')
                self.lst_scores_now.append('031323')
                self.flag_remove = True

            if self.main_board[4][3].color == self.main_board[5][3].color == self.main_board[6][3].color != 'white' \
                    and '435363' not in self.lst_scores_now:
                print('12')
                self.lst_scores_now.append('435363')
                self.flag_remove = True

            if self.main_board[2][4].color == self.main_board[3][4].color == self.main_board[4][4].color != 'white' \
                    and '243444' not in self.lst_scores_now:
                print('13')
                self.lst_scores_now.append('243444')
                self.flag_remove = True

            if self.main_board[1][5].color == self.main_board[3][5].color == self.main_board[5][5].color != 'white' \
                    and '153555' not in self.lst_scores_now:
                print('14')
                self.lst_scores_now.append('153555')
                self.flag_remove = True

            if self.main_board[0][6].color == self.main_board[3][6].color == self.main_board[6][6].color != 'white' \
                    and '063666' not in self.lst_scores_now:
                print('15')
                self.lst_scores_now.append('063666')
                self.flag_remove = True

            # ** full col **

            if self.main_board[0][0].color == self.main_board[1][1].color == self.main_board[2][2].color != 'white' \
                    and '001122' not in self.lst_scores_now:
                print('16')
                self.lst_scores_now.append('001122')
                self.flag_remove = True

            if self.main_board[0][6].color == self.main_board[1][5].color == self.main_board[2][4].color != 'white' \
                    and '061524' not in self.lst_scores_now:
                print('17')
                self.lst_scores_now.append('061524')
                self.flag_remove = True

            if self.main_board[6][0].color == self.main_board[5][1].color == self.main_board[4][2].color != 'white' \
                    and '605142' not in self.lst_scores_now:
                print('18')
                self.lst_scores_now.append('605142')
                self.flag_remove = True

            if self.main_board[6][6].color == self.main_board[5][5].color == self.main_board[4][4].color != 'white' \
                    and '665544' not in self.lst_scores_now:
                print('19')
                self.lst_scores_now.append('665544')
                self.flag_remove = True

            # ** full skew **
            self.remove_from_number_head()
            # print('scores: ', self.lst_scores_now)

        except:
            pass

    def remove_from_number_head(self):
        if self.flag_remove:
            print('player1 red number head out before remove: ', self.player1.number_bead)
            print('player2 blue number head out before remove: ', self.player2.number_bead)

            if self.player == self.player1 and self.player2.number_bead > 0:
                self.player2.number_bead -= 1
                self.flag_remove = False

            elif self.player == self.player2 and self.player1.number_bead > 0:
                self.player1.number_bead -= 1
                self.flag_remove = False

            print('player1 red number head out: ', self.player1.number_bead)
            print('player2 blue number head out: ', self.player2.number_bead)
            print('*************************\t')

    def remove_bead(self, row, col):

        button = self.main_board[row][col]
        if self.player.color != button.color:
            button.color = 'white'
            button.change_button_color()
            self.flag_remove = False

            if self.player == self.player1:
                self.player2.alive_bead -= 1

            if self.player == self.player2:
                self.player1.alive_bead -= 1

            self.check_win()
        else:
            print('can not delete this bead')

    def check_win(self):
        if self.player1.alive_bead < self.min_bead_for_game:
            print('player 2 is winner')

        elif self.player2.alive_bead < self.min_bead_for_game:
            print('player 1 is winner')
