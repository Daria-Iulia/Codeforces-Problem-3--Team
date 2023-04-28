surest = "1 1 1"
stillsure = "1 1 0"
stillsure1 = "0 1 1"
stillsure2 = "1 0 1"
notsosure = "1 0 0"
notsosure1 = "0 1 0"
notsosure2 = "0 0 1"
notsureatall = "0 0 0"

n = int(input())

contor = 0

def verdict(sure):
    if sure == surest:
        return 1
    elif sure == stillsure or sure == stillsure2 or sure == stillsure1:
        return 1
    else:
        return 0
    
for i in range(n):
    sure = str(input(""))
    contor += verdict(sure)

print(contor)
