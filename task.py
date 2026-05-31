def conv_num(num_str):
    if type(num_str) != str or num_str == "":
        return None

    negative = False

    if num_str[0] == "-":
        negative = True
        num_str = num_str[1:]

    if num_str == "":
        return None

    # hexadecimal
    if len(num_str) >= 3 and num_str[0:2].lower() == "0x":
        hex_part = num_str[2:]

        if hex_part == "" or "." in hex_part:
            return None

        value = 0

        for ch in hex_part:
            if "0" <= ch <= "9":
                digit = ord(ch) - ord("0")
            elif "a" <= ch.lower() <= "f":
                digit = ord(ch.lower()) - ord("a") + 10
            else:
                return None

            value = value * 16 + digit

        if negative:
            value = -value

        return value

    # decimal / float
    dot_count = 0
    for ch in num_str:
        if ch == ".":
            dot_count += 1
        elif not ("0" <= ch <= "9"):
            return None

    if dot_count > 1:
        return None

    # only "." is invalid
    if num_str == ".":
        return None

    if dot_count == 0:
        value = 0

        for ch in num_str:
            value = value * 10 + (ord(ch) - ord("0"))

        if negative:
            value = -value

        return value

    # float
    parts = num_str.split(".")
    left = parts[0]
    right = parts[1]

    value = 0

    for ch in left:
        value = value * 10 + (ord(ch) - ord("0"))

    decimal_place = 10
    for ch in right:
        value += (ord(ch) - ord("0")) / decimal_place
        decimal_place *= 10

    if negative:
        value = -value

    return value

def my_datetime(num_sec):
    pass

def conv_endian(num, endian='big'):
    pass
