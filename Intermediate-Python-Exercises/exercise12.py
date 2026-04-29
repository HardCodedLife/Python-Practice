def exercise12(lib: dict[str,list[str]]) -> dict[str,str]:
    return {book:author for author in lib for book in lib[author]}
if __name__ == "__main__":
    print(exercise12({"Orwell": ["1984", "Animal Farm"], "Huxley": ["Brave New World"]}))
