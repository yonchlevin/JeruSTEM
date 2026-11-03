# main.py
# משתמש ב-tools.py. שני הקבצים חייבים לשבת באותה תיקייה.

# דרך א': מייבאים את הקובץ כולו וניגשים דרך הנקודה
import tools

print(tools.DEVICE)
tools.beep(3)

# דרך ב': מייבאים שם בודד ומשתמשים בו ישירות
from tools import c_to_f

print(c_to_f(25))    # 77.0
