course = ["Hostory", "math", "Physics"]
course2 = ["algebra", "music"]
course.append("Art")
course.insert(0, "GGG")
course.extend(course2)
# print(course)
# print(len(course))
# print(course[2])
# print(course[-1])
# print(course[0:2])
# print(course[1:])
# popped = course.pop()
# print(popped)
# print(course)
# course.reverse()
# print(course)
# course.sort()
# print(course)
# nums = [1, 4, 5, 6, 2, 9]
# nums.sort()
# print(nums)
# nums.sort(reverse=True)
# print(nums)
# sorted_nums = sorted(nums)
# print(sorted_nums)
# for index, item in enumerate(course, start=1):
#     print(index, item)
# course_str = "_-_".join(course)
# print(course_str)
# new_list = course_str.split("_-_")
# print(new_list)
tuple_1 = ("Hostory", "math", "Physics")
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
sets_1 = {"Hostory", "math", "Physics", "math"}
sets_2 = {"Hostory", "algebra", "Physics", "Art"}
print(sets_1)
print("math" in sets_1)
print(sets_1.intersection(sets_2))
print(sets_1.difference(sets_2))
print(sets_1.union(sets_2))
