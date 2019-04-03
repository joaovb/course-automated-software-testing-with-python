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