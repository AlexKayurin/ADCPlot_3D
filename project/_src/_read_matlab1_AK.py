import struct
import math
import numpy as np


VAL_TYPE = ['d', 'f', 'i', 'h', 'H', 'B']
VAL_LGTH = [8, 4, 4, 2, 2, 1]


def load_mat(fName):
    with open(fName, 'rb') as f:
        DATA = {}

        file_size = f.seek(0, 2)
        f.seek(0, 0)

        bytes_read = 0
        while bytes_read < file_size:
            '''
            Header = 20 bytes 5 x I
            [0]
            mx type
                1st digit = VAL_TYPE:
                    0: double-precision (64-bit) floating point numbers
                    1: single-precision (32-bit) floating point numbers
                    2: 32-bit signed integers
                    3: 16-bit signed integers
                    4: 16-bit unsigned integers
                    5: 8-bit unsigned integers
                        stored in global lists
                        VAL_TYPE = ['d', 'f', 'i', 'h', 'H', 'B']
                        VAL_LGTH = [8, 4, 4, 2, 2, 1]
                 
                2nd digit = type of mx:
                    0: Numeric
                    1: Text
                    2: Sparse
            [1]
            no of rows
            [2]
            no of columns
            [3]
            Length of mx name (+1 byte)
            '''
            hdr = struct.unpack('<5I', f.read(20))
            bytes_read += 20

            mx_type_id = hdr[0]
            mx_type_b = math.floor(mx_type_id / 10)                 # type id
            mx_type_t = mx_type_id % 10                             # data type

            mx_rows = hdr[1]
            mx_cols = hdr[2]

            mx_name_len = hdr[4]                                    # always +1
            # print(f'\n{hdr}')

            # mx name
            fmt = f'<{mx_name_len}s'
            mx_name = f.read(mx_name_len).decode('utf-8')[:-1]      # [:-1] - last byte is always 0
            bytes_read += mx_name_len
            # print(mx_name)

            # text data
            if mx_type_t == 1:
                '''
                for text type (mx_type == 1) each mx element is represented by 4 bytes float (f) 
                representing ASCII code of character
                '''
                fmt, mx_len_bytes = f'<{mx_cols}f', mx_cols * 4
                bytestring = struct.unpack(fmt, f.read(mx_len_bytes))
                bytes_read += mx_len_bytes

                textstring = []
                for b in bytestring:
                    textstring.append(chr(int(b)))
                mx = ''.join(textstring)
                # print(mx)
                DATA |= {mx_name: mx}

            # numeric data
            if mx_type_t == 0:
                '''
                0: double-precision (64-bit) floating point numbers
                1: single-precision (32-bit) floating point numbers
                2: 32-bit signed integers
                3: 16-bit signed integers
                4: 16-bit unsigned integers
                5: 8-bit unsigned integers
                    stored in global lists
                    VAL_TYPE = ['d', 'f', 'i', 'h', 'H', 'B']
                    VAL_LGTH = [8, 4, 4, 2, 2, 1]
                '''
                mx = np.zeros((mx_cols, mx_rows))

                var_type = VAL_TYPE[mx_type_b]
                var_lgth = VAL_LGTH[mx_type_b]
                fmt = f'<{var_type}'
                for col in range(mx_cols):
                    for row in range(mx_rows):
                        val = struct.unpack(fmt, f.read(var_lgth))
                        bytes_read += var_lgth
                        mx[col, row] = val[0]

                # print(mx_name)
                # print(mx)
                DATA |= {mx_name: mx}

    # print(f'Read: {bytes_read} of {file_size} - OK')
    # for k, v in DATA.items():
    #     print(k)
    return DATA

