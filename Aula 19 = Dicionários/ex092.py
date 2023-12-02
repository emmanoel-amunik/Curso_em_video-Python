from datetime import datetime
man_info = dict()
man_info['name'] = str(input("Worker's name: "))
w_year = int(input("Worker's year of birth: "))
man_info['age'] = datetime.now().year - w_year
man_info['work_card'] = int(input("Worker's work card number ('0' don't): "))
if man_info['work_card'] != 0:
    man_info['hiring_year'] = int(input("Worker's hiring year: "))
    man_info['wage'] = float(input("Worker's wage: U$ "))
    man_info['retirement'] = (man_info['hiring_year'] + 35) - w_year
print('-' * 35)
print(f"The worker's name is {man_info['name']}")
print(f"The worker's age is {man_info['age']}")
print(f"The worker's WC is {man_info['work_card']}")
if man_info['work_card'] != 0:
    print(f"The worker's hiring year is {man_info['hiring_year']}")
    print(f"The worker's wage is U$ {man_info['wage']}")
    print(f"The worker's retirement will be with {man_info['retirement']} years old.")
