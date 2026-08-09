# When you’re using variables in Python, you need to adhere to a few rules
# and guidelines. Breaking some of these rules will cause errors; other guidelines just help you write code that’s easier to read and understand. Be sure
# to keep the following rules in mind when working with variables:


# •	 Variable names can contain only letters, numbers, and underscores.
# They can start with a letter or an underscore, but not with a number.
# For instance, you can call a variable message_1 but not 1_message.


# •	 Spaces are not allowed in variable names, but underscores can be used
# to separate words in variable names. For example, greeting_message works
# but greeting message will cause errors.


# •	 Avoid using Python keywords and function names as variable names.
# For example, do not use the word print as a variable name; Python
# has reserved it for a particular programmatic purpose. (See “Python
# Keywords and Built-in Functions” on page 466.)


# •	 Variable names should be short but descriptive. For example, name is
# better than n, student_name is better than s_n, and name_length is better
# than length_of_persons_name.


# •	 Be careful when using the lowercase letter l and the uppercase letter O
# because they could be confused with the numbers 1 and 0.


0variable="This is a error variable"#starts with a number

space variable="This is a error variable"#contains a space

print='This is a error variable'#uses a Python keyword as a variable name

n="jishnu M"#bad variable name

Student_name="jishnu M"#Good variable name

message = "Hello Python Crash Course reader!"
print(message)#error in variable name because of typo,its message variable not mesage variable



# Variables Are Labels 

# 1 Variables are often described as boxes you can store values in.
