from w2_Task1 import *
n_proc, n_task = [int(i) for i in input().split()]
task_time = [int(i) for i in input().split()]
proc_time = [[0, i] for i in range(n_proc)]


minbuildheapdown(proc_time)
anss = []
for i in range(n_task):
    anss.append([proc_time[0][1], proc_time[0][0]])
    proc_time[0][0] += task_time.pop(0)
    minsiftdown(0, proc_time)
for i in anss:
    print(i[0], i[1], sep=' ')
