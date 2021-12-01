with open('calendar_text.txt','r') as f:
    inputs = f.readlines()
inputs = ''.join(inputs)
lines = inputs.split('\n\n')
with open('calendar_lunar_day_name.txt','w') as f:
    for line in lines:
        num, *name = line.split('.')
        name = '.'.join(name).strip().split()[0].replace(':','')
        f.writelines(name+' '+num+'\n')

with open('calendar_lunar_day_info.txt','w') as f:
    for line in lines:
        num, *line = line.split('.')
        line = '.'.join(line).strip().split()
        name = line[0]
        if '):' in ' '.join(line):
            info = ' '.join(line).strip().split('):')[1]
        else:
            info = ' '.join(line).strip().split(':')[1]

        f.write(num+' '+info+'\n')

