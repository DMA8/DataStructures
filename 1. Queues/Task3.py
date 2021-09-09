from tests_task3 import test
from tests_task3 import packets, buffsize_and_npacks, corrects
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
        if _buff:
            if _sys_time < _buff[0][0]:
                _sys_time = _buff[0][0]
            if not _bad_packets or _bad_packets[0] > _buff[0][0]:
                ans_for_test.append(_sys_time)
                _sys_time += _buff[0][1]
                _buff.pop(0)
            while _bad_packets and _buff and _bad_packets[0] < _buff[0][0]:
                    ans_for_test.append(-1)
                    _bad_packets.pop(0)
    while _buff:
        if _sys_time < _buff[0][0]: _sys_time = _buff[0][0]
        while _bad_packets and _buff and _bad_packets[0] < _buff[0][0]:
                ans_for_test.append(-1)
                _bad_packets.pop(0)
        ans_for_test.append(_sys_time)
        _sys_time += _buff[0][1]
        _buff.pop(0)
    while _bad_packets:
        ans_for_test.append(-1)
        _bad_packets.pop(0)
    return ans_for_test
test(packet_handler)
