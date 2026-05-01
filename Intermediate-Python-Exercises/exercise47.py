import re

def exercise47(text: str)-> tuple[str, ...]:
    expression = r'[^\s]+@[^\s\d]+\.[^\s\d]+'
    return re.findall(expression, text)
if __name__ == "__main__":
   print(exercise47("Contact us at support@company.com or sales.dept@office.org for help.")) 
