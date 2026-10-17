def Longest_Substring_Without_Repeating_Characters(str1: str, str2: str) -> bool:
    
    if len(str1) != len(str2):
        return False

    return sorted(str1) == sorted(str2)