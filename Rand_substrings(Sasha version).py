import random

def massSTR_to_massWORDS(massiv_strok):
    massiv_words = []  
    mass_substr = []
    for i in range(len(massiv_strok)):
        mass_substr = massiv_strok[i].split()
        for j in range(len(mass_substr)):
            massiv_words.append(mass_substr[j])
    return massiv_words

#  я сейчас буду подключить к гиту
def genSTR(massiv_slov):
    length_of_gen = random.randint(1, 8)
    code_of_gen = []
    for i in range(length_of_gen):  
        code_of_gen.append(ra)