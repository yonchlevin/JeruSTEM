# hw.py
# ספריית החומרה של הקורס. כל קובץ .py הוא ספרייה — בדיוק כמו tools.py מהמפגש הראשון.
# שאר הסקריפטים מייבאים מכאן, כדי שלא נכתוב את אותן שש שורות בכל פעם.
#
# השתמשו בזה כך:
#     from hw import display, button, buzzer

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

WIDTH = 128
HEIGHT = 64

# freq=400000 הוא הקצב שבו הבקר מדבר עם המסך.
# זה הברז שמאחורי שיעור מדידת הביצועים: קצב נמוך יותר = פחות פריימים בשנייה.
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
display = SSD1306_I2C(WIDTH, HEIGHT, i2c)

button = Pin(4, Pin.IN, Pin.PULL_UP)

buzzer = Pin(23, Pin.OUT)
buzzer.off()


def clear():
    """מנקה את המסך ומציג מיד. שימושי מה-Shell כשרוצים להתחיל מחדש."""
    display.fill(0)
    display.show()


def pressed():
    """מחזירה True כשהכפתור לחוץ. עוטפת את הלוגיקה ההפוכה של PULL_UP."""
    return button.value() == 0
