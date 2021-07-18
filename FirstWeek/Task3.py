buffsize_and_npacks = [[1, 1], [2, 8], [2, 8], [1, 5], [3, 6], [2, 6], [2, 5], [3, 8],
                       [5, 10], [4, 5], [1, 25],[11, 25]]
packets = [
    [[0, 0]],
    [[0, 0], [0, 0], [0, 0], [1, 1], [1, 0], [1, 0], [1, 2], [1, 3]],
    [[0, 0], [0, 0], [0, 0], [1, 0], [1, 0], [1, 1], [1, 2], [1, 3]],
    [[999999, 1], [1000000, 0], [1000000, 1], [1000000, 0], [1000000, 0]],
    [[0, 7], [0, 0], [2, 0], [3, 3], [4, 0], [5, 0]],
    [[0, 2], [0, 0], [2, 0], [3, 0], [4, 0], [5, 0]],
    [[2, 9], [4, 8], [10, 9], [15, 2], [19, 1]],
    [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]],
    [[2, 4], [9, 21], [125, 16], [126, 19], [126, 29], [126, 55], [141, 90], [141, 0], [999, 150], [999, 0]],
    [[0, 7], [2, 7], [4, 7], [6, 7], [21, 7]],
    [
        [16, 0], [29, 3], [44, 6], [58, 0], [72,2], [88, 8], [95, 7], [108, 6], [123, 9], [139, 6], [152, 6], [157, 3],
        [169, 3], [183, 1], [192, 0], [202, 0], [213, 8], [229, 3], [232, 3], [236, 3], [239, 4], [247, 8], [251, 2],
        [267, 7], [275, 7]],
    [
        [6, 23], [15, 44], [24, 28], [25, 15], [33, 7], [47, 41], [58, 25], [65, 5], [70, 14], [79, 8],
        [93, 43], [103, 11], [110, 25], [123, 27], [138, 40], [144, 19], [159, 2], [167, 23],
        [179, 43], [182, 31], [186, 7], [198, 16], [208, 41], [222, 23], [235, 26]
    ]

]
corrects = [
    [0],
    [0, 0, 0, 1, 2, -1, -1, -1],
    [0, 0, 0, 1, 1, 1, 2, -1],
    [999999, 1000000, 1000000, -1, -1],
    [0, 7, 7, -1, -1, -1],
    [0, 2, 2, 3, 4, 5],
    [2, 11, -1, 19, 21],
    [1, 2, 4, 7, 11, -1, 16, -1],
    [2, 9, 125, 141, 160, 189, 244, 334, 999, 1149],
    [0, 7, 14, 21, 28],
    [16, 29, 44, 58, 72, 88, -1, 108, 123, 139, 152, -1, 169, 183, 192, 202, 213, 229, 232, 236, 239, 247, -1, 267, 275 ],
    [6, 29, 73, 101, 116, 123, 164, 189, 194, 208, 216, 259, 270, 295, 322, 362, -1, 381, -1, -1, -1, 404, 420, 461, 484]

]

def packet_handler(buffsize: int, n_packts: int, packs: list):
    _buff = []
    _sys_time = 0
    _pckt_counter = 0
    _pck_time = 0
    _bad_packets = []
    ans_for_test = []
    while _pckt_counter < n_packts:
        while len(_buff) < buffsize and _pckt_counter < n_packts:
            if packs[_pckt_counter][0] >= _sys_time:
                _buff.append(packs[_pckt_counter])
            else:
                _bad_packets.append(packs[_pckt_counter][0])
            _pckt_counter += 1
        if _buff and _sys_time < _buff[0][0]: _sys_time = _buff[0][0]
        if _buff:
            #print(_sys_time)
            if _bad_packets and _bad_packets[0] < _buff[0][0]:
                pass
            else:
                ans_for_test.append(_sys_time)
                _sys_time += _buff[0][1]
                _buff.pop(0)

        while _bad_packets and _buff:
            if _bad_packets[0] < _buff[0][0]:
                #print(-1)
                ans_for_test.append(-1)
                _bad_packets.pop(0)
            else:
                break
    while _buff:
        if _sys_time < _buff[0][0]: _sys_time = _buff[0][0]
        #print(_sys_time)
        while _bad_packets:
            if _bad_packets[0] < _buff[0][0]:
                ans_for_test.append(-1)
                _bad_packets.pop(0)
            else:
                break
        ans_for_test.append(_sys_time)
        _sys_time += _buff[0][1]
        _buff.pop(0)
    while _bad_packets:
        #print(-1)
        ans_for_test.append(-1)
        _bad_packets.pop(0)
    return ans_for_test

def test():
    out_dict = {i: 0 for i in range(len(packets))}
    for i in range(len(packets)):
        out_dict[i] = packet_handler(buffsize_and_npacks[i][0], buffsize_and_npacks[i][1], packets[i])
        if out_dict[i] == corrects[i]:
            print("TEST №{} PASSED".format(i))
        else:
            print("TEST №{} NOT PASSED".format(i))
            print("your answer is: ", out_dict[i])
            print("right answer is", corrects[i])
            print()
test()
#print(buffsize_and_npacks[11],corrects[11])
#print(packet_handler(buffsize_and_npacks[11][0], buffsize_and_npacks[11][1], packets[11]))