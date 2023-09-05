grades = [100, 4, 3, 4, 5, 3, 2, 2, 2, 2]


grades_no_duplicates = []
for i in grades:
    if i not in grades_no_duplicates:
        grades_no_duplicates.append(i)

print(grades_no_duplicates)

grades_no_duplicates = list(set(grades))
# grades_no_duplicates.sort(reverse=True)
print(grades_no_duplicates)
