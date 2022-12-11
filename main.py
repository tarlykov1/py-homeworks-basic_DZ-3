import os

path = './text/'

d = {}
for i in range(1, 3):
    name = f'{path}{i}.txt'
    with open(name, 'r', encoding='utf-8') as f:
        d[name] = [x for x in f.read().splitlines() if x]

with open('final_file.txt', 'w', encoding='utf-8') as file:
    for k, v in sorted(d.items(), key=lambda x: len([x[-1]])):
        file.write(k + '\n')
        file.write('Количество строк: ' +str(len(v)) + '\n')
        file.write('\n'.join(v))
        file.write('\n')
print('Выполнено')