# Numbers that are multiples of 3 or 5
print('sum of multiples of 3 or 5 up to 1000(<):')
i = 1
total_sum_arr = []
while i < 1000:
    i += 1
    if i % 3 == 0:
        total_sum_arr.append(i)

    if i % 5 == 0:
        total_sum_arr.append(i)
    if i == 999:
        break

# print(total_sum_arr)
sum_arr_without_duplicates = list(set(total_sum_arr))
print(sum(sum_arr_without_duplicates))
