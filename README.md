# 🚗 Car Dealership Management System

A comprehensive desktop application built with Python and Tkinter for managing car dealership operations including customer management, inventory tracking, sales recording, and business analytics.

## 📋 Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Database Schema](#database-schema)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### 📊 Dashboard
- Real-time business metrics
- Total customers count
- Available cars inventory
- Total sales tracking
- Revenue statistics

### 👥 Customer Management
- Add new customers
- View all customers
- Store customer contact information
- Track customer purchase history

### 🚗 Car Inventory Management
- Add new cars to inventory
- View all cars with details
- Track car availability status
- Manage car specifications (Model, Make, Year, Color, Price)

### 💰 Sales Management
- Record new sales transactions
- View sales history
- Track payment methods (Cash, Card, Financing)
- Automatic inventory status updates

### 🔍 Additional Features
- Input validation for emails and phone numbers
- Professional UI with color-coded components
- Error handling and user-friendly messages
- Responsive design

## 🛠️ Technologies Used

- **Programming Language:** Python 3.x
- **GUI Framework:** Tkinter
- **Database:** MySQL
- **Libraries:**
  - `mysql-connector-python` - MySQL database connectivity
  - `python-dotenv` - Environment variable management
  - `tkinter` - GUI development (built-in)

## 💻 System Requirements

- Python 3.7 or higher
- MySQL Server 5.7 or higher
- Windows/Linux/MacOS

## 📥 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/car-dealership-management.git
cd car-dealership-management
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create Environment File
Create a `.env` file in the project root directory:
```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password_here
DB_NAME=db_proj
```

## 🗄️ Database Setup

### 1. Create Database and Tables
```bash
mysql -u root -p < schema.sql
```

### 2. Load Sample Data (Optional)
```bash
mysql -u root -p < seed_data.sql
```

### Manual Setup
Alternatively, you can manually execute the SQL files:
```sql
-- Connect to MySQL
mysql -u root -p

-- Run schema
source schema.sql;

-- Run seed data
source seed_data.sql;
```

## 🚀 Usage

### Running the Application
```bash
python main.py
```

### Application Workflow

1. **Launch Application**
   - The main menu displays four management options

2. **Dashboard**
   - View key business metrics at a glance

3. **Customer Management**
   - Click "Add New Customer" to register customers
   - Click "View All Customers" to see customer list
   - Required fields: ID, Name, Phone, Email

4. **Car Management**
   - Click "Add New Car" to add inventory
   - Click "View All Cars" to see inventory
   - Required fields: Car ID, Model, Make, Year, Color, Price

5. **Sales Management**
   - Click "Record New Sale" to process transactions
   - Click "View All Sales" to see sales history
   - Automatically updates car availability status

## 📁 Project Structure

```
car-dealership-management/
│
├── config.py                 # Configuration and environment variables
├── database.py               # Database connection handler
├── utils.py                  # Utility functions and helpers
├── customer_management.py    # Customer CRUD operations
├── car_management.py         # Car inventory operations
├── sales_management.py       # Sales transaction operations
├── dashboard.py              # Dashboard and analytics
├── main.py                   # Application entry point
│
├── schema.sql                # Database schema
├── seed_data.sql             # Sample data
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables 
├── .env.example              # Environment template
└── README.md                 # Project documentation
```

## 📸 Screenshots

### Main Menu
The main dashboard provides easy navigation to all system modules.

### Customer Management
Add and manage customer information with validation.

### Car Inventory
Track all vehicles with detailed specifications and availability status.

### Sales Dashboard
Record transactions and view sales history with revenue tracking.

## 🗃️ Database Schema

### Tables

**Customer**
- CustomerID (Primary Key)
- Name
- ContactNumber
- Email
- Address

**Car**
- CarID (Primary Key)
- Model
- Make
- Price
- Year
- Color
- AvailabilityStatus (Available/Sold)

**Sales**
- SalesID (Primary Key, Auto-increment)
- SaleDate
- CustomerID (Foreign Key)
- CarID (Foreign Key)
- TotalAmount
- PaymentMethod (Cash/Card/Financing)

**Employee**
- EmployeeID (Primary Key, Auto-increment)
- Name
- Role
- ContactNumber

**Insurance**
- InsuranceID (Primary Key, Auto-increment)
- CarID (Foreign Key)
- CustomerID (Foreign Key)
- InsuranceProvider
- InsuranceStartDate
- InsuranceEndDate
- CoverageAmount

**Booking**
- BookingID (Primary Key, Auto-increment)
- CustomerID (Foreign Key)
- CarID (Foreign Key)
- BookingDate
- BookingStatus (Pending/Confirmed/Cancelled)
- AdvanceAmount

**Warranty**
- WarrantyID (Primary Key, Auto-increment)
- CarID (Foreign Key)
- WarrantyStartDate
- WarrantyEndDate
- CoverageDetails

## 🔐 Security Considerations

- **Environment Variables:** Sensitive data (DB credentials) stored in `.env` file
- **Input Validation:** Email and phone number validation implemented
- **SQL Injection Prevention:** Parameterized queries used throughout
- **Error Handling:** Proper exception handling for database operations

## 🐛 Troubleshooting

### Database Connection Issues
```
Error: Failed to connect to database
```
**Solution:** Check your `.env` file credentials and ensure MySQL server is running

### Missing Dependencies
```
Error: No module named 'mysql.connector'
```
**Solution:** Run `pip install -r requirements.txt`

### Port Already in Use
```
Error: Can't connect to MySQL server on 'localhost'
```
**Solution:** Check if MySQL is running on correct port (default: 3306)

## 📝 Requirements.txt

```
mysql-connector-python==8.2.0
python-dotenv==1.0.0
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Thanks to the Python community for excellent documentation
- Tkinter for providing a robust GUI framework
- MySQL for reliable database management

## 📞 Support

For support, email your.email@example.com or create an issue in the GitHub repository.

## 🔮 Future Enhancements

- [ ] User authentication and authorization
- [ ] Advanced reporting and analytics
- [ ] Export data to PDF/Excel
- [ ] Email notifications for bookings
- [ ] Insurance and warranty management modules
- [ ] Employee management interface
- [ ] Advanced search and filter options
- [ ] Dark mode support
- [ ] Multi-language support

---

**Note:** This is a learning project for database management and GUI development. For production use, implement additional security measures and testing.

Made with ❤️ using Python and Tkinter