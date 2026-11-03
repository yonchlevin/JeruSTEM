# tools.py
# ספרייה לדוגמה. כל קובץ .py הוא כבר ספרייה - אין צורך בשום דבר נוסף.
# הניחו את הקובץ הזה באותה תיקייה כמו main.py, או העלו אותו ל-ESP32 דרך Thonny.

DEVICE = 'ESP32'


def beep(times):
    """מדפיסה 'beep' מספר פעמים. לא מחזירה כלום - היא רק עושה."""
    for i in range(times):
        print('beep')


def c_to_f(celsius):
    """ממירה מעלות צלזיוס לפרנהייט ומחזירה את התוצאה."""
    return celsius * 9 / 5 + 32
