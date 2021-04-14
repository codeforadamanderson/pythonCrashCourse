current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    if current_number == 1:
        print(f"{current_number} hot banana.")
    else:
        print(f"{current_number} hot bananas.")