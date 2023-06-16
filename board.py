# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from rules import player


class piece:
    def __init__(self, button, x, y, row, col, lst_neighbors, color='white'):
        self.button: QPushButton = button
        self.x = x
        self.y = y
        self.row = row
        self.col = col
        self.color = color
        self.button.setGeometry(x, y, 40, 40)
        self.button.setStyleSheet("border-radius : 20; "
                                  "border : 2px solid black;")
        self.neighbors = lst_neighbors

    def change_button_color(self):
        # print('color:', self.color)
        if self.color == 'red':
            self.button.setStyleSheet("border-radius : 20; "
                                      "border : 2px solid black;"
                                      "background-image : url(/Users/euleday/mostafa/umz/game theory/morabaraba/images/red.png);")

        elif self.color == 'blue':
            self.button.setStyleSheet("border-radius : 20; "
                                      "border : 2px solid black;"
                                      "background-image : url(/Users/euleday/mostafa/umz/game theory/morabaraba/images/blue.jpg);")

        elif self.color == 'yellow':
            self.button.setStyleSheet("border-radius : 20; "
                                      "border : 2px solid black;"
                                      "background-image : url(/Users/euleday/mostafa/umz/game theory/morabaraba/images/yellow.jpg);")

        elif self.color == 'white':
            self.button.setStyleSheet("border-radius : 20; "
                                      "border : 2px solid black;"
                                      "background-image : url(/Users/euleday/mostafa/umz/game theory/morabaraba/images/white.png);")


class board(QMainWindow):
    def __init__(self):
        super().__init__()
        self.player = None
        self.player1 = player('player1', 'red', 1, number_bead=3)
        self.player2 = player('player2', 'blue')

        self.lst_neighbors = []
        self.start_bead_move = None
        self.end_bead_move = None
        self.color_change_bead = None
        self.flag_remove = False

        self.init_board()

        self.main_board = [[None, None, None, None, None, None, None],  # a
                           [None, None, None, None, None, None, None],  # b
                           [None, None, None, None, None, None, None],  # c
                           [None, None, None, None, None, None, None],  # d
                           # [None, None, None, None, None, None, None],  # d2
                           [None, None, None, None, None, None, None],  # e
                           [None, None, None, None, None, None, None],  # f
                           [None, None, None, None, None, None, None]]  # g

        # self.button_row_a = [None, None, None]
        # self.button_row_b = [None, None, None]
        # self.button_row_c = [None, None, None]
        # self.button_row_d = [None, None, None, None, None, None]
        # self.button_row_e = [None, None, None]
        # self.button_row_f = [None, None, None]
        # self.button_row_g = [None, None, None]

        self.draw_pieces()
        self.moving()
        self.show()

    def init_board(self):
        # setting title
        self.setWindowTitle("morabaraba")

        # setting geometry
        self.setGeometry(100, 100, 800, 600)

        self.setStyleSheet("""
        background-image: url("/Users/euleday/mostafa/umz/game theory/morabaraba/images/1.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;""")

    def draw_pieces(self):
        self.main_board[0][0]: piece = piece(QPushButton(self), 30, 36, row=0, col=0,
                                             lst_neighbors=[(0, 3), (3, 0), (1, 1)])
        self.main_board[0][3]: piece = piece(QPushButton(self), 378, 36, row=0, col=3,
                                             lst_neighbors=[(0, 0), (0, 6), (1, 3)])
        self.main_board[0][6]: piece = piece(QPushButton(self), 726, 36, row=0, col=6,
                                             lst_neighbors=[(0, 3), (4, 6), (1, 5)])

        self.main_board[1][1]: piece = piece(QPushButton(self), 112, 98, row=1, col=1,
                                             lst_neighbors=[(0, 0), (2, 2), (1, 3), (3, 1)])
        self.main_board[1][3]: piece = piece(QPushButton(self), 378, 94, row=1, col=3,
                                             lst_neighbors=[(1, 1), (1, 5), (0, 3), (2, 3)])
        self.main_board[1][5]: piece = piece(QPushButton(self), 642, 96, row=1, col=5,
                                             lst_neighbors=[(1, 3), (4, 5), (0, 6), (2, 4)])

    def moving(self):
        # a
        self.main_board[0][0].button.clicked.connect(
            lambda: self.allow_to_move(0, 0) if not self.flag_remove else self.remove_bead(0, 0))

        self.main_board[0][3].button.clicked.connect(
            lambda: self.allow_to_move(0, 3) if not self.flag_remove else self.remove_bead(0, 3))

        self.main_board[0][6].button.clicked.connect(
            lambda: self.allow_to_move(0, 6) if not self.flag_remove else self.remove_bead(0, 6))

        # b
        self.main_board[1][1].button.clicked.connect(
            lambda: self.allow_to_move(1, 1) if not self.flag_remove else self.remove_bead(1, 1))

        self.main_board[1][3].button.clicked.connect(
            lambda: self.allow_to_move(1, 3) if not self.flag_remove else self.remove_bead(1, 3))

        self.main_board[1][5].button.clicked.connect(
            lambda: self.allow_to_move(1, 5) if not self.flag_remove else self.remove_bead(1, 5))

    # def mouseMoveEvent(self, event):
    #     print(f"x mouse: {event.x()} and y mouse: {event.y()}")

    def remove_bead(self, row, col):
        button: piece = self.main_board[row][col]
        if self.player.color != button.color:
            button.color = 'white'
            button.change_button_color()
            self.flag_remove = False
        else:
            print('pass')

    def check_score(self):
        try:
            if self.main_board[0][0].color == self.main_board[0][3].color == self.main_board[0][6].color != 'white':  # row a
                print('score a')
                self.flag_remove = True

            if self.main_board[1][1].color == self.main_board[1][3].color == self.main_board[1][5].color != 'white':  # row b
                print('score b')
                self.flag_remove = True

            if self.main_board[2][2].color == self.main_board[2][3].color == self.main_board[2][4].color != 'white':  # row c
                print('score c')
                self.flag_remove = True

            if self.main_board[3][0].color == self.main_board[3][1].color == self.main_board[3][2].color != 'white':  # row d1
                print('score d1')
                self.flag_remove = True

            if self.main_board[3][4].color == self.main_board[3][5].color == self.main_board[3][6].color != 'white':  # row d2
                print('score d2')
                self.flag_remove = True

            if self.main_board[4][2].color == self.main_board[4][3].color == self.main_board[4][4].color != 'white':  # row e
                print('score e')
                self.flag_remove = True

            if self.main_board[5][1].color == self.main_board[5][3].color == self.main_board[5][5].color != 'white':  # row f
                print('score f')
                self.flag_remove = True

            if self.main_board[6][0].color == self.main_board[6][3].color == self.main_board[6][6].color != 'white':  # row g
                print('score g')
                self.flag_remove = True


            # **  full row **

        except:
            pass

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

    def allow_to_move(self, row, col):
        # button: piece = self.get_button(row, col)
        button: piece = self.main_board[row][col]

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

                self.check_score()
                # print(f'{self.button_row_b[0].color}, {self.button_row_b[1].color}, {self.button_row_b[2].color}')

        elif self.player1.number_bead == 0 and self.player2.number_bead == 0:

            if button.color != 'white':  # choice start goal to move bead
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

App = QApplication(sys.argv)  # create pyqt5 app
window = board()  # create the instance of our Window
sys.exit(App.exec())
