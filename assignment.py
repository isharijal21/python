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
        print(new_list.title())


    string = "You are my Sunshine"
    string_tranformation(string)






