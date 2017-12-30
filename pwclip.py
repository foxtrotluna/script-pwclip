import pyperclip
import random
chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
symbols = '[]{};:|?><.,`~!@£$%^&*()_+-=§±¡€#¢∞§¶•ªº–≠⁄™‹›ﬁ‡°·‚—±'
pw = ''
donesymbol = False
for i in range(0,random.randrange(10,15)):
    pos = random.randrange(0,len(chars))
    issymbol = (i == random.randrange(0,10) or (i > 9 and not donesymbol))
    totake = chars
    if issymbol:
        totake = symbols
    pw += totake[pos]
print('password copied to clipboard!')
pyperclip.copy(pw)
test = pyperclip.paste()
