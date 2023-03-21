uwu = [1,2,6,10,2,1,6,1,2,8,10,2,1,8,12]
bigger_uwu = {
}

for i in range(len(uwu)):
    bigger_uwu[uwu[i]] = 0
    
for i in range(len(uwu)):
    bigger_uwu[uwu[i]] = bigger_uwu[uwu[i]]+1

for key, value in bigger_uwu.items():
    if 1 == value:
        print(key)