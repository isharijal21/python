"""Q1. String Cleaning & Transformation
Write a Python function that takes a sentence and performs the following:
	•	Removes all vowels (a, e, i, o, u)
	•	Replaces spaces with underscores _
	•	Converts it to title case (first letter of each word capitalized)
Example:
Input:  "data engineering rocks"
Output: "Dt_Engnrng_Rcks"""


if __name__ == '__main__':

    def string_tranformation(sentence):
        new_list = ""
        vowels = set('aeiou')

        for char in sentence:
            if char not in vowels:
                if char == " ":
                    char = "_"
                new_list = new_list + char
        return (new_list.title())




    string = "You are my Sunshine"
    print(string_tranformation(string))

"""
Q2. Dictionary Aggregation
    Given a list of dictionaries representing sales transactions:
    sales = [
      {"product": "Pen", "amount": 10},
      {"product": "Book", "amount": 20},
      {"product": "Pen", "amount": 15},
      {"product": "Pencil", "amount": 5}
    ]

    Write a Python program to calculate total sales per product and print the result as:
    Pen: 25
    Book: 20
    Pencil: 5 
"""

print("========q2==============")
sales = [
        {"product": "Pen", "amount": 10},
        {"product": "Book", "amount": 20},
        {"product": "Pen", "amount": 15},
        {"product": "Pencil", "amount": 5}
    ]
totals = {}
for sell in sales:
    product = sell["product"]
    amount = sell["amount"]
    if product in totals:
        totals[product] = totals[product] + amount
    else:
        totals[product] = amount


for product, total in totals.items():
    print(product, ":", totals[product])


print("===========q3========")

"""Q3. Unique Numbers in List
Write a Python function that takes a list of integers and returns a new list containing elements that appear exactly once.
Example:
Input: [4, 5, 4, 6, 7, 5, 8]
Output: [6, 7, 8]
"""

def unique_number(lst):
    result = []
    for num in lst:
        if lst.count(num) == 1:
            result.append(num)
    return result


lst1 = [4, 5, 4, 6, 7, 5, 8]
print(unique_number(lst1))













    




















