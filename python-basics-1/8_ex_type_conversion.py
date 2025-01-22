import time

birth_year = input("What year were you born?: ")
current_year = time.localtime().tm_year
current_age = current_year - int(birth_year)
print(f"You're {current_age} years old!")