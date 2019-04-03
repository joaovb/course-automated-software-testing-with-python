my_variable = "hello"


grades = [77, 80, 90]
grades_tuples = (77, 80, 90) #imutable
set_grades = {77, 80, 90} # unique & unordered


# print(sum(grades) / len(grades))
# print(sum(grades_tuples) / len(grades_tuples))
# grades.append(108)

grades_tuples = grades_tuples + (100, 200)

set_grades.add(900)

print(set_grades)
print("***************")

## Set operations

your_lottery_numbers = {1, 2, 3, 4, 5}
winning_number = {1, 3, 5, 7, 9, 11}

# print(your_lottery_numbers.intersection(winning_number))
print(your_lottery_numbers.union(winning_number))

print({1, 2, 3, 4}.difference({1, 2}))

print("***********")

lista_negra = [29, 78, 80]


print(sum(lista_negra))


set1 = {14, 5, 9, 31, 12, 77, 67, 8,}
set2 = {5}

