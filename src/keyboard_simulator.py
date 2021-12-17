NULL_CHAR = chr(0)

KEY_CODES = {
    0x04:['a', 'A'],
    0x05:['b', 'B'],
    0x06:['c', 'C'],
    0x07:['d', 'D'],
    0x08:['e', 'E'],
    0x09:['f', 'F'],
    0x0A:['g', 'G'],
    0x0B:['h', 'H'],
    0x0C:['i', 'I'],
    0x0D:['j', 'J'],
    0x0E:['k', 'K'],
    0x0F:['l', 'L'],
    0x10:['m', 'M'],
    0x11:['n', 'N'],
    0x12:['o', 'O'],
    0x13:['p', 'P'],
    0x14:['q', 'Q'],
    0x15:['r', 'R'],
    0x16:['s', 'S'],
    0x17:['t', 'T'],
    0x18:['u', 'U'],
    0x19:['v', 'V'],
    0x1A:['w', 'W'],
    0x1B:['x', 'X'],
    0x1C:['y', 'Y'],
    0x1D:['z', 'Z'],
    0x1E:['1', '!'],
    0x1F:['2', '@'],
    0x20:['3', '#'],
    0x21:['4', '$'],
    0x22:['5', '%'],
    0x23:['6', '^'],
    0x24:['7', '&'],
    0x25:['8', '*'],
    0x26:['9', '('],
    0x27:['0', ')'],
    0x28:['\n','\n'],
    0x2a:['\ndelete\n','\ndelete\n'],
    0x2b:['\ntab\n','\ntab\n'],
    0x2C:[' ', ' '],
    0x2D:['-', '_'],
    0x2E:['=', '+'],
    0x2F:['[', '{'],
    0x30:[']', '}'],
    0x32:['#','~'],
    0x33:[';', ':'],
    0x34:['\'', '"'],
    0x36:[',', '<'],
    0x38:['/', '?'],
    0x37:['.', '>'],
    0x2b:['\t','\t'],
    0x4b:['\nPageUp\n','\nPageUp\n'],
    0x4c:['\nFwdDelete\n', '\nFwdDelete\n'],
    0x4d:['\nEnd\n','\nEnd\n'],
    0x4e:['\nPageDown\n','\nPageDown\n'],
    0x4f:[u'→',u'→'],
    0x50:[u'←',u'←'],
    0x51:[u'↓',u'↓'],
    0x52:[u'↑',u'↑']
}

def get_keycode(val, my_dict=KEY_CODES):
    for key, value in my_dict.items():
        if val == value[0]:
            return (key, False)
        if val == value[1]:
            return (key, True)

def str_to_usb_hid_list(input_str: str):
    hid_list = []
    for char in input_str:
        keycode = get_keycode(char)
        if keycode[1]:
            hid_list.append(chr(32)+NULL_CHAR+chr(keycode[0])+NULL_CHAR*5)
        else:
            hid_list.append(NULL_CHAR*2+chr(keycode[0])+NULL_CHAR*5)
        hid_list.append(NULL_CHAR*8)
    
    print(hid_list)
    return hid_list

def hid_code_to_kb(report):
    try:
        with open('/dev/hidg0', 'rb+') as fd:
            fd.write(report.encode())
    except BlockingIOError:
        print("Cannot write to device. Make sure the device is connected via the USB-C port.")
        exit()

def keyboard_to_device(input_str):
    hid_list = str_to_usb_hid_list(input_str=input_str)
    for char in hid_list:
        hid_code_to_kb(char)
        print(char)

if __name__ == '__main__':
    keyboard_to_device("pwd\n")



