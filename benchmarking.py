import time
from main import calculating, setting_variables


anfangszeit = time.time()
a = []
i = 0
durchläufe = 0
sek_20 = time.time()

while durchläufe < 15:
    if sek_20 <= time.time():
        sek_20 = time.time() + 30
        setting_variables()
        durchläufe += 1
        a.append(i)
        i = 0
    calculating()

    i += 1
a.pop(0)
print("Durschnittliche Itteration: ", sum(a)/len(a))
print(a)
