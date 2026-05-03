def exercise61(rows: int):
    last = [1]
    for i in range(rows):
        current = []
        for j in range(i+1):
            if j == 0 or j == i:
                current.append(1)
            else:
                current.append(last[j-1] + last[j])
        print(current)
        last = current
if __name__ == "__main__":
    exercise61(5)
