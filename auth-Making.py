#Auth Making
#Making Auth Rubika Account
import random
import os
from colorama import init, Fore
import pyfiglet
import time
init()
os.system('cls')
fire = print(Fore.RED+'\tAuth Making')
hero = random.randint(1, 1000)
hend = print(Fore.BLUE+pyfiglet.figlet_format('A UTHER'))
git, hub, persian = 'https://', 'github.com/', 'Boy-Researcher'
rex = (Fore.GREEN+git + Fore.RESET+hub + Fore.RED+persian)
print(rex)
hex = input(Fore.LIGHTYELLOW_EX+'Enter y / n Or help: ')
css = (fire, hend, git, hub, persian, hex)
hex = hex.upper()
if hex == 'Y':
    list2 = ('qwertyuiopasdfghjklzxcvbnm')
    while True:
        iran0, iran1, iran2, iran3, iran4, iran5, iran6, iran7, iran8, iran9, iran10, iran11, iran12, iran13, iran14, iran15, iran16, iran17, iran18, iran19, iran20, iran21, iran23, iran24, iran25, iran26, iran27, iran28, iran29, iran30, iran31, iran32 = "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2)), "".join(random.choice(list2))
        cyan = iran0+iran1+iran2+iran3+iran4+iran5+iran6+iran7+iran8+iran9+iran10+iran11+iran12+iran13+iran14+iran15+iran16+iran17+iran18+iran19+iran20+iran21+iran23+iran24+iran25+iran26+iran27+iran28+iran29+iran30+iran31+iran32
        f = open(f'Auth_list1{hero}.txt', '+a')
        max = None
        f.write(cyan + '\n')
        time.sleep(0)
        print(Fore.GREEN+'Auth Making...')
        f.close()
elif hex == 'HELP':
    print(Fore.GREEN+'\nEnter y -> Making Auth', Fore.RESET+'Rubika Account', Fore.RED+' Enter n -> Close', Fore.RED+'https://github.com/Boy-Researcher')
elif hex == 'n':
    print('Good By')
