import serial


def __arduino_wr(ser: serial.Serial, mode='r', random_str='') -> str:

    ser.reset_input_buffer()

    mode_ind = '=' if mode == 'r' else '?'
    payload = mode_ind + random_str + '\n'
    card_uid = ''
    card_data = ''
    # print(payload)
    while True:
        s = ser.readline()
        s = s.strip()
        output = s.decode("utf-8")
        # print(output)

        if 'Card UID' in output:
            card_uid = output.split('UID: ')[1].replace(' ', '')
        if 'Card Data' in output:
            card_data = output.split('Data:  ')[1].replace(' ', '')
        if (len(card_uid) + len(card_data) > len(card_uid)):
            return (card_uid, card_data)
        if(output == "Arduino is ready" and mode == 'w'):
            ans = payload
            ans = ans.encode("utf-8")
            ser.write(ans)
        # return (card_uid, card_data)


def arduino_wr(mode='r', random_str='', ser_path='/dev/ttyUSB0') -> str:
    ser = serial.Serial(ser_path, 9600, timeout=1)
    print('Reading card, do not lift...' if mode ==
          'r' else 'Writing {} to card...'.format(random_str))
    if mode == 'r':
        data = __arduino_wr(ser=ser, mode='r')
        print('Done reading, lift')
        return data
    elif mode == 'w':
        print('First write, do not lift...')
        __arduino_wr(ser=ser, mode='w', random_str=random_str)
        print('First write done, lift.\nSecond write, do not lift...')
        return __arduino_wr(ser=ser, mode='w', random_str=random_str)


if __name__ == '__main__':
    print(arduino_wr(mode='r'))
