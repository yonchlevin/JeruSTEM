# pong2.py
# המשחק המלא: כדור קופץ, סטיק שנשלט בכפתור, ניקוד ומסך סיום.
#
# מה חדש לעומת pong1.py:
#   - הקיר הימני הוחלף בסטיק, ולכן בודקים חפיפה בשני צירים
#   - score עולה בכל פגיעה
#   - playing מחליף את True בתנאי הלולאה, ולכן למשחק יש סוף
#
# המשימה המסכמת:
#   1. הריצו וודאו שאתם צוברים ניקוד ושאפשר להפסיד.
#   2. שנו את PADDLE_H ל-24. שימו לב כמה מקומות בקוד מושפעים — ולמה קבוע חוסך את זה.
#   3. הגדילו את מהירות הכדור בכל פגיעה, כך שהמשחק נעשה קשה יותר.
#   4. הוסיפו צפצוף בפגיעה ובהפסד (אם יש זמזם בערכה).
#   5. בונוס: מדדו את קצב הפריימים והשוו למספר מ-fps.py.

from hw import display, pressed

BALL = 4
PADDLE_X = 120
PADDLE_W = 4
PADDLE_H = 16
PADDLE_SPEED = 2

MAX_BALL_Y = 64 - BALL
MAX_PADDLE_Y = 64 - PADDLE_H


def draw_paddle(y):
    """מציירת את הסטיק בגובה הנתון. אותה פונקציה, כל פריים."""
    display.fill_rect(PADDLE_X, y, PADDLE_W, PADDLE_H, 1)


ball_x = 60
ball_y = 30
dx = 2
dy = 1

paddle_y = 24
score = 0
playing = True

while playing:
    # --- הסטיק: הכפתור קובע כיוון, לא פעולה ---
    if pressed():
        paddle_y = paddle_y + PADDLE_SPEED
    else:
        paddle_y = paddle_y - PADDLE_SPEED

    if paddle_y < 0:
        paddle_y = 0
    if paddle_y > MAX_PADDLE_Y:
        paddle_y = MAX_PADDLE_Y

    # --- הכדור: מקדמים ---
    ball_x = ball_x + dx
    ball_y = ball_y + dy

    # --- קירות: שמאל, למעלה ולמטה ---
    if ball_x <= 0:
        ball_x = 0
        dx = -dx

    if ball_y <= 0:
        ball_y = 0
        dy = -dy
    elif ball_y >= MAX_BALL_Y:
        ball_y = MAX_BALL_Y
        dy = -dy

    # --- הסטיק: התנגשות דורשת חפיפה בשני הצירים ---
    hit_x = ball_x + BALL >= PADDLE_X
    hit_y = ball_y + BALL >= paddle_y and ball_y <= paddle_y + PADDLE_H

    if hit_x and hit_y:
        ball_x = PADDLE_X - BALL
        dx = -dx
        score = score + 1

    # --- פספוס ---
    if ball_x > 127:
        playing = False

    # --- מציירים את הפריים כולו ---
    display.fill(0)
    draw_paddle(paddle_y)
    display.fill_rect(ball_x, ball_y, BALL, BALL, 1)
    display.text(str(score), 0, 0, 1)
    display.show()

# --- מחוץ ללולאה: רץ פעם אחת, אחרי שהמשחק נגמר ---
display.fill(0)
display.text('GAME OVER', 24, 24, 1)
display.text(str(score), 60, 40, 1)
display.show()
