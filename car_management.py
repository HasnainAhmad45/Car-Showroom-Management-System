import tkinter as tk
from tkinter import ttk, messagebox
from database import get_db_connection
from utils import center_window, styled_label, styled_entry

def show_all_cars(root):
    """Display all cars"""
    win = tk.Toplevel(root)
    win.title("All Cars")
    center_window(win, 1000, 450)

    frame = tk.Frame(win)
    frame.pack(fill='both', expand=True, padx=10, pady=10)
    
    columns = ("CarID", "Model", "Make", "Year", "Color", "Price", "Status")
    tree = ttk.Treeview(frame, columns=columns, show="headings", height=15)
    
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor="center")
    
    v_scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=v_scroll.set)
    tree.pack(side="left", fill="both", expand=True)
    v_scroll.pack(side="right", fill="y")

    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT CarID, Model, Make, Year, Color, Price, AvailabilityStatus FROM Car")
            for row in cursor.fetchall():
                tree.insert("", tk.END, values=row)
        except Exception as e:
            messagebox.showerror("Error", "Failed to load cars: " + str(e))
        finally:
            conn.close()

def add_car_window(root):
    """Add new car"""
    win = tk.Toplevel(root)
    win.title("Add Car")
    win.configure(bg='#f0f0f0')
    center_window(win, 500, 400)
    
    tk.Label(win, text="Car Information", font=('Segoe UI', 12, 'bold'), 
            bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=10, sticky='w', padx=10)
    
    styled_label(win, "Car ID *", 1, 0)
    car_id = styled_entry(win, 1, 1)
    
    styled_label(win, "Model *", 2, 0)
    model = styled_entry(win, 2, 1)
    
    styled_label(win, "Make *", 3, 0)
    make = styled_entry(win, 3, 1)
    
    styled_label(win, "Year *", 4, 0)
    year = styled_entry(win, 4, 1)
    
    styled_label(win, "Color *", 5, 0)
    color = styled_entry(win, 5, 1)
    
    styled_label(win, "Price *", 6, 0)
    price = styled_entry(win, 6, 1)
    
    def submit():
        if not car_id.get() or not model.get() or not make.get():
            messagebox.showerror("Error", "ID, Model, Make are required")
            return
        
        conn = get_db_connection()
        if not conn:
            return
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Car (CarID, Model, Make, Year, Color, Price, AvailabilityStatus)
                VALUES (%s, %s, %s, %s, %s, %s, 'Available')
            """, (car_id.get(), model.get(), make.get(), year.get(), color.get(), price.get()))
            
            conn.commit()
            messagebox.showinfo("Success", "Car added successfully!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", "Failed to add car: " + str(e))
        finally:
            conn.close()
    
    styled_button(win, "Add Car", submit, 7)