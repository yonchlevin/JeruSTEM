# fps.py
# אותה תנועה כמו ב-motion.py, אבל עם מונה פריימים שמדפיס ל-Shell כל שנייה.
#
# הניסוי:
#   1. הריצו וכתבו את המספר שקיבלתם.
#   2. בטלו את ההערה מהלולאה שמוסיפה חמישה מלבנים, והריצו שוב.
#   3. ההפרש בין שני המספרים הוא כל השיעור.
#
# הערה: ticks_diff הוא הדרך הנכונה להחסיר שני זמנים. חיסור רגיל
# נראה עובד, אבל נשבר כשהמונה הפנימי גולש.

from time import ticks_ms, ticks_diff

from hw import display

SPEED = 2

x = 0
frames = 0
t0 = ticks_ms()

while True:
    display.fill(0)
    display.hline(x, 32, 20, 1)

    # --- שלב 2 של הניסוי: הסירו את סימני ההערה מהשורות הבאות ---
    # for i in range(5):
    #     display.rect(i * 10, 4, 8, 8, 1)

    display.show()

    x = x + SPEED
    if x > 127:
        x = 0

    frames = frames + 1
    if ticks_diff(ticks_ms(), t0) >= 1000:
        print('FPS:', frames)
        frames = 0
        t0 = ticks_ms()
