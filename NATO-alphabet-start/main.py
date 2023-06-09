import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}
name_in = input("Enter a name: ")
name = name_in.upper()
nato_name = [letter_dict[letter] for letter in name]
print(nato_name)

