# importing libraries
import sys
import os
from PyQt5.QtWidgets import *
from rules_game import rules

_wd = os.getcwd()

main_board = [[None, None, None, None, None, None, None],  # a
               [None, None, None, None, None, None, None],  # b
               [None, None, None, None, None, None, None],  # c
               [None, None, None, None, None, None, None],  # d
               [None, None, None, None, None, None, None],  # e
               [None, None, None, None, None, None, None],  # f
               [None, None, None, None, None, None, None]]  # g


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
                                      f"background-image : url({_wd}/images/images/red.png);")

        elif self.color == 'blue':
            self.button.setStyleSheet("border-radius : 20; "
                                      "border : 2px solid black;"
                                      f"background-image : url({_wd}/images/images/blue.jpg);")

        elif self.color == 'yellow':
            self.button.setStyleSheet("border-radius : 20; "
                                      "border : 2px solid black;"
                                      f"background-image : url({_wd}/images/images/yellow.jpg);")

        elif self.color == 'white':
            self.button.setStyleSheet("border-radius : 20; "
                                      "border : 2px solid black;"
                                      f"background-image : url({_wd}/images/images/white.png);")


class board(QMainWindow):
    def __init__(self):
        super().__init__()

        self.rule = rules(main_board)
        self.main_board = self.rule.main_board

        self.init_board()
        self.draw_pieces()
        self.moving()
        self.show()

    def init_board(self):
        # setting title
        self.setWindowTitle("morabaraba")

        # setting geometry
        self.setGeometry(100, 100, 800, 600)

        self.setStyleSheet(f"""
        background-image: url("{_wd}/images/images/board.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;""")

    def draw_pieces(self):
        # a
        self.main_board[0][0]: piece = piece(QPushButton(self), 30, 36, row=0, col=0,
                                             lst_neighbors=[(0, 3), (3, 0), (1, 1)])

        self.main_board[0][3]: piece = piece(QPushButton(self), 378, 36, row=0, col=3,
                                             lst_neighbors=[(0, 0), (0, 6), (1, 3)])

        self.main_board[0][6]: piece = piece(QPushButton(self), 726, 36, row=0, col=6,
                                             lst_neighbors=[(0, 3), (3, 6), (1, 5)])

        # b
        self.main_board[1][1]: piece = piece(QPushButton(self), 112, 98, row=1, col=1,
                                             lst_neighbors=[(0, 0), (2, 2), (1, 3), (3, 1)])

        self.main_board[1][3]: piece = piece(QPushButton(self), 378, 94, row=1, col=3,
                                             lst_neighbors=[(1, 1), (1, 5), (0, 3), (2, 3)])

        self.main_board[1][5]: piece = piece(QPushButton(self), 642, 96, row=1, col=5,
                                             lst_neighbors=[(1, 3), (3, 5), (0, 6), (2, 4)])

        # c

        self.main_board[2][2]: piece = piece(QPushButton(self), 206, 161, row=2, col=2,
                                             lst_neighbors=[(1, 1), (3, 2), (2, 3)])

        self.main_board[2][3]: piece = piece(QPushButton(self), 378, 158, row=2, col=3,
                                             lst_neighbors=[(1, 3), (2, 4), (2, 2)])

        self.main_board[2][4]: piece = piece(QPushButton(self), 556, 161, row=2, col=4,
                                             lst_neighbors=[(1, 5), (2, 3), (3, 4)])

        # d1
        self.main_board[3][0]: piece = piece(QPushButton(self), 32, 281, row=3, col=0,
                                             lst_neighbors=[(0, 0), (6, 0), (3, 1)])

        self.main_board[3][1]: piece = piece(QPushButton(self), 111, 282, row=3, col=1,
                                             lst_neighbors=[(3, 0), (1, 1), (3, 2), (5, 1)])

        self.main_board[3][2]: piece = piece(QPushButton(self), 205, 282, row=3, col=2,
                                             lst_neighbors=[(2, 2), (3, 1), (4, 2)])

        # d2

        self.main_board[3][4]: piece = piece(QPushButton(self), 561, 282, row=3, col=4,
                                             lst_neighbors=[(2, 4), (3, 5), (4, 4)])

        self.main_board[3][5]: piece = piece(QPushButton(self), 650, 284, row=3, col=5,
                                             lst_neighbors=[(1, 5), (5, 5), (3, 4), (3, 6)])

        self.main_board[3][6]: piece = piece(QPushButton(self), 730, 284, row=3, col=6,
                                             lst_neighbors=[(0, 6), (6, 6), (3, 5)])

        # e

        self.main_board[4][2]: piece = piece(QPushButton(self), 210, 402, row=4, col=2,
                                             lst_neighbors=[(3, 2), (4, 3), (5, 1)])

        self.main_board[4][3]: piece = piece(QPushButton(self), 380, 408, row=4, col=3,
                                             lst_neighbors=[(4, 2), (4, 4), (5, 3)])

        self.main_board[4][4]: piece = piece(QPushButton(self), 558 , 406, row=4, col=4,
                                             lst_neighbors=[(4, 3), (3, 4), (5, 5)])

        # f

        self.main_board[5][1]: piece = piece(QPushButton(self), 116, 471, row=5, col=1,
                                             lst_neighbors=[(4, 2), (3, 1), (6, 0), (5, 3)])

        self.main_board[5][3]: piece = piece(QPushButton(self), 380, 468, row=5, col=3,
                                             lst_neighbors=[(5, 1), (4, 3), (5, 5), (6, 3)])

        self.main_board[5][5]: piece = piece(QPushButton(self), 648, 474, row=5, col=5,
                                             lst_neighbors=[(5, 3), (3, 5), (6, 6), (4, 4)])

        # g

        self.main_board[6][0]: piece = piece(QPushButton(self), 32, 528, row=6, col=0,
                                             lst_neighbors=[(3, 0), (5, 1), (6, 3)])

        self.main_board[6][3]: piece = piece(QPushButton(self), 380, 528, row=6, col=3,
                                             lst_neighbors=[(6, 0), (5, 3), (6, 6)])

        self.main_board[6][6]: piece = piece(QPushButton(self), 730, 527, row=6, col=6,
                                             lst_neighbors=[(6, 3), (5, 5), (3, 6)])

    def moving(self):
        # a
        self.main_board[0][0].button.clicked.connect(
            lambda: self.rule.allow_to_move(0, 0) if not self.rule.flag_remove else self.rule.remove_bead(0, 0))

        self.main_board[0][3].button.clicked.connect(
            lambda: self.rule.allow_to_move(0, 3) if not self.rule.flag_remove else self.rule.remove_bead(0, 3))

        self.main_board[0][6].button.clicked.connect(
            lambda: self.rule.allow_to_move(0, 6) if not self.rule.flag_remove else self.rule.remove_bead(0, 6))

        # b
        self.main_board[1][1].button.clicked.connect(
            lambda: self.rule.allow_to_move(1, 1) if not self.rule.flag_remove else self.rule.remove_bead(1, 1))

        self.main_board[1][3].button.clicked.connect(
            lambda: self.rule.allow_to_move(1, 3) if not self.rule.flag_remove else self.rule.remove_bead(1, 3))

        self.main_board[1][5].button.clicked.connect(
            lambda: self.rule.allow_to_move(1, 5) if not self.rule.flag_remove else self.rule.remove_bead(1, 5))

        self.main_board[2][2].button.clicked.connect(
            lambda: self.rule.allow_to_move(2, 2) if not self.rule.flag_remove else self.rule.remove_bead(2, 2))

        self.main_board[2][3].button.clicked.connect(
            lambda: self.rule.allow_to_move(2, 3) if not self.rule.flag_remove else self.rule.remove_bead(2, 3))

        self.main_board[2][4].button.clicked.connect(
            lambda: self.rule.allow_to_move(2, 4) if not self.rule.flag_remove else self.rule.remove_bead(2, 4))

        self.main_board[3][0].button.clicked.connect(
            lambda: self.rule.allow_to_move(3, 0) if not self.rule.flag_remove else self.rule.remove_bead(3, 0))

        self.main_board[3][1].button.clicked.connect(
            lambda: self.rule.allow_to_move(3, 1) if not self.rule.flag_remove else self.rule.remove_bead(3, 1))

        self.main_board[3][2].button.clicked.connect(
            lambda: self.rule.allow_to_move(3, 2) if not self.rule.flag_remove else self.rule.remove_bead(3, 2))

        self.main_board[3][4].button.clicked.connect(
            lambda: self.rule.allow_to_move(3, 4) if not self.rule.flag_remove else self.rule.remove_bead(3, 4))

        self.main_board[3][5].button.clicked.connect(
            lambda: self.rule.allow_to_move(3, 5) if not self.rule.flag_remove else self.rule.remove_bead(3, 5))

        self.main_board[3][6].button.clicked.connect(
            lambda: self.rule.allow_to_move(3, 6) if not self.rule.flag_remove else self.rule.remove_bead(3, 6))

        self.main_board[4][2].button.clicked.connect(
            lambda: self.rule.allow_to_move(4, 2) if not self.rule.flag_remove else self.rule.remove_bead(4, 2))

        self.main_board[4][3].button.clicked.connect(
            lambda: self.rule.allow_to_move(4, 3) if not self.rule.flag_remove else self.rule.remove_bead(4, 3))

        self.main_board[4][4].button.clicked.connect(
            lambda: self.rule.allow_to_move(4, 4) if not self.rule.flag_remove else self.rule.remove_bead(4, 4))

        self.main_board[5][1].button.clicked.connect(
            lambda: self.rule.allow_to_move(5, 1) if not self.rule.flag_remove else self.rule.remove_bead(5, 1))

        self.main_board[5][3].button.clicked.connect(
            lambda: self.rule.allow_to_move(5, 3) if not self.rule.flag_remove else self.rule.remove_bead(5, 3))

        self.main_board[5][5].button.clicked.connect(
            lambda: self.rule.allow_to_move(5, 5) if not self.rule.flag_remove else self.rule.remove_bead(5, 5))

        self.main_board[6][0].button.clicked.connect(
            lambda: self.rule.allow_to_move(6, 0) if not self.rule.flag_remove else self.rule.remove_bead(6, 0))

        self.main_board[6][3].button.clicked.connect(
            lambda: self.rule.allow_to_move(6, 3) if not self.rule.flag_remove else self.rule.remove_bead(6, 3))

        self.main_board[6][6].button.clicked.connect(
            lambda: self.rule.allow_to_move(6, 6) if not self.rule.flag_remove else self.rule.remove_bead(6, 6))


    # def mouseMoveEvent(self, event):
    #     print(f"x mouse: {event.x()} and y mouse: {event.y()}")


if __name__ == '__main__':
    App = QApplication(sys.argv)  # create pyqt5 app
    window = board()  # create the instance of our Window
    sys.exit(App.exec())
