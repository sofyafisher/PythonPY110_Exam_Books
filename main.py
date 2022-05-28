from book_gen import book_gen, to_json_file


if __name__ == "__main__":
    n = book_gen(2)
    to_json_file(n)