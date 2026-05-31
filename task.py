def conv_num(num_str):
    pass

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
