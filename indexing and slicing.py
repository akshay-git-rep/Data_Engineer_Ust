message = "learning for data engineer"
notification = 'saturday is not working day'
#print(messgae,"",notification)

escape_codes = """
\n = message \nnewline
\r = carriage \rreturn
\t = tab
\' = escape the ' between '
\" = escape "
\\ = literal backslash
"""
#print(escape_codes)
#print("the character at 6th position is:",message[5])
#print("the string from 9th position is:",message[9:])
#print("the string till 9th position is:",message[:9])
#print("the string from 9th to 15th position is:",message[9:15])
#print("display last 5th character",message[-5])
#print("the string from last 5th position to till end is:",message[-5:])
#print("the string from 3rd position to last 5th position to till end is:",message[3:-5])
#print("the string from first to last 5th position to till end is:",message[:-5])
#print("length of string",len(message))
#print("print string in reverse:",message[::-1])
#print("no of 'in' word in the string:",message.count("in"))
#print("find the position on in : ", message.find("in"))
#print("find the position of IN after 6th positition:",message.find("in",6))
#print("find the position of IN between 15 to 25th positition:",message.find("in",15,25))
#print("split the message",message.split())
#print("split the message",message.split("in"))
#print(message.index("a"))

#name = input("enter the name:")
#reverse_name = name[::-1]
#print(reverse_name)

paragraph = """
Next, let's create Redux store to hold our application's state.
In the src directory, create a new file called store.js.
Inside this file, import the configureStore function from @reduxjs/toolkit
and your todoslice reduce. Then, use configureStore to create the Redux
store.
""" 
vowels = 0
not_vowels = 0

for count in paragraph:
    if (count.upper() in "AEIOU"):
        vowels += 1
    elif(count.isalpha()):
        not_vowels += 1

paragraph_count = paragraph.split()       
print(vowels)      
print(not_vowels)
print(len(paragraph_count))
#print(paragraph_count)


