# meteors.py
# מגן המטאורים — המשחק המלא.
#
# ששת השלבים של כל פריים:
#   1. קוראים את הכפתור ומזיזים את החללית
#   2. מחשבים gap ויוצרים מטאור אם הגיע הזמן
#   3. מקדמים את כל המטאורים
#   4. בודקים כל אחד: נחסם, פוספס, או ממשיך
#   5. מוחקים, מציירים הכול, מציגים
#   6. מטפלים בזמזם ובודקים אם נגמרו החיים
#
# המשימה המסכמת:
#   1. שחקו סבב מלא.
#   2. כוונו את הקושי: שנו את START_GAP ואת MIN_GAP עד שהמשחק מרגיש הוגן.
#   3. הוסיפו מטאור זהב נדיר ששווה 5 נקודות (רמז: שדה points במילון).
#   4. הציגו את השיא של הסבב הקודם במסך הסיום.
#   5. בונוס: מדדו את קצב הפריימים עם עשרה מטאורים על המסך.

from random import randint

from hw import display, pressed, buzzer
from sprites import (draw_ship, draw_meteor, draw_lives,
                     SHIP_X, SHIP_H, MAX_SHIP_Y,
                     METEOR, MAX_METEOR_Y)

SHIP_SPEED = 2
START_GAP = 40          # פריימים בין מטאורים בתחילת המשחק
MIN_GAP = 10            # הרצפה: לא נרד מתחת לזה גם בניקוד גבוה
BEEP_FRAMES = 3         # אורך הצפצוף, בפריימים

ship_y = 24
meteors = []
since = 0
score = 0
lives = 3
beep_left = 0
playing = True


def spawn():
    """מטאור חדש בגובה ובמהירות אקראיים."""
    rock = {
        'x': 0,
        'y': randint(0, MAX_METEOR_Y),
        'speed': randint(1, 3),
    }
    meteors.append(rock)


while playing:
    # --- 1. החללית: הכפתור קובע כיוון ---
    if pressed():
        ship_y = ship_y + SHIP_SPEED
    else:
        ship_y = ship_y - SHIP_SPEED

    if ship_y < 0:
        ship_y = 0
    if ship_y > MAX_SHIP_Y:
        ship_y = MAX_SHIP_Y

    # --- 2. יצירת מטאורים, בצפיפות שעולה עם הניקוד ---
    gap = START_GAP - score
    if gap < MIN_GAP:
        gap = MIN_GAP

    since = since + 1
    if since >= gap:
        spawn()
        since = 0

    # --- 3. מקדמים את כולם ---
    for m in meteors:
        m['x'] = m['x'] + m['speed']

    # --- 4. נחסם / פוספס / ממשיך ---
    alive = []
    for m in meteors:
        hit_x = m['x'] + METEOR >= SHIP_X
        hit_y = m['y'] + METEOR >= ship_y and m['y'] <= ship_y + SHIP_H

        if hit_x and hit_y:
            score = score + 1
            buzzer.on()
            beep_left = BEEP_FRAMES
        elif m['x'] > 127:
            lives = lives - 1
        else:
            alive.append(m)

    meteors = alive

    # --- 5. מציירים את הפריים ---
    display.fill(0)
    draw_ship(ship_y)
    for m in meteors:
        draw_meteor(m['x'], m['y'])
    display.text(str(score), 0, 0, 1)
    draw_lives(lives)
    display.show()

    # --- 6. זמזם וסיום ---
    if beep_left > 0:
        beep_left = beep_left - 1
    else:
        buzzer.off()

    if lives <= 0:
        playing = False

# --- מחוץ ללולאה: רץ פעם אחת ---
buzzer.off()
display.fill(0)
display.text('GAME OVER', 24, 20, 1)
display.text('SCORE', 24, 36, 1)
display.text(str(score), 80, 36, 1)
display.show()
