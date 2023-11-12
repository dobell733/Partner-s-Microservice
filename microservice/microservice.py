import sys
import json

def calculate_finances(monthly_income, monthly_expenses):
    net_income = monthly_income - monthly_expenses
    debt_to_income_ratio = (monthly_expenses / monthly_income) * 100 if monthly_income else 0
    # return dictionary of values
    return {
        'net_income': net_income,
        'debt_to_income_ratio': debt_to_income_ratio
    }

if __name__ == "__main__":
    # get "command line" arguments
    monthly_income = float(sys.argv[1])
    monthly_expenses = float(sys.argv[2])
    # perform calculation
    result = calculate_finances(monthly_income, monthly_expenses)
    # serialize dictionary result to json and print to "stdout" for main program to use
    print(json.dumps(result))