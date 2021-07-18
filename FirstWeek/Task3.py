def packet_handler(buffsize: int, n_packts: int, packs: list):
    _buff = []
    _sys_time = 0
    _pckt_counter = 0
    _pck_time = 0
    _bad_packets = 0
    ans_for_test = []
    while _pckt_counter < n_packts:
        while len(_buff) < buffsize and _pckt_counter < n_packts:
            if packs[_pckt_counter][0] >= _sys_time:
                _buff.append(packs[_pckt_counter])
            else:
                _bad_packets += 1
            _pckt_counter += 1
        if _buff and _sys_time <= _buff[0][0]: _sys_time = _buff[0][0]
        if _buff:
            #print(_sys_time)
            ans_for_test.append(_sys_time)
            _sys_time += _buff[0][1]
            _buff.pop(0)
        while _bad_packets:
            #print(-1)
            ans_for_test.append(-1)
            _bad_packets -= 1
    while _buff:
        #print(_sys_time)
        ans_for_test.append(_sys_time)
        _sys_time += _buff[0][1]
        _buff.pop(0)
    return ans_for_test

def test():
    buffsize_and_npacks = [[2, 8], [2, 8], [1, 5], [3, 6], [2, 6], [2, 5], [3, 8],
                           [5, 10]]
    packets = [
            [[0, 0], [0, 0], [0, 0], [1, 1], [1, 0], [1, 0], [1, 2],[1, 3]],
            [[0, 0], [0, 0], [0, 0], [1, 0], [1, 0], [1, 1], [1, 2], [1, 3]],
            [[999999, 1], [1000000, 0], [1000000, 1], [1000000, 0], [1000000, 0]],
            [[0, 7], [0, 0], [2, 0], [3, 3], [4, 0], [5, 0]],
            [[0, 2], [0, 0], [2, 0], [3, 0], [4, 0], [5, 0]],
            [[2, 9], [4, 8], [10, 9], [15, 2], [19, 1]],
            [[1,1], [2,2], [3,3], [4,4], [5,5], [6,6], [7,7], [8,8]],
            [[2, 4], [9, 21], [125, 16], [126, 19], [126, 29], [126, 55], [141, 90], [141, 0], [999, 150], [999, 0]],

               ]
    corrects = [
        [0, 0, 0, 1, 2, -1, -1, -1],
        [0, 0, 0, 1, 1, 1, 2, -1],
        [999999, 1000000, 1000000, -1, -1],
        [0, 7, 7, -1, -1, -1],
        [0, 2, 2, 3, 4, 5],
        [2, 11, -1, 19, 21],
        [1, 2, 4, 7, 11, -1, 16, -1],
        [2, 9, 125, 141, 160, 189, 244, 334, 999, 1149]

            ]
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
