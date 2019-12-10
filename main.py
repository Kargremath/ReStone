import terminal
import module_system


def main(colors, module):
    input_console, log_console, map_console, stat_console = terminal.draw_base_ui(module)
    log_console.addstr(2, 2, module["event"]["inForest"]["description"])
    log_console.refresh()
    command = terminal.get_player_command(input_console)


if __name__ == "__main__":
    console = terminal.initialize_console(80, 60)
    colors = terminal.initialize_colors(console)
    module = module_system.initialize_modules()
    main(colors, module)
    terminal.close_console()

