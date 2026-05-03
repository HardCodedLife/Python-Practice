def exercise65(size: int):
    total = (size-1)*2 +1
    for i in range(size*2-1):
        if i > 3:
            i = 6 - i
        center = "*"*(2*i + 1)
        side = " "*(total - len(center) // 2)
        row = side + center + side
        print(row)
if __name__ == "__main__":
    exercise65(4)
