from itertools import *

k = 0
for i in product("моль", repeat = 5):
    s = ''.join(i)
    news = s.replace("м", "л")

    if news.count("ь") == news.count("ль"):
        k+=1

print(k)