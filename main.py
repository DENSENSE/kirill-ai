for number in range(338472, 338495):
    dell = set()
    for d in range(1, (number**(1/2)) + 1):
        if number % d == 0:
            dell.add(d)

            dell.add(number % d)
    if len(dell) == 6:
        print(number, max(dell), max(dell, 1))
    