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

    value = 0.0

    for ch in left:
        value = value * 10 + (ord(ch) - ord("0"))

    decimal_place = 10

    for ch in right:
        value += (ord(ch) - ord("0")) / decimal_place
        decimal_place *= 10

    return value


def get_sign(num_str):
    if num_str[0] == "-":
        return True, num_str[1:]

    if num_str[0] == "+":
        return False, num_str[1:]

    return False, num_str


def is_valid_decimal(num_str):
    if num_str == ".":
        return False

    if num_str.count(".") > 1:
        return False

    for ch in num_str:
        if ch != "." and not ("0" <= ch <= "9"):
            return False

    return True


def convert_decimal(num_str):
    if "." in num_str:
        return float_to_decimal(num_str)

    return int_to_decimal(num_str)


def conv_num(num_str):
    if not isinstance(num_str, str) or num_str == "":
        return None

    negative, num_str = get_sign(num_str)

    if num_str == "":
        return None

    if len(num_str) >= 2 and num_str[:2].lower() == "0x":
        hex_part = num_str[2:]

        if hex_part == "" or "." in hex_part:
            return None

        value = hex_to_decimal(hex_part)
    else:
        if not is_valid_decimal(num_str):
            return None

        value = convert_decimal(num_str)

    if value is None:
        return None

    if negative:
        return -value

    return value


# A year is a leap year if it is divisable by 4, and is not a century year or is also divisble by 400
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def my_datetime(num_sec):
    # Number of full days
    days = num_sec // 86400

    year = 1970
    # Get year
    while True:
        days_in_year = 366 if is_leap_year(year) else 365
        if days < days_in_year:
            break
        days -= days_in_year
        year += 1

    month_days = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31]
    month = 0
    # Find month
    while days >= month_days[month]:
        days -= month_days[month]
        month += 1

    return '{:02d}-{:02d}-{}'.format(month + 1, days + 1, year)


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
