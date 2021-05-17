try:
    with open("article1.txt", "r", encoding="UTF-8") as read_first:
        with open("article2.txt", "r", encoding="UTF-8") as read_second:
            for lines in read_first:
                print(lines.rsplit("\n"))
                for lines2 in read_second:
                    print(lines2.rsplit("\n"))
except EOFError:
    print("")
