import os
import platform
from subprocess import call
from controller import main_controller


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Darwin":
        os.system("clear")
    else:
        print(
            "This program cannot clear the screen in your operating system. It only works with Windows and Linux"
        )


def print_menu(title, options):
    print(f"{title}\n")
    for i in range(len(options) - 1):
        print(f"({str(i+1)}) {options[i+1]}")
    print(f"\n(0) {options[0]}\n")


def print_message(message):
    print(message + " ")


def print_general_results(result, label):
    print(label, ":\n", result)


def print_table(table):
    nrCols = len(table[0])
    lengths = []
    for i in range(nrCols):
        lengths.append(len(table[0][i]))

    for row in table[1:]:
        for i in range(nrCols):
            lenValue = len(row[i])
            if lengths[i] < lenValue:
                lengths[i] = lenValue
    sumLengths = 0
    for i in range(nrCols):
        sumLengths += lengths[i]

    strLine = "-" * (sumLengths + (3 * nrCols) - 1)

    print(f"/{strLine}\\")

    for row in table:
        print("|", end="")

        for i in range(nrCols):
            lenValue = len(row[i])
            strFill = " " * int(((lengths[i] - lenValue) / 2))
            strExtra = " " * int((len(strFill) * 2 + lenValue) < lengths[i])

            print(f"{strExtra} {strFill}{row[i]}{strFill} |", end="")

        if row != table[-1]:
            print(f"\n|{strLine}|")
        else:
            print("")

    print(f"\\{strLine}/")


def get_input(label):
    return input(f"{label}: ")


def get_inputs(labels):
    inputs = []

    for i in labels:
        x = input(i + ": ")
        inputs.append(x)

    return inputs


def print_error_message(message):
    print(message)
