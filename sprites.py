# sprites.py
# החללית והמטאור — שתי פונקציות ציור בלבד.
#
# הכלל היחיד שחשוב: כל מספר בציור נמדד ביחס ל-y (ול-x במטאור).
# מי שכותב מספר מוחלט מקבל ספרייט שמתפרק ברגע שהוא זז.

from hw import display

SHIP_X = 120
SHIP_H = 12
MAX_SHIP_Y = 64 - SHIP_H        # 52

METEOR = 5
MAX_METEOR_Y = 64 - METEOR      # 59


def draw_ship(y):
    """חללית בת 12 פיקסלים, מחוד שמאלה לכיוון המטאורים."""
    display.fill_rect(122, y + 2, 6, 8, 1)      # גוף
    display.vline(121, y + 4, 4, 1)             # חרטום
    display.vline(120, y + 5, 2, 1)
    display.hline(125, y, 3, 1)                 # כנפון עליון
    display.hline(125, y + 11, 3, 1)            # כנפון תחתון


def draw_meteor(x, y):
    """סלע 5 על 5: שני מלבנים חופפים יוצרים מתומן."""
    display.fill_rect(x + 1, y, 3, 5, 1)
    display.fill_rect(x, y + 1, 5, 3, 1)


def draw_lives(n):
    """n ריבועים קטנים בפינה הימנית העליונה של המסך."""
    for i in range(n):
        display.fill_rect(104 + i * 6, 0, 4, 4, 1)
