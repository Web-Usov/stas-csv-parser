# # from my_pack import pack

# # pack.greeting()

# # cities = ["Moscow", "Paris", "Rome"]
# # separator = ", "
# # result = separator.join(cities)
# # print(result)

# # my_tuple = (1, 4, 2)
# # print(my_tuple)

# # set1 = {1, 2, 3}
# # set2 = {3, 4, 5}

# # print(set1 | set2)
# # print(set1 & set2)
# # print(set1 - set2)

# # from collections import defaultdict
# # my_dict = defaultdict(list)
# # my_dict["1"].append(1)
# # my_dict["1"].append(2)
# # my_dict["2"].append(2)

# # print(my_dict)

# # keys = ["1", "2", "3"]
# # inventory = dict.fromkeys(keys, 0)
# # print(inventory)

# # squares = [x ** 2 for x in range(10)]
# # print(squares)

# # odds = [x for x in range(10) if x % 2 == 1]
# # print(odds)

# # odds2 = [x ** 2 if x % 2 == 1 else x / 2 for x in range(1,10)]
# # print(odds2)

# first = []

# for x in range(1, 5):
#   for y in range(5, 1, -1):
#     if x != y:
#       first.append((x, y))

# print(first)

# second = [(x, y) for x in range(1, 5) for y in range(5, 1, -1) if x != y]
# print(second)

# vec = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# digits = [digit for lst in vec for elem in lst for digit in elem]
# print(digits)

# super_dict = dict([(x, y) for x in range(1, 5) for y in range(5, 1, -1)])
# print(super_dict)

# gen = (x for x in range(1, 5))
# print(gen.__next__())
# print(gen.__next__())

# s_dict = {key: value for key, value in zip([1,2,3], ["a", "b", "c"])}
# print(s_dict)

# l = ['a', 'v', 'r', 'h', 'v', 'c', 'd', 'y', 'g', 'b']
# print(sorted(l))
# print(l.sort())

# original_dict = {'b': 1, 'a': 2, 'c': 3}
# sorted_list = sorted(original_dict.items())
# sorted_dict = dict(sorted_list)
# print(sorted_dict)

# words = ['cat', 'hamster', 'squirrel', 'rabbit']
# sort_by_len = sorted(words, key=len, reverse=True)
# print(sort_by_len)

# def last_char(word):
#     return word[-1]

# print(sorted(words, key=last_char))

# from collections import defaultdict
# from statistics import median
# rows = [
#     {"student": "A", "coffee_spent": "100"},
#     {"student": "A", "coffee_spent": "300"},
#     {"student": "B", "coffee_spent": "500"},
# ]

# data = defaultdict(list)

# for row in rows:
#     data[row["student"]].append(int(row["coffee_spent"]))

# print(data)
# result = sorted([(student, median(values)) for student, values in data.items()],
#     key=lambda x: x[1],
#     reverse=True)
# print(result)



# data = {
#     "A": 200,
#     "B": 500,
#     "C": 100
# }

# result = sorted(data.items(),
#                 key=lambda x: x[1],
#                 reverse=True)
# print(result)





# rows = [
#     {"student": "A", "coffee_spent": "100"},
#     {"student": "A", "coffee_spent": "300"},
#     {"student": "B", "coffee_spent": "200"},
#     {"student": "B", "coffee_spent": "400"},
#     {"student": "C", "coffee_spent": "50"},
# ]

# data = defaultdict(list)

# for row in rows:
#     data[row["student"]].append(int(row["coffee_spent"]))

# result = sorted(
#     [(student, max(values)) for student, values in data.items()],
#     key = lambda x: x[1],
#     reverse=True
# )
# print(result)



# def ask_for_password(func):
#     def inner():
#         passcode = input("Enter your password: ")
#         if passcode == "123":
#             func()
#         else:
#             print("Incorrect password")
#     return inner

# @ask_for_password
# def start_server():
#     print("Starting server")

# if __name__ == "__main__":
#     start_server()


# class User:
#     def __init__(self, name, age, balance):
#         self.name = name
#         self.age = age
#         self.balance = balance

#     def show_info(self):
#         print(f"Name: {self.name}", f"Age: {self.age}", f"Amount: {self.balance}")

#     def change_balance(self, amount):
#         self.balance = amount

# user1 = User("John", 25, 100)
# user2 = User("Jane", 30, 50)
# user3 = User("Bob", 35, 200)

# users = [user1, user2, user3]
# a = (user.balance for user in users)

# print(next(a))

# print([user.balance for user in users])


# import timeit
# execution_time = timeit.timeit("''.join(str(n) for n in range(100))", number=10000)
# print(execution_time)

from abc import ABC, abstractmethod
from collections import defaultdict

class Report(ABC):
    @abstractmethod
    def generate(self, rows: list[dict[str, str]]) -> list[tuple[str, float]]:
        pass

class MaxCoffeeReport(Report):
    name: str = "max"

    def generate(self, rows: list[dict[str, str]]) -> list[tuple[str, float]]:
        data = defaultdict(list)
        for row in rows:
            student = row["student"]
            coffee_spent = int(row["coffee_spent"])
            data[student].append(coffee_spent)

        maxes = [
                    (student, max(values)) 
                    for student, values in data.items() 
                    if values
                ]

        return sorted(maxes, key=lambda x: x[1], reverse=True)


class AvgCoffeeReport(Report):
    name: str = "avg"

    def generate(self, rows: list[dict[str, str]]) -> list[tuple[str, float]]:
        data = defaultdict(list)
        for row in rows:
            student = row["student"]
            coffee_spent = int(row["coffee_spent"])
            data[student].append(coffee_spent)

        averages = [
            (student, sum(values) / len(values)) 
            for student, values in data.items()
            if values
        ]    

        return sorted(averages, key=lambda x: x[1], reverse=True)
    
REPORTS = {
    AvgCoffeeReport.name: AvgCoffeeReport,
    MaxCoffeeReport.name: MaxCoffeeReport
}
    
def get_report(name: str) -> Report:
    if name not in REPORTS:
        raise ValueError(f"Unknown report: {name}")
    return REPORTS[name]()

if __name__ == '__main__':
    rows = [
                {"student": "A", "coffee_spent": "100"},
                {"student": "A", "coffee_spent": "300"},
                {"student": "B", "coffee_spent": "200"},
                {"student": "B", "coffee_spent": "400"},
            ]

    report = get_report("max")

    generated_report = report.generate(rows)
    
    print(generated_report)

# def palindrome(text: str) -> bool:
#     for i in range(len(text) // 2):
#         if text[i] != text[-i - 1]:
#             return False
#     return True
    

# import csv
# try:
#     with open("test.txt", "r", encoding="utf-8") as f:
#         reader = csv.DictReader(f)

#         print(f"{'ID':<5} | {'NAME':<15} | {'EMAIL':<20}")
#         print("-" * 45)

#         for row in reader:
#             print(f"{row['id']:<5} | {row['name']:<15} | {row['email']:<20}")

# except FileNotFoundError:
#     print("File not found")
# except KeyError:
#     print("Ошибка: В файле отсутствуют нужные колонки (id, name, email).")

# from tabulate import tabulate

# data = [
#     ["1", "Иван", "ivan@mail.ru"],
#     ["2", "Алексей", "alex@gmail.com"],
#     ["105", "Константин", "konst@corp.it"]
# ]
# headers = ["ID", "Имя", "Email"]

# # Простой вывод
# print(tabulate(data, headers=headers, tablefmt="github"))
