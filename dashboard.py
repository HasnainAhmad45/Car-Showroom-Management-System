import tkinter as tk
from database import get_db_connection
from utils import center_window

def open_dashboard(root):
    """Open dashboard with statistics"""
    win = tk.Toplevel(root)
    win.title("Dashboard")
    win.configure(bg='#f0f0f0')
    center_window(win, 900, 500)
    
    metrics_frame = tk.Frame(win, bg='#f0f0f0')
    metrics_frame.pack(fill='x', padx=10, pady=10)
    
    def create_metric_card(parent, title, value, color):
        card = tk.Frame(parent, bg=color, relief='raised', bd=2)
        card.pack(side='left', fill='x', expand=True, padx=5, pady=5)
        
        tk.Label(card, text=title, font=('Segoe UI', 10), bg=color, fg='white').pack(pady=5)
        tk.Label(card, text=str(value), font=('Segoe UI', 16, 'bold'), bg=color, fg='white').pack(pady=5)
        return card
    
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            
            cursor.execute("SELECT COUNT(*) FROM Customer")
            total_customers = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM Car WHERE AvailabilityStatus = 'Available'")
            available_cars = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM Car")
            total_cars = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM Sales")
            total_sales = cursor.fetchone()[0]
            
            cursor.execute("SELECT COALESCE(SUM(TotalAmount), 0) FROM Sales")
            total_revenue = cursor.fetchone()[0]
            
        except Exception as e:
            pass
        finally:
            conn.close()
    
    create_metric_card(metrics_frame, "Total Customers", total_customers, "#2196F3")
    create_metric_card(metrics_frame, "Available Cars", available_cars, "#4CAF50")
    create_metric_card(metrics_frame, "Total Cars", total_cars, "#FF9800")
    create_metric_card(metrics_frame, "Total Sales", total_sales, "#9C27B0")
    create_metric_card(metrics_frame, "Total Revenue", "Rs. " + str(int(total_revenue)), "#607D8B")
