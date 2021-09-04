from controller import main_controller
import os
import platform


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Darwin":
        os.system("clear")
    else:
        print(
            "This program cannot clear the screen in your operating system. \n It only works with Windows and Linux"
        )


if __name__ == "__main__":
    main_controller.menu()
