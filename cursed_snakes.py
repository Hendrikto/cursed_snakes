#!/usr/bin/env python3

import curses

from model.snake import Snake

__author__ = "Hendrik Werner"

board_width = 50
board_height = 30
score_width = 21


def add_titleborder(window, title):
    window.border()
    title_string = f"╴{title}╶"
    window.addstr(
        0,
        (window.getmaxyx()[1] - len(title_string)) // 2,
        title_string,
    )


def draw_loop(board):
    snake = Snake(1, 1)
    curses.curs_set(0)
    board.resize(board_height, board_width)
    add_titleborder(board, "Game Board")
    score = curses.newwin(board_height, score_width, 0, board_width + 1)
    add_titleborder(score, "Score")
    key = None
    while key != 'q':
        key = board.getkey()
        snake.update_head()
        snake.draw(board)
        snake.update_tail()
        board.refresh()
        score.refresh()

if __name__ == '__main__':
    curses.wrapper(draw_loop)
