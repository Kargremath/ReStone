import json
import sys
import terminal


def initialize_modules():
    if len(sys.argv) == 1:
        terminal.close_console("Invalid params: No module", 1)

    #argv != 1
    if len(sys.argv) != 2:
        terminal.close_console("Invalid params: Too much params", 1)

    module_name = sys.argv[1]
    main_module = {}
    main_module = load_main_module(main_module, module_name)

    return main_module


def load_main_module(main_module, module_name):
    try:
        with open(module_name + "\\main.json", 'r') as json_file:
            main_module = json.load(json_file)
            if "includes" in main_module:
                for item in main_module["includes"]:
                    main_module = load_module(main_module, item)

    except FileNotFoundError:
        terminal.close_console("Invalid module name", 1)
    return main_module


def load_module(parent_module, path):
    module = {}
    try:
        with open(path, 'r') as json_file:
            module = json.load(json_file)
            if "includes" in module:
                for item in module["includes"]:
                    module = load_module(module, item)
            parent_module[module["name"]] = module
    except FileNotFoundError:
        terminal.close_console("Invalid include in" + parent_module["name"], 1)
    return parent_module
