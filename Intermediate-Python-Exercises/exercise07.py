def exercise7(sentence: str) -> bool:
    sentence = ''.join(c.lower() for c in sentence if c.isalnum())
    return sentence == sentence[::-1]

if __name__ == "__main__":
   print(exercise7("A man, a plan, a canal: Panama")) 
