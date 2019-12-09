import curses


def initialize_console(width, height):
    console = curses.initscr()
    y, x = console.getmaxyx()
    if y < height or x < width:
        curses.endwin()
        print("Too small console size.")
        print("Need: %dx%d" % (width, height))
        print("Your: %dx%d" % (x, y))
        exit(1)
        return None

    # Console size is correct
    curses.echo()
    curses.raw()
    curses.curs_set(1)
    console.refresh()
    return console


def initialize_colors(console):
    if not curses.has_colors():
        curses.endwin()
        print("Your console can't display colors!")
        exit(1)
    curses.start_color()
    colors = {}
    colors["Error"] = 1
    curses.init_pair(colors["Error"], curses.COLOR_RED, curses.COLOR_BLACK)
    return colors

def close_console(message="Bye-bye" ,exit_code = 0):
    curses.endwin()
    print(message)
    exit(exit_code)

