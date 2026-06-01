def conv_num(num_str):
    pass


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
