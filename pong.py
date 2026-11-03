# pong.py
# נקודת הנחיתה הראשונה: משחק שלם.
# כדור שקופץ משלושה קירות, חללית שאתם מזיזים, ניקוד על כל חבטה, ופספוס שמסיים.
#
# ארבעת שלבי הפריים נמצאים כאן בדיוק כמו ב-motion.py:
#   מוחקים, מציירים, מציגים, מקדמים — רק עם יותר דברים באמצע.
#
# התרגיל:
#   1. שחקו סבב. צברו ניקוד, הפסידו.
#   2. כוונו את הקושי: שנו את dx, את dy ואת SHIP_H עד שזה מרגיש הוגן.
#   3. הגדילו את מהירות הכדור בכל חבטה.
#   4. בונוס: שלושה חיים במקום סיום מיידי (draw_lives כבר מחכה ב-sprites.py).

from hw import display, pressed
from sprites import (draw_ship, draw_rock,
                     SHIP_X, SHIP_H, MAX_SHIP_Y, BALL)

SHIP_SPEED = 2
MAX_BALL_Y = 64 - BALL        # 59

ship_y = 24
ball_x = 60
ball_y = 30
dx = 2
dy = 1
score = 0
playing = True

while playing:
    # --- החללית: הכפתור קובע כיוון, לא פעולה ---
    if pressed():
        ship_y = ship_y + SHIP_SPEED      # לחוץ: יורדת, כי Y גדל כלפי מטה
    else:
        ship_y = ship_y - SHIP_SPEED      # משוחרר: עולה

    if ship_y < 0:
        ship_y = 0
    if ship_y > MAX_SHIP_Y:
        ship_y = MAX_SHIP_Y

    # --- הכדור: מקדמים ---
    ball_x = ball_x + dx
    ball_y = ball_y + dy

    # --- קירות: שמאל, למעלה ולמטה ---
    # מצמידים את המיקום לפני היפוך הסימן, אחרת הכדור רועד בקיר
    if ball_x <= 0:
        ball_x = 0
        dx = -dx

    if ball_y <= 0:
        ball_y = 0
        dy = -dy
    elif ball_y >= MAX_BALL_Y:
        ball_y = MAX_BALL_Y
        dy = -dy

    # --- החללית: התנגשות דורשת חפיפה בשני הצירים ---
    hit_x = ball_x + BALL >= SHIP_X
    hit_y = ball_y + BALL >= ship_y and ball_y <= ship_y + SHIP_H

    if hit_x and hit_y:
        ball_x = SHIP_X - BALL
        dx = -dx
        score = score + 1

    # --- פספוס ---
    if ball_x > 127:
        playing = False

    # --- מציירים את הפריים כולו ---
    display.fill(0)
    draw_ship(ship_y)
    draw_rock(ball_x, ball_y)
    display.text(str(score), 0, 0, 1)
    display.show()

# --- מחוץ ללולאה: רץ פעם אחת, אחרי שהמשחק נגמר ---
display.fill(0)
display.text('GAME OVER', 24, 20, 1)
display.text('SCORE', 24, 36, 1)
display.text(str(score), 80, 36, 1)
display.show()
