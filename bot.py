from random import choice

from algorithms_movement import algorithms
from copy import deepcopy


class Bot(algorithms):
    def __init__(self, main_board, bot_color='blue'):
        super().__init__(main_board)
        self.bot_color = bot_color

    def get_copy_state(self):
        p1_bead = deepcopy(self.player1.number_bead)
        p1_alive = deepcopy(self.player1.alive_bead)

        p2_bead = deepcopy(self.player2.number_bead)
        p2_alive = deepcopy(self.player2.alive_bead)

        copy_lst_scores = deepcopy(self.lst_scores_now)
        copy_flag_remove = deepcopy(self.flag_remove)
        copy_board = self.get_copy_main_board()
        return p1_bead, p1_alive, p2_bead, p2_alive, copy_lst_scores, copy_flag_remove, copy_board

    def do_copy_to_state(self, **kwargs):
        self.player1.number_bead = kwargs['p1_bead']

        self.player1.alive_bead = kwargs['p1_alive']

        self.player2.number_bead = kwargs['p2_bead']
        self.player2.alive_bead = kwargs['p2_alive']

        self.lst_scores_now = kwargs['copy_lst_scores']
        self.flag_remove = kwargs['copy_flag_remove']
        self.set_copy_main_board(kwargs['copy_board'])

    def bot_insert(self):

        random_insert = self.random('white')
        button = self.main_board[random_insert[0]][random_insert[1]]

        if self.player2.number_bead <= 11:
            p1_bead, p1_alive, p2_bead, p2_alive, copy_lst_scores, copy_flag_remove, copy_board = \
                self.get_copy_state()

            self.close_window = False
            p = self.minimax(5, False)
            self.close_window = True
            if p[1]:
                # print("PPPP:", p)
                x = p[1][0]
                y = p[1][1]
            else:
                x, y = random_insert[0], random_insert[1]

            self.do_copy_to_state(p1_bead=p1_bead, p1_alive=p1_alive, p2_bead=p2_bead, p2_alive=p2_alive,
                                  copy_lst_scores=copy_lst_scores, copy_flag_remove=copy_flag_remove,
                                  copy_board=copy_board)

            button = self.main_board[x][y]

        self.player2.turn = 1
        self.player1.turn = 0

        self.insert(button, 1)
        self.switch_turn()

    def bot_choice_start_bead_to_move(self):
        # random_start_bead_to_move = self.random(self.bot_color)
        # self.lst_neighbors = self.get_all_white_piece_for_min_bead('white')
        # if not self.lst_neighbors:
        #     self.lst_neighbors = self.check_neighbors(random_start_bead_to_move[0], random_start_bead_to_move[1])
        # while True:
        #     if self.lst_neighbors:
        #         break
        #     random_start_bead_to_move = self.random(self.bot_color)
        #     self.lst_neighbors = self.check_neighbors(random_start_bead_to_move[0], random_start_bead_to_move[1])
        #
        # button = self.main_board[random_start_bead_to_move[0]][random_start_bead_to_move[1]]
        # return self.choice_start_bead_to_move(button, 1)
        #####################################################################
        p1_bead, p1_alive, p2_bead, p2_alive, copy_lst_scores, copy_flag_remove, copy_board = \
            self.get_copy_state()

        lst_neighbors = self.get_all_white_piece_for_min_bead('white')

        if lst_neighbors:
            lst_blue = self.get_all_color_piece('blue')
            x, y = choice(lst_blue)

        else:
            self.close_window = False
            s = self.minimax_move(4, True)
            self.close_window = True

            # print("ssssssss:", s)
            x = s[1][0]
            y = s[1][1]

        self.do_copy_to_state(p1_bead=p1_bead, p1_alive=p1_alive, p2_bead=p2_bead, p2_alive=p2_alive,
                              copy_lst_scores=copy_lst_scores, copy_flag_remove=copy_flag_remove,
                              copy_board=copy_board)

        # if self.main_board[x][y].color == 'red':
        #     random_start_bead_to_move = self.random(self.bot_color)
        #     self.lst_neighbors = self.get_all_white_piece_for_min_bead('white')
        #     if not self.lst_neighbors:
        #         self.lst_neighbors = self.check_neighbors(random_start_bead_to_move[0], random_start_bead_to_move[1])
        #     while True:
        #         if self.lst_neighbors:
        #             break
        #         random_start_bead_to_move = self.random(self.bot_color)
        #         self.lst_neighbors = self.check_neighbors(random_start_bead_to_move[0], random_start_bead_to_move[1])

        self.best_movement_start_choice = (x, y)
        button = self.main_board[x][y]

        self.player2.turn = 1
        self.player1.turn = 0

        self.player_win = None
        self.total_score_moving = 0

        return self.choice_start_bead_to_move(button, 1)

    def bot_choice_end_bead_to_move(self):
        lst_white_all = self.get_all_white_piece_for_min_bead('white')
        if lst_white_all:
            player = self.player2
            pos = self.finding_end_pos_for_min_bead()

            if pos is None:
                pos = choice(lst_white_all)

            button_pos = self.main_board[pos[0]][pos[1]]
            if button_pos.color == 'red':
                pos = choice(lst_white_all)

        else:
            player, score, pos = self.eval_minimax_end(self.best_movement_start_choice)

        if player:
            button = self.main_board[pos[0]][pos[1]]
            # print('button from:', pos)

        else:
            random_end_bead_to_move = self.random(None, self.lst_neighbors)
            button = self.main_board[random_end_bead_to_move[0]][random_end_bead_to_move[1]]
            # print('button from random:', random_end_bead_to_move)

        if self.choice_end_bead_to_move(button, 1):
            if not self.flag_remove:
                self.switch_turn()

    def bot_remove_bead(self):

        copy_board_red = self.get_copy_main_board()
        copy_flag_remove = deepcopy(self.flag_remove)

        self.close_window = False
        r = self.minimax_move(4, False)
        self.close_window = True

        self.set_copy_main_board(copy_board_red)
        self.flag_remove = copy_flag_remove

        print("rrrrrrrrrr:", r)
        x = r[1][0]
        y = r[1][1]

        self.player2.turn = 1
        self.player1.turn = 0

        # btn = self.main_board[x][y]
        # if btn.color == 'blue':
        #     random_remove_piece = self.random('red')
        #     x, y = random_remove_piece[0], random_remove_piece[1]
        #     print('position remove:', random_remove_piece)

        return self.remove_bead(x, y)

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
