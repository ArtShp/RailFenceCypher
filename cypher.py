def encode_rail_fence_cipher(string, n):
    res = ""
    count_arr = []
    count_arr.append(0)
    count_arr.append(len(string) // 3)
    count_arr.append(len(string) - (len(string)//3-1))
    '''
    count_arr.append(len(string) // 3)
    count_arr.append(len(string) - (2*(len(string)//3) - 1))
    count_arr.append(len(string)//3 - 1)
    '''

    for i in range(len(string)//4):
        res += string[count_arr[0]]
        count_arr[0] += 1
        res += string[count_arr[1]]
        count_arr[1] += 1
        res += string[count_arr[2]]
        count_arr[2] += 1
        res += string[count_arr[1]]
        count_arr[1] += 1
    res += string[count_arr[0]]
    count_arr[0] += 1

    return res





def decode_rail_fence_cipher(string, n):
    pass
