import tkinter as tk
from tkinter import ttk, messagebox
from database import get_db_connection
from utils import center_window, styled_label, styled_entry, validate_email, validate_phone

def show_all_customers(root):
    """Display all customers"""
    win = tk.Toplevel(root)
    win.title("All Customers")
    center_window(win, 900, 400)

    frame = tk.Frame(win)
    frame.pack(fill='both', expand=True, padx=10, pady=10)
    
    columns = ("CustomerID", "Name", "Phone", "Email", "Address")
    tree = ttk.Treeview(frame, columns=columns, show="headings", height=15)
    
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor="center")
    
    v_scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=v_scroll.set)
    tree.pack(side="left", fill="both", expand=True)
    v_scroll.pack(side="right", fill="y")

    def load_customers():
        for item in tree.get_children():
            tree.delete(item)
        
        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT CustomerID, Name, ContactNumber, Email, Address FROM Customer")
                for row in cursor.fetchall():
                    tree.insert("", tk.END, values=row)
            except Exception as e:
                messagebox.showerror("Error", "Failed to load customers: " + str(e))
            finally:
                conn.close()
    
    load_customers()

def add_customer_window(root):
    """Add new customer"""
    win = tk.Toplevel(root)
    win.title("Add Customer")
    win.configure(bg='#f0f0f0')
    center_window(win, 500, 350)
    
    tk.Label(win, text="Customer Information", font=('Segoe UI', 12, 'bold'), 
            bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=10, sticky='w', padx=10)
    
    styled_label(win, "Customer ID *", 1, 0)
    cust_id = styled_entry(win, 1, 1)
    
    styled_label(win, "Name *", 2, 0)
    name = styled_entry(win, 2, 1)
    
    styled_label(win, "Phone *", 3, 0)
    phone = styled_entry(win, 3, 1)
    
    styled_label(win, "Email *", 4, 0)
    email = styled_entry(win, 4, 1)
    
    styled_label(win, "Address", 5, 0)
    address = tk.Text(win, font=('Segoe UI', 11), width=30, height=2)
    address.grid(row=5, column=1, padx=10, pady=5)
    
    def submit():
        if not cust_id.get() or not name.get():
            messagebox.showerror("Error", "ID and Name are required")
            return
        
        if not validate_phone(phone.get()):
            messagebox.showerror("Error", "Invalid phone number")
            return
        
        if not validate_email(email.get()):
            messagebox.showerror("Error", "Invalid email")
            return
        
        conn = get_db_connection()
        if not conn:
            return
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Customer (CustomerID, Name, ContactNumber, Email, Address)
                VALUES (%s, %s, %s, %s, %s)
            """, (cust_id.get(), name.get(), phone.get(), email.get(), address.get("1.0", tk.END).strip()))
            
            conn.commit()
            messagebox.showinfo("Success", "Customer added successfully!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", "Failed to add customer: " + str(e))
        finally:
            conn.close()
    
    styled_button(win, "Add Customer", submit, 6)