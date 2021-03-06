from calendar_bot_solution import *

with open('mahina_calendar_day_name.txt','r') as f:
    dmap = dict()
    for line in f:
        name, date = line.strip().split()
        date = int(date)-1
        dmap[date] = name
    print(dmap)
    warm_up()
ans = [
        (dmap[18],'1/1/2021'),
        (dmap[19],'1/2/2021'),
        (dmap[29],'1/12/2021'),
        (dmap[18],'1/31/2021'),
        (dmap[19],'2/1/2021'),
        (dmap[0],'2/11/2021'),
        (dmap[0],'6/9/2021'),
        (dmap[29],'8/6/2021'),
        (dmap[0],'10/5/2021'),
        (dmap[0],'11/3/2021'),
        (dmap[29],'12/2/2021'),
       ]
errors = []
for idx, (expected, date) in enumerate(ans):
    curr = dmap[get_mahina_day_idx(date)]
    print('expected',expected)
    if expected != curr:
        print('*************   '+date +' got '+curr)
        errors.append(date)

print('++++++++++++++')
print(errors)
print('++++++++++++++')
