monthly_income = float(input("Enter monthly income: "))
monthly_expenditure = float(input("Enter monthly expenditure: "))

monthly_savings = monthly_income - monthly_expenditure
Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Projected savings after one year, with interest, is: ", Projected_Savings)