from datetime import date


def vote(b_year):

    age = date.today().year - b_year

    if age < 16:
        print(f"{age} years old: DON'T VOTE!")
    elif 18 <= age < 65:
        print(f"{age} years old: MANDATORY VOTE!")
    elif 16 <= age < 18 or age > 65:
        print(f"{age} years old: OPTIONAL VOTE!")


voter = int(input("Voter's year of birth: "))
vote(voter)
