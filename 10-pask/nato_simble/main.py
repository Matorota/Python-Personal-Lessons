import pandas
import csv

dt = pandas.read_csv("nato_phonetic_alphabet.csv.")

# n = 2
#
# temperatures = []
# data_no_header = word[]
# count = 0
# res = ""

word = str("nigeria")
warudo = list(word)
print(warudo)
code_list = dt["code"].to_list()
letter_list = dt["letter"].to_list()
print(code_list)
count = 0
for row in word:
    if word == code_list:
        print()