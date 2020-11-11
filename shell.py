from subprocess import check_output
import os.path

HELP = """
>>> availible commands: hello.py, hello.py + name, Hexdump.py, Hexdump.py + filename, cd, show me a surprise.
>>> you can type: 'hello help'/'hexdump help' for more information about these commands.
>>> enter "exit" to close the shell.
>>> by using the "|" symbol, the command after the "|" gets the output of the command before the "|".
>>> by using the ">" symbol, the output of the command before the ">" goes into the file after the ">".
>>> by using the "<" symbol, the input of the command after the "<" will be the file's text before the "<".
>>> by typing "cd" you can change the directory of the program.
>>> by typing "set" you will see the variables of the program. you can change it by typing 'set var new_answer'.
>>> author: Omer Oz
"""
HELLO_HELP = "prints hello with the author name' unless you type a name after the command 'hello.py'"
HEXDUMP_HELP = "prints the hex data of a pre set photo.\n" \
               "you can change the photo by typing the file name after the command 'Hexdump.py'"

set_dictionary = {
    "teacher": "Nir Dweck",
    "USERNAME": "omer",
    "pyversion": "3.7",
    "mygrade": "100",
    "myage": "17",
    "path": "C:\\Users\\omero\\PycharmProjects\\pythonProject4;C:\\Windows\\System32"
}


def path_handle(command):
    """
    handles the path and adds the directory to the command
    :param command: the input given
    :return: the full path of the command
    """
    path = set_dictionary["path"].split(";")
    for p in path:
        cmd = p + "\\" + command
        if os.path.isfile(cmd):
            return 0
    return 1


def cd_handle(command):
    """
    handles the cd command.
    by typing "cd" you can change the directory of the program.
    :param command: input given.
    :return: the old directory and the new directory.
    """
    list_cmd = command.split(" ")
    print("\u0332".join("directory changed from:") + "  " + os.getcwd(), end="")
    os.chdir(list_cmd[1])
    print("  " + "\u0332".join("to:") + "  " + os.getcwd())


def set_handle(command):
    """
    handles the set command.
    by typing "set" you will see the variables of the program. you can change it by typing 'set var new_answer'.
    :param command: input given.
    :return: the set dictionary or one of its args.
    """
    list_cmd = command.split(" ")
    if len(list_cmd) == 1:
        return set_dictionary
    elif len(list_cmd) == 2:
        return list_cmd[1] + " = " + set_dictionary.get(list_cmd[1])
    else:
        set_dictionary[list_cmd[1]] = list_cmd[2]
        return list_cmd[1] + " = " + list_cmd[2]


def output_cmd_handle(command):
    """
    handles the '>' command.
    by using the ">" symbol, the output of the command before the ">" goes into the file after the ">".
    :param command: input given.
    :return: a message that the output was transferred successfully.
    """
    list_cmd = command.split(" > ")
    func = list_cmd[0]
    file = list_cmd[1]
    if " " in func:
        output = check_output(["python", func.split(" ")[0], func.split(" ")[1]]).decode()
    else:
        output = check_output(["python", func]).decode()
    f = open(file.rstrip().lstrip(), "w")
    f.write(output)
    return "message transferred successfully.\nthe message is: " + output + "."


def input_cmd_handle(command):
    """
    handles the '<' command.
    by using the "<" symbol, the input of the command after the "<" will be the file's text before the "<".
    :param command: input given.
    :return: the output of the command.
    """
    list_cmd = command.split(" < ")
    file = list_cmd[0]
    func = list_cmd[1]
    t1 = open(file, "r", encoding='utf-8')
    text = ""
    for row in t1:
        text += row
    return check_output(["python", func, text]).decode()


def pipe_handle(command):
    """
    handles the '|' command.
    by using the "|" symbol, the command after the "|" gets the output of the command before the "|".
    :param command: input given.
    :return: the output of the command after the '|'.
    """
    command = command.lstrip().rstrip()
    list_cmd = command.split(" | ")
    first = list_cmd[0]
    if " " in first:
        output = check_output(["python", first.split(" ")[0], first.split(" ")[1]]).decode()
    else:
        output = check_output(["python", first]).decode()
    return check_output(["python", list_cmd[1], output]).decode()


def command_input(command):
    """
    handles the input after the command in cases which the input is more than 1 word.
    :param command: the input given.
    :return: the full input after the command.
    """
    lst = command.split(" ")
    length = len(lst)
    counter = 1
    cmd_input = ""
    while length > 1:
        cmd_input += lst[counter]
        cmd_input += " "
        counter += 1
        length -= 1
    return cmd_input


def main():
    pinput = ''
    while pinput != "exit":  # the shell runs until the input 'exit' is given.
        print("[shell] >> ", end="")
        pinput = input()
        pinput = pinput.lstrip().rstrip()
        if '>' in pinput:
            print(output_cmd_handle(pinput))
        elif '<' in pinput:
            print(input_cmd_handle(pinput))
        elif '|' in pinput:
            print(pipe_handle(pinput))
        elif 'cd' in pinput:
            cd_handle(pinput)
        elif 'set' in pinput:
            print(set_handle(pinput))
        elif pinput == "help":
            print(HELP)
        elif pinput == "hexdump help":
            print(HEXDUMP_HELP)
        elif pinput == "hello help":
            print(HELLO_HELP)
        elif pinput == "show me a surprise":
            print(check_output(["python", "surprise.py"]).decode())
        else:
            if pinput == "exit":
                break
            lst = pinput.split(" ")
            cmd_input = command_input(pinput)
            if path_handle(lst[0]) == 0:
                if len(lst) > 1:
                    if ".py" in lst[0]:
                        print(check_output(["python", lst[0], cmd_input]).decode())
                    else:
                        print(check_output([lst[0], cmd_input]).decode())
                else:
                    if ".py" in lst[0]:
                        print(check_output(["python", lst[0]]).decode())
                    else:
                        print(check_output([lst[0]]).decode())
            elif path_handle(pinput) == 1:
                print("error. command not found")


if __name__ == "__main__":
    main()
