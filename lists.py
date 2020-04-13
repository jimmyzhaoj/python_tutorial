nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1 = [n for n in nums]
print (list1)
list2 = [n * n for n in nums]
print (list2)
list3 = map(lambda n: n * n, nums)
print (list3)
list4 = [n for n in nums if n % 2 == 0]
print (list4)
list5 = filter(lambda n: n % 2 == 0, nums)
print (list5)
list6 = [(letter, num) for letter in "abcd" for num in range(4)]
print (list6)

names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heros = ["Batman", "superman", "Spiderman", "Wolverine", "Deadpool"]
print zip(names, heros)

dict1 = {name: hero for name, hero in zip(names, heros) if name != "Peter"}
print dict1
