from book_gen import book_gen

if __name__ == "__main__":
    for key, value in book_gen().items():
        print("{0}: {1}".format(key, value))
    print("----------")