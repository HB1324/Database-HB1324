
def birthdaycalc(birth_year, current_year):
    age = current_year - birth_year
    return age


birth = int(input('Enter your Birth Year: '))
current = int(input('Enter Current Year: '))

age = birthdaycalc(birth, current)
print("You are", age, "years old!")
