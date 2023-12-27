def plain(str):
    if len(str) > 1:
        if str[0] == str[len(str) - 1]:
            str = str[1:-1]
            return plain(str)
        else:
            return False

    else:
        return True


print(plain("abcbad"))
