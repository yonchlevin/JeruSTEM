# meteors.py
# ההרחבה: אותו משחק בדיוק, אבל במקום כדור אחד — זרם מטאורים.
#
# מה חדש לעומת pong.py:
#   - רשימה במקום שני משתנים, וכל מטאור הוא מילון עם x, y ו-speed
#   - randint, כדי שכל מטאור ייכנס בגובה ובמהירות אחרים
#   - שלושה חיים, ולכן פספוס אחד לא מסיים
#   - הקושי עולה: ככל שהניקוד גדל, המטאורים מגיעים צפופים יותר
#
# ההתנגשות עצמה זהה לזו של pong.py, מילה במילה — רק בתוך לולאה.
#
# כלי הדיבוג של הקובץ הזה: בטלו את ההערה מהשורה שמדפיסה len(meteors).
# אם המספר רק עולה — הרשימה לא מתנקה, והמשחק יזחל תוך דקה.

from random import randint

from hw import display, pressed
from sprites import (draw_ship, draw_rock, draw_lives,
                     SHIP_X, SHIP_H, MAX_SHIP_Y, BALL)

SHIP_SPEED = 2
MAX_METEOR_Y = 64 - BALL      # 59
START_GAP = 40                # פריימים בין מטאורים בתחילת המשחק
MIN_GAP = 10                  # רצפה: לא נרד מתחת לזה גם בניקוד גבוה

ship_y = 24
meteors = []
since = 0
score = 0
lives = 3
playing = True


def spawn():
    """מטאור חדש בגובה ובמהירות אקראיים, ומוסיף אותו לרשימה."""
    rock = {
        'x': 0,
        'y': randint(0, MAX_METEOR_Y),
        'speed': randint(1, 3),
    }
    meteors.append(rock)


while playing:
    # --- החללית ---
    if pressed():
        ship_y = ship_y + SHIP_SPEED
    else:
        ship_y = ship_y - SHIP_SPEED

    if ship_y < 0:
        ship_y = 0
    if ship_y > MAX_SHIP_Y:
        ship_y = MAX_SHIP_Y

    # --- יצירה תקופתית, בצפיפות שעולה עם הניקוד ---
    gap = START_GAP - score
    if gap < MIN_GAP:
        gap = MIN_GAP

    since = since + 1
    if since >= gap:
        spawn()
        since = 0

    # --- מקדמים את כולם ---
    for m in meteors:
        m['x'] = m['x'] + m['speed']

    # --- נחסם / פוספס / ממשיך ---
    # בונים רשימה חדשה. אסור להוציא מרשימה שעוברים עליה.
    alive = []
    for m in meteors:
        hit_x = m['x'] + BALL >= SHIP_X
        hit_y = m['y'] + BALL >= ship_y and m['y'] <= ship_y + SHIP_H

        if hit_x and hit_y:
            score = score + 1
        elif m['x'] > 127:
            lives = lives - 1
        else:
            alive.append(m)

    meteors = alive

    # print('meteors:', len(meteors))

    # --- מציירים את הפריים כולו ---
    display.fill(0)
    draw_ship(ship_y)
    for m in meteors:
        draw_rock(m['x'], m['y'])
    display.text(str(score), 0, 0, 1)
    draw_lives(lives)
    display.show()

    if lives <= 0:
        playing = False

# --- מחוץ ללולאה ---
display.fill(0)
display.text('GAME OVER', 24, 20, 1)
display.text('SCORE', 24, 36, 1)
display.text(str(score), 80, 36, 1)
display.show()
