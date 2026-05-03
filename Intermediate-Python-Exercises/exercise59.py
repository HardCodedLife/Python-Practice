import re
def exercise59():
    while (user_command:=input("To-Do List App:$ ").strip()).lower() != "q" and user_command.lower() != "quit":
        if user_command == "view":
            with open("to-do","r") as file:
                print(file.read())
        elif user_command == "clear":
            with open("to-do","w") as file:
                file.write("--- My To-Do List ---\n")
        elif (user_commands:=user_command.split(":"))[0] == "Add Task":
            with open("to-do","r") as file:
                lines = len(file.readlines())
            with open("to-do","a") as file:
                file.write(f"{lines}. {re.search(r'"(.*)"',user_commands[1]).group(1)}\n")
        else:
            print("Not supported command!")
    print("Bye!")
if __name__ == "__main__":
    from pathlib import Path
    file = Path("to-do")
    file.write_text("--- My To-Do List ---\n")
    exercise59()
    file.unlink()
