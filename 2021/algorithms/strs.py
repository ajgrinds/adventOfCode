def get_sec_word(string):
    """Get the second word of a string. Useful for problems that contain DIRECTION DISTANCE or something
    :return int if isdigit()
    """
    ans = string.split(" ")[1]
    if ans.isdigit():
        ans = int(ans)
    return ans


def l_str(arr, seperator=''):
    """Converts a list to a string. Useful for an array of numbers"""
    return seperator.join(map(str, arr))


def l_int(arr, base=2):
    """Converts a list of strings to a number. Default base is 2, can be specified differently.
    If there is a letter in it, it defaults to 16"""
    if not all(type(x) == int or x.isdigit() for x in arr) and base == 2:
        base = 16
    string = "".join(map(str, arr))
    return int(string, base)
