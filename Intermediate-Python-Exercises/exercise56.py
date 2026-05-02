import re
def exercise56(filename: str):
    lines, words, characters= 0, 0, 0
    with open(filename, mode="r", newline='') as file:
        for line in file:
            lines += 1
            words += len(re.findall(r"\w+", line))
            characters += len(line)
    print(f"Lines: {lines} | Words: {words} | Characters: {characters}")
if __name__ == "__main__":
    from pathlib import Path
    sample_file = Path("sample.txt")
    sample_file.write_text(
            """Hello World
Python is fun.
""")
    exercise56(sample_file)
    sample_file.unlink()
