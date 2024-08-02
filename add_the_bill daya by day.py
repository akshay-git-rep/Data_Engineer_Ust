height_of_tower = 442
thick_of_bill = 0.11
no_of_bills = 1
days = 1


while (no_of_bills * thick_of_bill) <= height_of_tower:
    no_of_bills *= 2
    days += 1

print("it takes",days,
      "days to complete the tower, total number of bills is",no_of_bills,
      "height of bills",no_of_bills * thick_of_bill)

