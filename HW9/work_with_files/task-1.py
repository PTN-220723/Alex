def open_file(a, b):
    with open(a, b, encoding='UTF-8') as f:
        return f
adr = '../files/mbox-short.txt'
mode = 'r'
txt = open_file(adr, mode)
print(txt)
# with open('../files/mbox-short.txt', encoding='UTF-8') as txt:
txt:
    for line in txt:
        if 'From stephen' in line and line.split()[-3] == '5':
            print(line)
cnt = 0
with open('../files/mbox-short.txt', encoding='UTF-8') as txt:
    for line in txt:
        if line.startswith('From '):
            cnt += 1
            print(line.strip())
            print(f'Количество входящих писем: {cnt}')
