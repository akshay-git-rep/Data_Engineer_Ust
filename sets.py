lucky_draws = ()
print(type(lucky_draws), lucky_draws)

lucky_draws_o = {14,18,35,37,67,67,40,18,37}
lucky_draws_s = {11,18,35,36,66,55,43}
print("online value",lucky_draws_o)
lucky_draws_o.add(4)
print("online value",lucky_draws_o)
lucky_draws_o.discard(4)
print("online value",lucky_draws_o)
print("online value",lucky_draws_o,"length is:",len(lucky_draws_o))

for draw in lucky_draws_o:
    print(draw)

print("union:", lucky_draws_o | lucky_draws_s) # | means or and dublicate is deleted
print("intersect:", lucky_draws_o & lucky_draws_s) # & measn and show the same value
print("dif b/w online and shop", lucky_draws_o - lucky_draws_s) # show whcih is present in online and not in shopping
print("dif b/w shop and online", lucky_draws_s - lucky_draws_o)
print("*"*64)


set1 = {"apple","banana","appale"}
set2 = {5,1,3}
print(set1==set2)

print(set1)
set1.clear()
print(set1)
