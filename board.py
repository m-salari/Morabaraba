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
        self.lst_neighbors = lst_neighbors

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

        self.start_bead_move = None
        self.end_bead_move = None
        self.color_change_bead = None

        self.init_board()

        self.main_board = [[None, None, None],  # a
                           [None, None, None],  # b
                           [None, None, None],  # c
                           [None, None, None],  # d1
                           [None, None, None],  # d2
                           [None, None, None],  # e
                           [None, None, None],  # f
                           [None, None, None]]  # g

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
        # piece(QPushButton(self), 30, 36, 'a', 0, [(2,2)], 'white')
        self.main_board[0][0]: piece = piece(QPushButton(self), 30, 36, 'a', 0, lst_neighbors=[()])
        self.main_board[0][1]: piece = piece(QPushButton(self), 378, 36, 'a', None,  3)
        self.main_board[0][2]: piece = piece(QPushButton(self), 726, 36, 'a', None,  6)

        self.main_board[1][0]: piece = piece(QPushButton(self), 112, 98, 'b', None,  1)
        self.main_board[1][1]: piece = piece(QPushButton(self), 378, 94, 'b', None,  3)
        self.main_board[1][2]: piece = piece(QPushButton(self), 642, 96, 'b', None,  5)

        # self.main_board[2][0]: piece = piece(QPushButton(self), 'x', 'y', 'c', 0, [(2, 1), (3, 1,)])
        # self.main_board[2][0]: piece = piece(QPushButton(self), 206, 162, 'c', 2)
        #################################################################################

    def moving(self):
        self.main_board[0][0].button.clicked.connect(lambda: self.allow_to_move(0, 0))
        self.main_board[0][1].button.clicked.connect(lambda: self.allow_to_move(0, 1))
        self.main_board[0][2].button.clicked.connect(lambda: self.allow_to_move(0, 2))

        self.main_board[1][0].button.clicked.connect(lambda: self.allow_to_move(1, 0))
        self.main_board[1][1].button.clicked.connect(lambda: self.allow_to_move(1, 1))
        self.main_board[1][2].button.clicked.connect(lambda: self.allow_to_move(1, 2))


        # self.main_board[2][0].button.clicked.connect(lambda: self.allow_to_move(2, 0))

    # def mouseMoveEvent(self, event):
    #     print(f"x mouse: {event.x()} and y mouse: {event.y()}")

    def check_score(self):
        # todo: باید مطابق با main board درست شود
        try:
            if self.button_row_a[0].color == self.button_row_a[1].color == self.button_row_a[
                2].color != 'white':  # row a
                print('score a')

            if self.button_row_b[0].color == self.button_row_b[1].color == self.button_row_b[
                2].color != 'white':  # row b
                print('score b')

            if self.button_row_c[0].color == self.button_row_c[1].color == self.button_row_c[
                2].color != 'white':  # row c
                print('score c')

            if self.button_row_d[0].color == self.button_row_d[1].color == self.button_row_d[
                2].color != 'white':  # row d1
                print('score d1')

            if self.button_row_d[3].color == self.button_row_d[4].color == self.button_row_d[
                5].color != 'white':  # row d2
                print('score d2')

            if self.button_row_e[0].color == self.button_row_e[1].color == self.button_row_e[
                2].color != 'white':  # row e
                print('score e')

            if self.button_row_f[0].color == self.button_row_f[1].color == self.button_row_f[
                2].color != 'white':  # row f
                print('score f')

            if self.button_row_g[0].color == self.button_row_g[1].color == self.button_row_g[
                2].color != 'white':  # row g
                print('score g')

            # **  full row **

            # if self.button_row_a[0].color == self.button_row_d[0].color == self.button_row_g[0].color != 'white':  # col 0
            #     print('score col 0')

            # if self.button_row_b[0].color == self.button_row_d[1].color == self.button_row_f[0].color != 'white':  # col 1
            #     print('score col 1')

        except:
            pass

    def check_neighbors(self, row, col):
        lst_neighbors = []

        # check horizontal
        print(f'row: {row} and col: {col}')
        print(self.main_board[row][col])

        if self.main_board[row][col - 1].color == 'white':
            lst_neighbors.append((row, col - 1))

        if (col < 2) and (self.main_board[row][col + 1].color == 'white'):
            lst_neighbors.append((row, col + 1))

        if (col == 2) and (self.main_board[row][0].color == 'white'):  # if last element on row check first element
            lst_neighbors.append((row, 0))

        # check vertical

        return True

    def allow_to_move(self, row, col):
        # button: piece = self.get_button(row, col)
        button: piece = self.main_board[row][col]

        if self.player1.number_bead > 0 or self.player2.number_bead > 0:
            if button.color == 'white':
                if self.player1.turn:
                    if self.player1.number_bead > 0:
                        self.player1.number_bead -= 1
                        self.player = self.player1

                    # todo: add if number_head is last --> switch
                    if self.player2.number_bead > 0:  # switch turn
                        self.player1.turn = 0
                        self.player2.turn = 1

                elif self.player2.turn:
                    if self.player2.number_bead > 0:
                        self.player2.number_bead -= 1
                        self.player = self.player2

                    if self.player1.number_bead > 0:  # switch turn
                        self.player2.turn = 0
                        self.player1.turn = 1

                button.color = self.player.color
                button.change_button_color()
                # self.check_score()
                # print(f'{self.button_row_b[0].color}, {self.button_row_b[1].color}, {self.button_row_b[2].color}')

        elif self.player1.number_bead == 0 and self.player2.number_bead == 0:

            if button.color != 'white':  # choice start goal to move bead
                # todo: check neighbors
                lst_neighbors = self.check_neighbors(row, col)
                if lst_neighbors:  # if neighbor is empty

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
                # todo: check state end goal exist in list allowed move
                self.end_bead_move = button
                self.end_bead_move.color = self.color_change_bead
                self.end_bead_move.change_button_color()

                self.start_bead_move.color = 'white'
                self.start_bead_move.change_button_color()

                self.color_change_bead = None


App = QApplication(sys.argv)  # create pyqt5 app
window = board()  # create the instance of our Window
sys.exit(App.exec())
