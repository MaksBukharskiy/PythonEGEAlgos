def solutionOf_synonym():
    input = sys.stdin.read().split()

    if not input:
        return 0

    pairOf_syn = {}

    index = 1
    first = int(input[0])

    for i in range(first):
        word1 = input[first]
        word2 = input[first+1]

        pairOf_syn[word1] = word2
        pairOf_syn[word2] = word1

        first+=2


    ans = pairOf_syn[input[-1]]

    print(ans)



