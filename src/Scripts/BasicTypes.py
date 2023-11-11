from string import Template
# Two basic types of numbers in Python
# 1. Integers
# 2. Floating point numbers

print('Python numbers')

n1 = 2
n2 = 1.1

print('n1 = 2 type of n1', str(type(n1)))
print('n2 = 1.1 type of n2', str(type(n2)))

print('float(n1)', str(float(n1)))
print('int(n1)', str(int(n2)))

# Boolean type in Python

print('Boolean type in Python')

b1 = True
b2 = False

print(type(b1))

print(b1)
print(b2)

print(str(0), ': ', str(bool(0)))
print(str(1), ': ', str(bool(1)))
print('\'\'', ': ', str(bool('')))
print('Hello: ', str(bool('Hello')))
print('None: ', str(bool(None)))
print('[]: ', str(bool([])))
print('[1, 2, 3]: ', str(bool([1, 2, 3])))
print('{}: ', str(bool({})))
print('{1: 2, 3: 4}: ', str(bool({1: 2, 3: 4})))

# Strings in Python
# Strings are immutable
# Strings can be enclosed in single quotes or double quotes
# Strings can be enclosed in triple quotes to span multiple lines
# Literal strings can be concatenated with the + operator
# Strings can be indexed and sliced
# Strings can be formatted with the format() method
# Strings can be formatted with the % operator
# Strings can be formatted with f-strings (in Python 3.6+)
# Strings can be formatted with the Template class
# Strings can be compared with the < and > operators
# Strings can be compared with the == and != operators
# Strings can be compared with the is and is not operators
# Strings can be compared with the in and not in operators


print('Strings in Python')

s1 = 'Hello'
s2 = "Hello"

print(type(s1))

print('\'Hello\': ', s1)
print('"Hello": ', s2)

print("print(s1, ' ', \"World\")")
print(s1, ' ', 'World')

print('print(3)')
print(3)

print('print(\'use str() to covert numbers to strings: \', str(3)')
print('use str() to covert numbers to strings: ', str(3))

a = """Use triple quotes to create
a string that contains multiple lines."""
print(a)

print('print(\'Use \\ to escape characters: \', \'\\n\\t\\\'\\\"\')')

print('use in to check if a string contains a substring')
print("print('\'Hello\' in \'Hello World\'')")
print('\'Hello\' in \'Hello World\'')

b = "Hello, World!"
print("print(b[2:5])")
print(b[2:5])

print("age = 36")
age = 36
print("txt = 'My name is John, and I am {}'")
txt = 'My name is John, and I am {}'
print("print(txt.format(age))")
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

name = "Eric"
age = 74
print("Hello, %s. You are %s." % (name, age))

f"Hello, {name}. You are {age}."
'Hello, Eric. You are 74.'

# List Student stores the name and marks of three students
Student = [('Ram', 90), ('Ankit', 78), ('Bob', 92)]

# We are creating a basic structure to print the name and
# marks of the students.
t = Template('Hi $name, you have got $marks marks')

for i in Student:
    print(t.substitute(name=i[0], marks=i[1]))

str1 = 'apple'
str2 = 'banana'

print('str1 = \'apple\'')
print('str2 = \'banana\'')
print('str1 < str2: ', str1 < str2)
print('str1 > str2: ', str1 > str2)
print('str1 == str2: ', str1 == str2)
print('str1 != str2: ', str1 != str2)
print('str1 is str2: ', str1 is str2)
print('str1 is not str2: ', str1 is not str2)
print('\'a\' in str1: ', 'a' in str1)
print('\'a\' not in str1: ', 'a' not in str1)
