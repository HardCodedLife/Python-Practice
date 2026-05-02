import re
from collections import Counter
def exercise52(text: str) -> dict[str,int]:
    return Counter(re.split(r"[^\w]+", text.lower()))
    # counts = {}
    # for word in (words:=re.split(r"[^\w]+", text)):
    #     counts[case] = counts.get((case:=word.lower()),0) + 1
    # return counts
if __name__ == "__main__":
    print(exercise52("Python is great. Python is fast, and learning Python is fun!"))
