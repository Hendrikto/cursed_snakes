#!/usr/bin/env python3

import curses

from model.border_window import BorderWindow
from model.snake import Snake

__author__ = "Hendrik Werner"

board_width = 50
board_height = 30
score_width = 21


def draw_loop(stdscr):
    curses.curs_set(0)
    board = BorderWindow(board_width, board_height, stdscr, "Game Board")
    score = BorderWindow(
        score_width,
        board_height,
        begin_x=board_width + 3,
        title="Score",
    )
    snake = Snake(0, 0)
    key = None
    while key != 'q':
        key = board.window.getkey()
        snake.update_direction(key)
        snake.update_head()
        snake.draw(board.window)
        snake.update_tail()
        score.window.addstr(0, 0, f"Snake 1: {snake.length}")
        board.window.refresh()
        score.window.refresh()


if __name__ == '__main__':
    curses.wrapper(draw_loop)
