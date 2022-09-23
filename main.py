from application.salary import calculate_salary
from application.db.people import get_employees
import datetime

if __name__ == '__main__':
    print(f'время: {datetime.datetime.now()}, salary: {calculate_salary()}')
    print(f'время: {datetime.datetime.today()}, people: {get_employees()}')