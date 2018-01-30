#!/usr/bin/env python3

import curses

__author__ = "Hendrik Werner"

board_width = 50
board_height = 30
score_width = 21


def draw_loop(board):
    curses.curs_set(0)
    board.resize(board_height, board_width)
    board.border()
    score = curses.newwin(board_height, score_width, 0, board_width + 1)
    score.border()
    board.refresh()
    score.refresh()
    key = None
    while key != 'q':
        key = board.getkey()

if __name__ == '__main__':
    curses.wrapper(draw_loop)
