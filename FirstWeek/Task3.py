# ОБРАБОТЧИК СЕТЕВЫХ ПАКЕТОВ
# packets[n] = [arrival_time, operation_time]
# buff_size, n_packets = [int(i) for i in input().split()]
# packets = [[0, 0], [0, 0], [0, 0], [1, 1], [1, 0], [1, 0], [1, 2], [1, 3]]
# packets = [[1, 100], [1, 100], [1, 100], [1, 0]]
packets = [[999999, 1],[1000000, 0],[1000000,1],[1000000, 0],[1000000, 0]]
n_packets = 5
buff_size = 1
buff = []
sys_time = 0
'''for i in range(n_packets):
    packets.append([int(i) for i in input().split()])'''
#print(packets)
# заполняем буффер пакетами до упора
pckt_counter = 0
pck_time = 0
"""for i in range(n_packets):
    packets.append([int(i) for i in input().split()])"""
bad_packets = 0
while pckt_counter < n_packets:
    while len(buff) < buff_size and pckt_counter < n_packets:
        if packets[pckt_counter][0] >= sys_time:
            buff.append(packets[pckt_counter])
            pckt_counter += 1
        else:
            bad_packets += 1
            pckt_counter += 1
    if buff and sys_time <= buff[0][0]: sys_time = buff[0][0]
    if buff:
        print(sys_time)
        sys_time += buff[0][1]
        buff.pop(0)
    while bad_packets:
        print(-1)
        bad_packets -= 1




"""buff_size, n_packets = [int(i) for i in input().split()]
packets = []
buff = []
sys_time = 0
for i in range(n_packets):
    packets.append([int(i) for i in input().split()])
pckt_counter = 0
while pckt_counter < n_packets:
    while len(buff) < buff_size:
        if sys_time <= packets[pckt_counter][0]:
            sys_time = packets[pckt_counter][0]
            buff.append(packets[pckt_counter])
        else:
            print(-1)
            break
    if len(buff): a = buff.pop(0)
    if buff_size == 1:
        print(sys_time)
    if len(buff):
        print(sys_time)
        sys_time += a[1]
    pckt_counter += 1"""
