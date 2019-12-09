import terminal
import module_system


def main(console, colors, module):
    console.addstr(1, 1, module["name"])
    console.addstr(2, 1, module["version"])
    console.addstr(3, 1, module["description"])
    console.addstr(4, 1, module["author"])
    console.getstr(15, 0)


if __name__ == "__main__":
    console = terminal.initialize_console(80, 60)
    colors = terminal.initialize_colors(console)
    module = module_system.initialize_module()
    main(console, colors, module)
    terminal.close_console()

