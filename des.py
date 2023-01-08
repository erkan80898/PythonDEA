INITIAL_PERM = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]

FINAL_PERM = [40, 8, 48, 16, 56, 24, 64, 32,
              39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30,
              37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28,
              35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26,
              33, 1, 41, 9, 49, 17, 57, 25]

EXP_PERM = [32, 1, 2, 3, 4, 5, 4, 5,
            6, 7, 8, 9, 8, 9, 10, 11,
            12, 13, 12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21, 20, 21,
            22, 23, 24, 25, 24, 25, 26, 27,
            28, 29, 28, 29, 30, 31, 32, 1]

FUNC_PERM = [16, 7, 20, 21,
             29, 12, 28, 17,
             1, 15, 23, 26,
             5, 18, 31, 10,
             2, 8, 24, 14,
             32, 27, 3, 9,
             19, 13, 30, 6,
             22, 11, 4, 25]

PARITY_DROP = [57, 49, 41, 33, 25, 17, 9, 1,
               58, 50, 42, 34, 26, 18, 10, 2,
               59, 51, 43, 35, 27, 19, 11, 3,
               60, 52, 44, 36, 63, 55, 47, 39,
               31, 23, 15, 7, 62, 54, 46, 38,
               30, 22, 14, 6, 61, 53, 45, 37,
               29, 21, 13, 5, 28, 20, 12, 4]

KEY_PREM = [14, 17, 11, 24, 1, 5, 3, 28,
            15, 6, 21, 10, 23, 19, 12, 4,
            26, 8, 16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55, 30, 40,
            51, 45, 33, 48, 44, 49, 39, 56,
            34, 53, 46, 42, 50, 36, 29, 32]

SBOX = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

test = 0xA51FF2A7C67BA384


def print_b(val, bits):
    bits = str(bits + 2)
    print(format(val, '#0' + bits + 'b'))


def print_keys(keys):
    for key in keys:
        print_b(key, 48)

def print_keys_hex(keys):
    for key in keys:
        print(hex(key))

def set_bit(bits, bit_size, pos, on):
    pos = bit_size - (pos - 1)
    if on:
        return bits | (1 << (pos - 1))
    else:
        return bits & ~(1 << (pos - 1))


def get_bit(bits, bit_size, pos):
    pos = bit_size - (pos - 1)
    return (bits >> pos) & 1


def prem(block, block_size, table):
    result = 0
    count = 1

    for idx in table:
        if get_bit(block, block_size,  idx):
            result = set_bit(result, block_size, count, True)
        else:
            result = set_bit(result, block_size, count, False)
        count += 1
    return result


def partition(block, block_size):
    if block_size == 56:
        mask = 0xFFFFFFF
    else:
        result = []
        mask = 0x3F
        for i in range(block_size/6):
            result.append(block & mask)
            block >>= 6
        return result

    return block >> (block_size // 2), block & mask


def expansion(block):
    result = 0
    count = 1
    for idx in EXP_PERM:
        if get_bit(block, idx):
            result = set_bit(result, count, True)
        else:
            result = set_bit(result, count, False)
        count += 1
    return result


def apply_f(block, block_size, key):
    block = prem(block, block_size, EXP_PERM)
    block ^= key
    #partition into eight 6 bits for sbox application
    sbox_input = partition(block, 48)
    sbox_output = apply_sbox(sbox_input)



def apply_sbox(blocks):
    result = []
    mask_MSB = 0b100000
    mask_LSB = 1
    mask_inner = 0b011110
    count = 0
    for block in blocks:
        row = ((block & mask_MSB) >> 4 | (block & mask_LSB))
        col = (block & mask_inner) >> 1
        result.append(SBOX[count][row][col])
        count += 1
    return result


def bit_rotation(block, block_size, shift_count, mode):
    if mode:
        return ((block << shift_count) | block >> (block_size - shift_count)) % 2 ** block_size
    else:
        return ((block >> shift_count) | block << (block_size - shift_count)) % 2 ** block_size


# mode = True -> Enc
def key_scheduler(key, mode, round, subkeys):
    if round == 17:
        return

    if round == 1:
        key = prem(key, 64, PARITY_DROP)

    if not mode and round == 1:
        subkey_n = prem(key, 56, KEY_PREM)
        subkeys.append(subkey_n)
        return key_scheduler(key, mode, round + 1, subkeys)

    shift_count = 1
    if round not in [1, 2, 9, 16]:
        shift_count = 2

    (left, right) = partition(key, 56)
    left = bit_rotation(left, 28, shift_count, mode)
    right = bit_rotation(right, 28, shift_count, mode)
    key_block = (left << 28) | right
    subkey_n = prem(key_block, 56, KEY_PREM)
    subkeys.append(subkey_n)

    return key_scheduler(key_block, mode, round + 1, subkeys)

def des(block, block_size, )

def driver(key):
    key = 0xAABB09182736CCDD
    plaintext = 0x123456ABCD132536
    cipher = 0xC0B7A8D05F3A829C

    #ENCRYPTION
    subkeys = []
    key_scheduler(key, True, 1, subkeys)

    plaintext = prem(plaintext, 64, INITIAL_PERM)








