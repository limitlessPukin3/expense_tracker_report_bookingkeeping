import pandas as pd
from io import BytesIO
from zipfile import ZipFile

# Create sample data for each sheet
dashboard = pd.DataFrame({
    "Metric": ["Total Income", "Total Expenses", "Net Profit", "Total Payroll", "Distributions"],
    "Amount": [0, 0, 0, 0, 0]
})

income = pd.DataFrame({
    "Date": [],
    "Invoice #": [],
    "Client / Project": [],
    "Amount": [],
    "Payment Method": [],
    "Notes": []
})

expenses = pd.DataFrame({
    "Date": [],
    "Category": [],
    "Vendor": [],
    "Amount": [],
    "Payment Method": [],
    "Notes": []
})

payroll = pd.DataFrame({
    "Date": [],
    "Salary Paid": [],
    "Payroll Taxes Withheld": [],
    "Net Salary": [],
    "Distributions": [],
    "Payroll Taxes Paid": [],
    "Notes": []
})

taxes = pd.DataFrame({
    "Date": [],
    "Tax Type": [],
    "Amount Paid": [],
    "Method": [],
    "Notes": []
})

# Save to a BytesIO stream
output = BytesIO()
with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
    dashboard.to_excel(writer, index=False, sheet_name='Dashboard')
    income.to_excel(writer, index=False, sheet_name='Income')
    expenses.to_excel(writer, index=False, sheet_name='Expenses')
    payroll.to_excel(writer, index=False, sheet_name='Payroll + Distributions')
    taxes.to_excel(writer, index=False, sheet_name='Tax Payments')

output.seek(0)

