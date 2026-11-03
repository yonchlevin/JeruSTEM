# mission.py
# התוכנית הראשית של המשימה. מריצים את הקובץ הזה, לא את game.py.

from random import randint

import game

MAX_TRIES = 5

secret = randint(1, 100)
tries = 0
won = False

while tries < MAX_TRIES:
    guess = int(input('נחשו מספר בין 1 ל-100: '))
    tries = tries + 1

    result = game.check(guess, secret)
    print(result)

    if result == game.HIT:
        won = True
        break

print('---')
if won:
    print('ניצחתם אחרי', tries, 'ניסיונות')
else:
    print('נגמרו הניסיונות. המספר היה', secret)

for i in range(tries):
    print('ניסיון', i + 1)

# בונוס: אחרי שתשלימו את bar() ב-game.py, בטלו את ההערה מהשורה הבאה
# game.bar(MAX_TRIES - tries + 1)
