import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
from database import get_db_connection
from utils import center_window, styled_label, styled_entry

def show_all_sales(root):
    """Display all sales"""
    win = tk.Toplevel(root)
    win.title("All Sales")
    center_window(win, 1100, 450)

    frame = tk.Frame(win)
    frame.pack(fill='both', expand=True, padx=10, pady=10)
    
    columns = ("SalesID", "Date", "Customer", "Car", "Amount", "Method")
    tree = ttk.Treeview(frame, columns=columns, show="headings", height=15)
    
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=140, anchor="center")
    
    v_scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=v_scroll.set)
    tree.pack(side="left", fill="both", expand=True)
    v_scroll.pack(side="right", fill="y")

    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT s.SalesID, s.SaleDate, c.Name, ca.Model, s.TotalAmount, s.PaymentMethod
                FROM Sales s
                JOIN Customer c ON s.CustomerID = c.CustomerID
                JOIN Car ca ON s.CarID = ca.CarID
            """)
            for row in cursor.fetchall():
                tree.insert("", tk.END, values=row)
        except Exception as e:
            messagebox.showerror("Error", "Failed to load sales: " + str(e))
        finally:
            conn.close()

def record_sale_window(root):
    """Record new sale"""
    win = tk.Toplevel(root)
    win.title("Record Sale")
    win.configure(bg='#f0f0f0')
    center_window(win, 500, 350)
    
    tk.Label(win, text="Sales Information", font=('Segoe UI', 12, 'bold'), 
            bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=10, sticky='w', padx=10)
    
    styled_label(win, "Customer ID *", 1, 0)
    customer_id = styled_entry(win, 1, 1)
    
    styled_label(win, "Car ID *", 2, 0)
    car_id = styled_entry(win, 2, 1)
    
    styled_label(win, "Total Amount *", 3, 0)
    amount = styled_entry(win, 3, 1)
    
    styled_label(win, "Payment Method *", 4, 0)
    method = ttk.Combobox(win, values=["Cash", "Card", "Financing"], font=('Segoe UI', 11), width=27)
    method.grid(row=4, column=1, padx=10, pady=5)
    
    def submit():
        if not customer_id.get() or not car_id.get() or not amount.get():
            messagebox.showerror("Error", "All fields are required")
            return
        
        conn = get_db_connection()
        if not conn:
            return
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Sales (SaleDate, CustomerID, CarID, TotalAmount, PaymentMethod)
                VALUES (%s, %s, %s, %s, %s)
            """, (date.today(), customer_id.get(), car_id.get(), amount.get(), method.get()))
            
            cursor.execute("UPDATE Car SET AvailabilityStatus = 'Sold' WHERE CarID = %s", (car_id.get(),))
            
            conn.commit()
            messagebox.showinfo("Success", "Sale recorded successfully!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", "Failed to record sale: " + str(e))
            conn.rollback()
        finally:
            conn.close()
    
    styled_button(win, "Record Sale", submit, 5)