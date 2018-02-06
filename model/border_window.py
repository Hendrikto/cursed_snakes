import curses

__author__ = "Hendrik Werner"


class BorderWindow():
    def __init__(
        self,
        width,
        height,
        outer_window=None,
        title=None,
        begin_y=0,
        begin_x=0,
    ):
        if outer_window is None:
            outer_window = curses.newwin(
                height + 2, width + 2, begin_y, begin_x
            )
        else:
            outer_window.resize(height + 2, width + 2)
        self.border = outer_window
        self.window = outer_window.derwin(height, width, 1, 1)
        self.title = title
        self.draw_border()
        self.border.refresh()

    def draw_border(self):
        self.border.border()
        if not self.title:
            return
        title_string = f"╴{self.title}╶"
        self.border.addstr(
            0,
            (self.border.getmaxyx()[1] - len(title_string)) // 2,
            title_string,
        )
