# 🧾 Lavish Interpricies Payslip Generator

This project is a simple Python script that reads employee data from an Excel file and generates PDF payslips, optionally sending them via email.

## 📁 Files

- `employees.xlsx` — Contains:
  - Sheet 1: A formatted salary slip (not parsed by script)
  - Sheet 2 (named `Data`): Employee details such as Name, Email, Salary
- `payslip.py` — Python script that reads Excel data and creates PDFs
- `.env` — (Optional) Contains email credentials (for sending payslips)

## 🛠 Requirements

- Python 3.7+
- Install packages:
  ```bash
  pip install pandas fpdf yagmail python-dotenv
  ```

## ▶️ How to Use

1. Make sure your Excel file is named `employees.xlsx` and placed in the same folder as `payslip.py`.
2. Run the script:
   ```bash
   python payslip.py
   ```
3. PDFs will be generated and saved in the `payslips/` folder.

## 📬 Sending Emails (Optional)

1. Create a `.env` file with:
   ```
   EMAIL_USER=your_email@gmail.com
   EMAIL_PASSWORD=your_app_password
   ```
2. Make sure you enable **App Passwords** in your Google account settings.

3. The script will automatically send the generated PDF to each employee's email.

## 🧮 Net Salary Formula

```
Net Salary = Basic Salary + Allowances - Deductions
```

## 📌 Notes

- Column names in Excel must be: `Employee ID`, `Name`, `Email`, `Basic Salary`, `Allowances`, `Deductions`.
- Script reads from the **second sheet** of the Excel file.