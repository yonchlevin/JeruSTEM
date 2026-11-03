# rain.py
# תרגיל הרשימות: גשם מטאורים, בלי חללית ובלי ניקוד.
#
# מה לנסות:
#   1. הריצו וראו שלושה מטאורים חוצים את המסך.
#   2. בטלו את ההערה מהשורה שמדפיסה את len(meteors) וראו את המספר עולה ויורד.
#   3. החליפו את הקטע המסומן בגרסה השבורה (למטה) וראו מטאור נתקע בקצה.
#   4. בונוס: ה-spawn התקופתי כבר כאן — שנו את GAP וראו מה קורה לצפיפות.

from random import randint

from hw import display
from sprites import draw_meteor, METEOR, MAX_METEOR_Y

GAP = 30            # פריימים בין מטאור למטאור

meteors = []
since = 0


def spawn():
    """יוצר מטאור חדש בגובה ובמהירות אקראיים, ומוסיף אותו לרשימה."""
    rock = {
        'x': 0,
        'y': randint(0, MAX_METEOR_Y),
        'speed': randint(1, 3),
    }
    meteors.append(rock)


# שלושה מטאורים לפתיחה
spawn()
spawn()
spawn()

while True:
    # --- יצירה תקופתית ---
    since = since + 1
    if since >= GAP:
        spawn()
        since = 0

    # --- מקדמים את כולם ---
    for m in meteors:
        m['x'] = m['x'] + m['speed']

    # --- מוציאים את מי שיצא מהמסך ---------------------------
    # הדרך הנכונה: בונים רשימה חדשה של מי שנשאר.
    alive = []
    for m in meteors:
        if m['x'] <= 127:
            alive.append(m)
    meteors = alive
    #
    # הגרסה השבורה, להדגמה בכיתה — אל תשאירו אותה:
    #   for m in meteors:
    #       if m['x'] > 127:
    #           meteors.remove(m)
    # --------------------------------------------------------

    # print('meteors:', len(meteors))

    # --- מציירים את הפריים ---
    display.fill(0)
    for m in meteors:
        draw_meteor(m['x'], m['y'])
    display.show()
