with open('../files/mbox-short.txt', encoding='UTF-8') as txt:
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
