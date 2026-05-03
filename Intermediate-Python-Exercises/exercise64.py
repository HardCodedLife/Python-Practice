def exercise64(height: int):
    for i in range(height):
        # row = " "*(height*2-1)
        row = "".join(" " if k!=(height-1)-i and k!=(height-1)+i else "*" for k in range(height*2-1))
        # row[(height-1)-i] = "*"
        # row[(height-1)+i] = "*"
        if i == height-1:
            row = "*"*(height*2-1)
        print(row)
if __name__ == "__main__":
    exercise64(5)
