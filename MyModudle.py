import random

def getFibonacci(x):
    if x <= 1:
        return 1
    else:
         return getFibonacci(x - 2) + getFibonacci(x - 1)



def getDigits_Number(x):
    if x < 10:
        return 1

    else:
        return 1 + getDigits_Number(x // 10)

        
def getRandom_Number():
    key = int(input())
    random.seed(key)
    data = [0] * 6
    i = 0
    while i < 6 :
        x = random.randint(1,43)
        flag = True
        j = 0 
        while j < i and flag:
            if data[j] == x:
                flag = False
            j +=1
        if flag: 
            data[i] = x 
            i += 1
    for y in data:
        print(y ,end="\t")
    print()
