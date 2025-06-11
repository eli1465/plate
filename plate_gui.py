import tkinter as tk
from plate import plate_generator,plate_validator

# تابع اجرا‌شدن با دکمه
def check_plate():
    p1 = part1.get()
    p2 = part2.get()
    p3 = part3.get()
    p4 = part4.get()

    plate = plate_generator(p1, p2, p3, p4)

    if plate_validator(plate):
        result_label.config(text=" پلاک ثبت شد", fg="green")
    else:
        result_label.config(text=" پلاک مجاز نیست", fg="red")


# ایجاد پنجره
window = tk.Tk()
window.title("بررسی پلاک ایرانی")
window.geometry("400x250")

# ورودی‌ها
part1 = tk.StringVar()
part2 = tk.StringVar()
part3 = tk.StringVar()
part4 = tk.StringVar()

tk.Entry(window, textvariable=part1, font=("B Traffic", 16), width=5, justify='center').place(x=50, y=30)
tk.Entry(window, textvariable=part2, font=("B Traffic", 16), width=3, justify='center').place(x=110, y=30)
tk.Entry(window, textvariable=part3, font=("B Traffic", 16), width=5, justify='center').place(x=160, y=30)
tk.Entry(window, textvariable=part4, font=("B Traffic", 16), width=5, justify='center').place(x=230, y=30)

# دکمه بررسی
tk.Button(window, text="بررسی پلاک", font=("B Traffic", 14), command=check_plate).place(x=150, y=80)

# نمایش نتیجه
result_label = tk.Label(window, text="", font=("B Traffic", 16))
result_label.place(x=120, y=130)

# اجرای برنامه
window.mainloop()
