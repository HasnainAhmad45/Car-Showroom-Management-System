import tkinter as tk
import re

def center_window(win, width=400, height=300):
    """Center a window on screen"""
    win.update_idletasks()
    x = (win.winfo_screenwidth() - width) // 2
    y = (win.winfo_screenheight() - height) // 2
    win.geometry(str(width) + "x" + str(height) + "+" + str(x) + "+" + str(y))

def validate_email(email):
    """Validate email format"""
    if not email:
        return False
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """Validate phone number format"""
    if not phone:
        return False
    pattern = r'^\+?1?\d{9,15}$'
    return re.match(pattern, phone) is not None

def styled_label(win, text, row, col, **kwargs):
    """Create styled label"""
    label = tk.Label(win, text=text, font=('Segoe UI', 11), bg='#f0f0f0', **kwargs)
    label.grid(row=row, column=col, padx=10, pady=5, sticky='w')
    return label

def styled_entry(win, row, col, **kwargs):
    """Create styled entry"""
    entry = tk.Entry(win, font=('Segoe UI', 11), width=30, **kwargs)
    entry.grid(row=row, column=col, padx=10, pady=5)
    return entry

def styled_button(win, text, command, row, col_span=2, **kwargs):
    """Create styled button"""
    btn = tk.Button(win, text=text, command=command, bg="#2196F3", fg="white", 
                   font=('Segoe UI', 11, 'bold'), **kwargs)
    btn.grid(row=row, columnspan=col_span, pady=10, padx=10, sticky='ew')
    return btn