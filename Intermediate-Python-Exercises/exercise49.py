import os
def exercise49(dir_name: str) -> None:
    for dirpath, dirnames, filenames in os.walk(dir_name):
        for f in filenames:
            name, extension = os.path.splitext(f)
            if extension.lower() == '.py':
                print(f'{dirpath}/{dirnames}/{f}')
if __name__ == "__main__":
    print(exercise49('./'))
