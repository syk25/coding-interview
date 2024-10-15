for character in input():
    if 0 <= ord(character) - ord("a") <= 25:
        print(chr((ord(character) - ord("a")) + ord("A")), end="")
    elif 0 <= ord(character) - ord("A") <= 25:
        print(chr((ord(character) - ord("A")) + ord("a")), end="")
