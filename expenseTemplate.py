import pandas as pd

# Data for each sheet (headers only)
sheets = {
    "Dashboard": pd.DataFrame({
        "Metric": ["Total Income", "Total Expenses", "Net Profit", "Total Payroll", "Distributions"],
        "Amount": [0, 0, 0, 0, 0]
    }),
    "Income": pd.DataFrame(columns=["Date", "Invoice #", "Client / Project", "Amount", "Payment Method", "Notes"]),
    "Expenses": pd.DataFrame(columns=["Date", "Category", "Vendor", "Amount", "Payment Method", "Notes"]),
    "Payroll + Distributions": pd.DataFrame(columns=["Date", "Salary Paid", "Payroll Taxes Withheld", "Net Salary", "Distributions", "Payroll Taxes Paid", "Notes"]),
    "Tax Payments": pd.DataFrame(columns=["Date", "Tax Type", "Amount Paid", "Method", "Notes"]),
}

# Create Excel file
file_name = "LLC_Bookkeeping_Template.xlsx"
with pd.ExcelWriter(file_name, engine="xlsxwriter") as writer:
    for sheet_name, df in sheets.items():
        df.to_excel(writer, index=False, sheet_name=sheet_name)

print(f"✅ Bookkeeping spreadsheet saved as {file_name}")
