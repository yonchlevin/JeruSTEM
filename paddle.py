# paddle.py
# הכפתור מזיז את הסטיק: לחוץ — יורד, משוחרר — עולה.
#
# שימו לב להצמדה לגבולות (clamping) בשורות שאחרי התנועה.
# נסו למחוק אותן ולראות מה קורה: הסטיק יוצא מהמסך ולא חוזר, בלי שום שגיאה.
#
# שימו לב גם שההצמדה באה אחרי שינוי המיקום ולא לפניו.

from hw import display, pressed

PADDLE_X = 120
PADDLE_W = 4
PADDLE_H = 16
SPEED = 2

MAX_Y = 64 - PADDLE_H        # 48

paddle_y = 24

while True:
    if pressed():
        paddle_y = paddle_y + SPEED      # לחוץ: יורד, כי Y גדל כלפי מטה
    else:
        paddle_y = paddle_y - SPEED      # משוחרר: עולה

    if paddle_y < 0:
        paddle_y = 0
    if paddle_y > MAX_Y:
        paddle_y = MAX_Y

    display.fill(0)
    display.fill_rect(PADDLE_X, paddle_y, PADDLE_W, PADDLE_H, 1)
    display.show()
