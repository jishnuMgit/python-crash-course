# Strings

# we can use single or double quotes around your
# strings like this:
# "This is a string."
# 'This is also a string.'

message_1 = "Hello Python Crash Course reader!"

message_2 = 'Hello Python Crash Course reader!'
print(message_1, message_2)

# Changing Case in a String with Methods

name = "ada lovelace small" 

name_1="SMALL"
print(name.title()) # make the first letter of each word in the string capitalized.

print(name.upper()) # make all letters in the string uppercase.

print(name_1.lower()) # make all letters in the string lowercase.


first_name = "jishnu"
last_name = "m"
full_name = f"{first_name.title()} {last_name.title()}"
new_full_name = first_name.title() + " " + last_name.title()
print(full_name,new_full_name)

#useing f-string to format a string with variables like f"{variable_name}{variable_name}".

# Adding Whitespace to Strings with Tabs or Newlines

print("Python")
print("\tPython") # add a tab space before the string.
print("Languages:\nPython\nC\nJavaScript") # add a new line before the string.
print("Languages:\n\tPython\n\tC\n\tJavaScript") # add a new line and a tab space before the string.    



favorite_language = '         python         '

print(favorite_language.rstrip()) # remove the whitespace at the beginning and end of the string.
print(favorite_language.lstrip()) # remove the whitespace at the beginning of the string.
print(favorite_language.strip()) # remove the whitespace at the end of the string.


# Removing Prefixes

favorite_language = 'python'
message = 'python programming'

print(message.removeprefix('s'))  # remove the prefix 'python' if it appears at the start
print(message.removeprefix('py'))      # remove a shorter prefix at the start
print(message.removeprefix('Java'))    # no change if the prefix is not present

# If you want to remove suffixes instead, use .removesuffix() in a similar way
print(message.removesuffix('ming'))    # remove the suffix 'ming' if present
