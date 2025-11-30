import tkinter as tk
from tkinter import messagebox
from config import APP_TITLE
from utils import center_window
from customer_management import show_all_customers, add_customer_window
from car_management import show_all_cars, add_car_window
from sales_management import show_all_sales, record_sale_window
from dashboard import open_dashboard

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.configure(bg='#f0f0f0')
        center_window(self.root, 900, 600)
        
        self.show_main_menu()
    
    def show_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        header = tk.Frame(self.root, bg='#2196F3')
        header.pack(fill='x')
        
        tk.Label(header, text="🚗 " + APP_TITLE, font=("Segoe UI", 18, "bold"), 
                bg="#2196F3", fg="white").pack(side='left', padx=20, pady=15)
        
        content = tk.Frame(self.root, bg='#f0f0f0')
        content.pack(fill='both', expand=True, padx=20, pady=20)
        
        tk.Label(content, text="Main Menu", font=("Segoe UI", 16, "bold"), 
                bg="#f0f0f0").pack(pady=10)
        
        button_frame = tk.Frame(content, bg='#f0f0f0')
        button_frame.pack(fill='both', expand=True, pady=20)
        
        buttons = [
            ("📊 Dashboard", open_dashboard),
            ("👥 Customer Management", self.customer_menu),
            ("🚗 Car Management", self.car_menu),
            ("💰 Sales Management", self.sales_menu),
        ]
        
        for idx, (label, command) in enumerate(buttons):
            row = idx // 2
            col = idx % 2
            
            btn = tk.Button(button_frame, text=label, command=lambda c=command: c(self.root),
                           bg="#2196F3", fg="white", font=('Segoe UI', 12, 'bold'),
                           height=4, relief='raised', bd=2)
            btn.grid(row=row, column=col, padx=15, pady=15, sticky='nsew')
        
        button_frame.grid_rowconfigure(0, weight=1)
        button_frame.grid_rowconfigure(1, weight=1)
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
    
    def customer_menu(self, root):
        menu_win = tk.Toplevel(root)
        menu_win.title("Customer Management")
        menu_win.configure(bg='#f0f0f0')
        center_window(menu_win, 400, 300)
        
        tk.Label(menu_win, text="Customer Management", font=('Segoe UI', 14, 'bold'), 
                bg='#f0f0f0').pack(pady=20)
        
        tk.Button(menu_win, text="View All Customers", command=lambda: show_all_customers(root),
                 bg="#2196F3", fg="white", font=('Segoe UI', 11, 'bold'), width=30).pack(pady=10)
        
        tk.Button(menu_win, text="Add New Customer", command=lambda: add_customer_window(root),
                 bg="#4CAF50", fg="white", font=('Segoe UI', 11, 'bold'), width=30).pack(pady=10)
    
    def car_menu(self, root):
        menu_win = tk.Toplevel(root)
        menu_win.title("Car Management")
        menu_win.configure(bg='#f0f0f0')
        center_window(menu_win, 400, 300)
        
        tk.Label(menu_win, text="Car Management", font=('Segoe UI', 14, 'bold'), 
                bg='#f0f0f0').pack(pady=20)
        
        tk.Button(menu_win, text="View All Cars", command=lambda: show_all_cars(root),
                 bg="#2196F3", fg="white", font=('Segoe UI', 11, 'bold'), width=30).pack(pady=10)
        
        tk.Button(menu_win, text="Add New Car", command=lambda: add_car_window(root),
                 bg="#4CAF50", fg="white", font=('Segoe UI', 11, 'bold'), width=30).pack(pady=10)
    
    def sales_menu(self, root):
        menu_win = tk.Toplevel(root)
        menu_win.title("Sales Management")
        menu_win.configure(bg='#f0f0f0')
        center_window(menu_win, 400, 300)
        
        tk.Label(menu_win, text="Sales Management", font=('Segoe UI', 14, 'bold'), 
                bg='#f0f0f0').pack(pady=20)
        
        tk.Button(menu_win, text="View All Sales", command=lambda: show_all_sales(root),
                 bg="#2196F3", fg="white", font=('Segoe UI', 11, 'bold'), width=30).pack(pady=10)
        
        tk.Button(menu_win, text="Record New Sale", command=lambda: record_sale_window(root),
                 bg="#4CAF50", fg="white", font=('Segoe UI', 11, 'bold'), width=30).pack(pady=10)

def main():
    root = tk.Tk()
    root.configure(bg='#f0f0f0')
    app = MainApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()