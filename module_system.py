import json
import sys
import terminal


def initialize_module():
    if len(sys.argv) == 1:
        terminal.close_console("Invalid params: No module", 1)

    #argv != 1
    if len(sys.argv) != 2:
        terminal.close_console("Invalid params: Too much params", 1)

    module = sys.argv[1]
    try:
        with open(module + "\\main.json", 'r') as json_file:
            module = json.load(json_file)
    except FileNotFoundError:
        terminal.close_console("Module doesn't exists", 1)

    # module now is json dict
    return module

