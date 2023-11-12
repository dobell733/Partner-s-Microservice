import subprocess
import json

def get_finance_data(monthly_income, monthly_expenses):
    # start and run the microservice in another process
    process = subprocess.run(
        ['python', '../microservice/microservice.py', str(monthly_income), str(monthly_expenses)],
        text=True,
        capture_output=True
    )
    # get and deserialize the result if everything worked
    if process.returncode == 0:
        result = json.loads(process.stdout)
        return result
    # report errors
    else:
        print(f'Error: {process.stderr}')

# usage
monthly_income = 5000
monthly_expenses = 3000
finance_data = get_finance_data(monthly_income, monthly_expenses)
print(finance_data)
