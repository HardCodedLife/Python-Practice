def exercise4(word1: str, word2: str) -> bool:
    return sorted(word1) == sorted(word2)

if __name__ == "__main__":
   print(exercise4("listen","silent")) 
