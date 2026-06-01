def hex_to_decimal(hex_part):
    value = 0

    for ch in hex_part:
        if "0" <= ch <= "9":
            digit = ord(ch) - ord("0")
        elif "a" <= ch.lower() <= "f":
            digit = ord(ch.lower()) - ord("a") + 10
        else:
            return None

        value = value * 16 + digit

    return value


def int_to_decimal(num_str):
    value = 0

    for ch in num_str:
        value = value * 10 + (ord(ch) - ord("0"))

    return value


def float_to_decimal(num_str):
    left, right = num_str.split(".")

    value = 0

    for ch in left:
        value = value * 10 + (ord(ch) - ord("0"))

    decimal_place = 10

    for ch in right:
        value += (ord(ch) - ord("0")) / decimal_place
        decimal_place *= 10

    return value


def conv_num(num_str):
    if not isinstance(num_str, str) or num_str == "":
        return None

    negative = False

    if num_str[0] == "-":
        negative = True
        num_str = num_str[1:]

    if num_str == "":
        return None

    if len(num_str) >= 2 and num_str[:2].lower() == "0x":
        hex_part = num_str[2:]

        if hex_part == "" or "." in hex_part:
            return None

        value = hex_to_decimal(hex_part)

        if value is None:
            return None

    else:
        dot_count = num_str.count(".")

        if dot_count > 1:
            return None

        for ch in num_str:
            if ch != "." and not ("0" <= ch <= "9"):
                return None

        if num_str == ".":
            return None

        if dot_count == 0:
            value = int_to_decimal(num_str)
        else:
            value = float_to_decimal(num_str)

    if negative:
        value = -value

    return value


def my_datetime(num_sec):
    pass


def conv_endian(num, endian='big'):
    if endian != 'big' and endian != 'little':
        return None

    is_negative = num < 0
    num = abs(num)

    if num == 0:
        return '00'

    # Convert number to hex string
    hex_chars = '0123456789ABCDEF'
    hex_str = ''
    while num > 0:
        hex_str = hex_chars[num % 16] + hex_str
        num = num // 16

    # Padding to even
    if len(hex_str) % 2 != 0:
        hex_str = '0' + hex_str

    # Split into bytes
    bytes_list = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)]

    if endian == 'little':
        bytes_list.reverse()

    result = ' '.join(bytes_list)

    if is_negative:
        result = '-' + result

    return result
