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


def draw_base_ui(module):
    log_console = curses.newwin(55, 60, 0, 0)
    log_console.box('|', '-')
    log_console.addstr(0, 1, module["name"])
    log_console.refresh()

    input_console = curses.newwin(5, 60, 55, 0)
    input_console.box('|', '-')
    input_console.addstr(0, 1, "Commands")
    input_console.addstr(2, 2, '>')
    input_console.refresh()
        
    map_console = curses.newwin(11, 20, 0, 60)
    map_console.box('|', '-')
    map_console.addstr(0, 1, "Map")
    map_console.refresh()

    stat_console = curses.newwin(49, 20, 11, 60)
    stat_console.box('|', '-')
    stat_console.addstr(0, 1, "Stat")
    stat_console.refresh()
    return input_console, log_console, map_console, stat_console


def get_player_command(input_console):
    input_console.move(2, 3)
    input_console.clrtoeol()
    input_console.addstr(2, 59, '|')
    command = input_console.getstr(2, 4)
    return command

