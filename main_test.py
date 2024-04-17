import random

new_s = ''
li = ['привет я', 'кейн, омега', 'idol', 'sigma', 'я конечно не волк, но тоже могу драться', 'всем привет', 'покакал наконец-то ура', 'Официальное название: смерть от голода.', 'Но сможем ли мы продолжить издеваться над симами или, наоборот, защищать их от неожиданной кончины старыми методами? Все же смерть в Симс 4 заметно отличается от предыдущих частей игры.']

stack = set()

for _ in range(random.randint(0, len(li) // 2 - 1)):
    print('____________________________________')
    ran = random.randint(0, len(li)-1)
    while len(li[ran].split(' ')) <= 2:
        ran = random.randint(0, len(li)-1)
    temp = list(map(str, li[ran].split(' ')))
    ran1 = 0
    temp_s = ''
    while ran1 <= 1:
        ran1 = random.randint(0, len(temp) - 1)
    for i in range(0, len(temp)-1):
        temp_s += temp[i]
        temp_s += ' '
    new_s += temp_s
print(new_s)


#  дальше ты, саша