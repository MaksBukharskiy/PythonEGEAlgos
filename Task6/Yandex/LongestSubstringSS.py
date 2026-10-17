def Longest_Substring_Without_Repeating_Characters(string1: str, string2: str) -> bool:

    if (len(string1) != len(string2)):
        return False

    alf = [0] * 26

    for i in range(len(string1)):

        alf[ord([string1]) - ord('a')] += 1
        alf[ord([string2]) - ord('a')] -= 1



    for x in count:
        if x!=0:
            return False

    return True