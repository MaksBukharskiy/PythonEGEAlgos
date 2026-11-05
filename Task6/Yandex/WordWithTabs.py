def solution():
    all_text = sys.stdin.read()
    words_splited = all_text.split()

    print(len(set(words_splited)))

    