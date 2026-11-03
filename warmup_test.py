# warmup_test.py
# בדיקת חימום לתחילת המפגש. הקובץ הזה עומד בפני עצמו בכוונה —
# הוא לא מייבא כלום חוץ מהספריות של הבקר, כדי שתקלה בו תצביע על החומרה.
#
# שלושת הסימנים שצריך לראות:
#   1. המסך מציג READY
#   2. לחיצה על הכפתור משנה את מה שכתוב על המסך
#   3. ה-Shell נקי משגיאות

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
display = SSD1306_I2C(128, 64, i2c)
button = Pin(4, Pin.IN, Pin.PULL_UP)

while True:
    display.fill(0)
    display.text('READY', 0, 0, 1)

    if button.value() == 0:          # 0 = לחוץ, בגלל PULL_UP
        display.text('PRESSED', 0, 24, 1)
    else:
        display.text('press button', 0, 24, 1)

    display.show()
