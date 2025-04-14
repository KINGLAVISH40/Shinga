import pandas as pd
from fpdf import FPDF
import os
import yagmail
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Email credentials
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Create payslips directory if it doesn't exist
if not os.path.exists("payslips.py"):
    os.makedirs("payslips.py")

# Read Excel file
try:
    df = pd.read_excel("employees.xlsx")
except Exception as e:
    print("Error reading Excel file:", e)
    exit()
df.columns = df.columns.str.strip()  # Removes leading/trailing spaces from column names
df = pd.read_excel("employees.xlsx", sheet_name="Data")
df.columns = df.columns.str.strip()  # Clean column names
print(df.columns)  # Prints out all the column names
print(df['Name'])  # Prints the "Name" column to check for correctness
import pandas as pd
from fpdf import FPDF
import os
import yagmail
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Load Excel file
xls = pd.ExcelFile("employees.xlsx")
print("Sheets found:", xls.sheet_names)

# Load employee data from "Data" sheet
df = pd.read_excel(xls, sheet_name="Data")
df.columns = df.columns.str.strip()

# Create payslips directory
os.makedirs("payslips", exist_ok=True)

# Define generate_payslip function
def generate_payslip(employee):
    emp_id = str(employee["Employee ID"])
    name = employee["Name"]
    basic = employee["Basic Salary"]
    allowances = employee["Allowances"]
    deductions = employee["Deductions"]
    net_salary = basic + allowances - deductions

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Lavish Interpricies - Salary Slip", ln=True, align="C")

    pdf.set_font("Arial", "", 12)
    pdf.ln(10)
    pdf.cell(0, 10, f"Employee ID: {emp_id}", ln=True)
    pdf.cell(0, 10, f"Name: {name}", ln=True)
    pdf.cell(0, 10, f"Basic Salary: ${basic}", ln=True)
    pdf.cell(0, 10, f"Allowances: ${allowances}", ln=True)
    pdf.cell(0, 10, f"Deductions: ${deductions}", ln=True)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, f"Net Salary: ${net_salary}", ln=True)
    pdf.ln(20)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, "Employee Signature: ____________________", ln=True)
    pdf.cell(0, 10, "Authorized Signature: ___________________", ln=True)

    filename = f"payslips/{emp_id}_{name}.pdf"
    pdf.output(filename)
    return filename

# Define email sending function
def send_email(to_email, subject, body, attachment):
    try:
        yag = yagmail.SMTP(EMAIL_USER, EMAIL_PASSWORD)
        yag.send(to=to_email, subject=subject, contents=body, attachments=attachment)
        print(f" Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

#  Process each employee
for index, row in df.iterrows():
    try:
        payslip_file = generate_payslip(row)
        email_subject = "Your Payslip for This Month"
        email_body = f"Hello {row['Name']},\n\nPlease find attached your payslip for this month.\n\nBest regards,\nHR Department"
        send_email(row['Email'], email_subject, email_body, payslip_file)
    except Exception as e:
        print(f"Error processing employee {row['Employee ID']}: {e}")

