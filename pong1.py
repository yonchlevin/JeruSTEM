# pong1.py
# פונג שלב ראשון: כדור שקופץ מארבעת הקירות.
#
# כל הקפיצה היא היפוך סימן:  dx = -dx
#
# שימו לב שההצמדה של המיקום (clamp) באה יחד עם היפוך הכיוון.
# בלעדיה הכדור יכול לחרוג מעבר לגבול, התנאי יתקיים בכל פריים,
# הסימן יתהפך שוב ושוב — והכדור ירעד בקיר במקום לקפוץ ממנו.
#
# המשימה המסכמת:
#   1. הריצו וודאו שהכדור קופץ מכל ארבעת הקירות.
#   2. נסו DX ו-DY שווים, ואז שונים. מה ההבדל במסלול?
#   3. הוסיפו את הסטיק מ-paddle.py — שניהם באותה לולאה, באותו פריים.
#   4. הוסיפו את מונה הפריימים מ-fps.py ובדקו כמה ירד הקצב.
#   5. בונוס: צפצוף קצר בכל קפיצה. שימו לב לכבות את הזמזם אחר כך.

from hw import display

BALL = 4
MAX_X = 128 - BALL           # 124
MAX_Y = 64 - BALL            # 60

ball_x = 60
ball_y = 30
dx = 2
dy = 1

while True:
    ball_x = ball_x + dx
    ball_y = ball_y + dy

    if ball_x <= 0:
        ball_x = 0
        dx = -dx
    elif ball_x >= MAX_X:
        ball_x = MAX_X
        dx = -dx

    if ball_y <= 0:
        ball_y = 0
        dy = -dy
    elif ball_y >= MAX_Y:
        ball_y = MAX_Y
        dy = -dy

    display.fill(0)
    display.fill_rect(ball_x, ball_y, BALL, BALL, 1)
    display.show()
