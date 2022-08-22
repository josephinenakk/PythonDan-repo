# Python String Methods
print("Python String Methods \n")
# 1. capitalize() : Converts the first character to upper case and the rest are converted to lower case.
# a. Converts the first character to upper case
st1 = "hello, and welcome ."
x = st1.capitalize()
print ("\n line 7- capitalize(hello, and welcome ) = ",x) # Result= Hello, and welcome to my world.

#b. The first character is converted to upper case, and the rest are converted to lower case.
st2= "games are FUN!"
print ("\n line 12- capitalize(games are FUN!) = ",y)

#c. if the first character is a number:
st3 = "36 is my Age."
z = st3.capitalize()
print ("\n line 17- capitalize(36 is my Age) = ",z)

#2.	casefold() : Converts string into lower case.
st1 = "Hello, And Welcome"
x = st1.casefold()
print("\n line 22- casefold(Hello, And Welcome) = ",x)

#3.	center()	: Returns a centered string
#Print the word "Josephine", taking up the space of given nuber (in this case 25) characters, with "banana" in the middle.
name = "Josephin"
x = name.center(25)
print("\n line 28- Josephine.center(25) = ",x)

#4.	count()	: Returns the number of times a specified value occurs in a string.
'''  count takes parameters
value => Required: A String  => The string to value to search for
start => Optional: An Integer=> The position to start the search. Default is 0
end   => Optional: An Integer=> The position to end the search. Default is the end of the string.
'''
#Syntax: string.count(value, start, end)
# a. count method with value only
st1 = "I love cherries, cherries are my favorite fruits."
x = st1.count("cherries")
print('\n st1= I love cherries, cherries are my favorite fruits')
print('\n line 41- count with search value "cherries" in the string st1= ', x)

#b.Search from position starting to endding:
x = st1.count("cherries", 7, 15)
print("\n line 45- count method with value ,satrt and end point mention = ",x)

#5.	encode() : Returns an encoded version of the string
# https://www.w3schools.com/charsets/ref_html_utf8.asp
# https://www.w3schools.com/CHARSETS/ref_html_ascii.asp

# unicode string
string = 'pythön!'
# print string
print('\n line 53- The string is: ', string.encode())
# ignore error
print('\n line 56- The encoded version (with ignore) is: ', string.encode("ascii", "ignore"))
# replace error
print('\n line 58- The encoded version (with replace) is: ', string.encode("ascii", "replace"))

#6.	endswith() : Returns true if the string ends with the specified value
st= "welcome to my world"
x = st.endswith("d")
print('\n line 63- Is st(welcome to my world) ends with d = ', x)

#7.	expandtabs() : Sets the tab size of the string
#Parameter :tabsize=>	Optional. A number specifying the tabsize. Default tabsize is 8.
st7 = "H\te\tl\tl\to"
print('\n line 68- expandtabs st = ',st7)
print('\n line 69- expandtabs st = ',st7.expandtabs())
print('\n line 70- expandtabs st = ',st7.expandtabs(2))
print('\n line 71- expandtabs st = ',st7.expandtabs(10))

#8.	find(): Searches the string for a specified value and returns the position of where it was found
#The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found.
#Syntax :string.find(value, start, end)
st8 = "Searches the string for a specified value"
x = st8.find("o")
print('\n line 78- find "o" in st8= ', x)
print('\n line 79- find "a" in st8= ',st8.find("a"))
print('\n line 80- index of "a" in st8= ',st8.index("a"))
x = st8.find("e", 5, 10)
print('\n line 82- find "e" in st8 between index 5,10 = ',x)

#9.	format() : Formats specified values in a string
#Insert the price inside the placeholder, two-decimal format:
st9 = "For only {price:.2f} dollars!"
print('\n line 87- two-decimal format = ', st9.format(price = 37))

#Using different placeholder values:
# a. named indexes:
st9_1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
print('\n line 92- named indexes placeholder= ', st9_1)

# b. numbered indexes:
st9_2 = "My name is {0}, I'm {1}".format("John",36)
print('\n line 96- numbered indexes placeholder= ', st9_2)

# c. empty placeholders:
st9_3 = "My name is {}, I'm {}".format("John",36)
print('\n line 100- empty placeholders= ', st9_3)

# d. Left aligns the result (within the available space) :< ,we insert the number 8 to set the available space for the value to 8 characters.
st_4 = "We have {:<8} chickens."
print('\n line 104- "<" to left-align the value(8) = ', st_4.format(49))

#e. Right aligns the result (within the available space) :> we insert the number 8 to set the available space for the value to 8 characters.
st_5= "We have {:>8} chickens."
print('\n line 108- ">" to right-align the value(8) = ', st_5.format(49))

#f.Center aligns the result (within the available space) :^ we insert the number 8 to set the available space for the value to 8 characters.
st_6 = "We have {:^8} chickens."
print('\n line 112-  "^" to center-align the value(8) = ', st_6.format(49))

#g.Places the sign to the left most position := we insert the number 8 to set the available space for the value to 8 characters.
st_7 = "The temperature is {:=8} degrees celsius."
print('\n line 116- :=Places the sign to the left most position = ', st_7.format(-5))

#8. Use a plus sign to indicate if the result is positive or negative
#Use "+" to always indicate if the number :
st_8 = "The temperature is between {:+} and {:+} degrees celsius."
print('\n line 121- Use a plus sign to indicate= ', st_8.format(-3, 7))

#h.Use a minus sign for negative values only
#Use "-" to always indicate if the number is negative (positive numbers are displayed without any sign):
st_9 = "The temperature is between {:-} and {:-} degrees celsius."
print('\n line 126- Use a minus sign for negative values only= ', st_9.format(-3, 7))

#i.Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
st_10 = "The temperature is between {: } and {: } degrees celsius."
print('\n line 130- Use a space to insert an extra space before positive numbers= ', st_10.format(-3, 7))

#j.Use a comma as a thousand separator :,
st_11= "The universe is {:,} years old."
print('\n line 134- Use a comma as a thousand separator= ', st_11.format(13800000000))

#k.Use a underscore as a thousand separator :_
st_12= "The universe is {:_} years old."
print('\n line 138- Use a underscore as a thousand separator= ',st_12.format(13800000000))

#l.Binary format :b
st_13 = "The binary version of {0} is {0:b}"
print('\n line 142- Binary format= ',st_13.format(5))

#m.Decimal format :d
st_14 = "We have {:d} chickens."
print('\n line 146- Decimal format= ',st_14.format(0b101))

#n.Scientific format, with a lower case e
#Use "e" to convert a number into scientific number format (with a lower-case e):
st_15= "We have {:e} chickens."
print('\n line 151- Scientific format, with a lower case e= ',st_15.format(5))

#o.Scientific format, with an upper case E
#Use "E" to convert a number into scientific number format (with an upper-case E):
st_16= "We have {:E} chickens."
print('\n line 156- Scientific format, with a lower case E= ',st_16.format(5))

#p.Fix point number format
#Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals:
st_17 = "The price is {:.2f} dollars."
print('\n line 161- Fix point number format given placeholder value= ',st_17.format(45))

#without the ".2" inside the placeholder, this number will be displayed like this:
st_17a= "The price is {:f} dollars."
print('\n line 165- Fix point number format placeholder default= ',st_17a.format(45))

#q. Fix point number format, in uppercase format (show inf and nan as INF and NAN)
#Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:
x = float('inf')
st_18 = "The price is {:F} dollars."
print('\n line 171- Fix point number format, in uppercase format= ',st_18.format(x))

#q.1same example, but with a lower case f:
st_18a = "The price is {:f} dollars."
print('\n line 175- Fix point number format, in lowercase format= ',st_18a.format(x))

#r.Octal format
#Use "o" to convert the number into octal format:
st_19 = "The octal version of {0} is {0:o}"
print('\n line -180- octal format= ',st_19.format(10))

#s.Hex format, lower case
#Use "x" to convert the number into Hex format:
st_20 = "The Hexadecimal version of {0} is {0:x}"
print('\n line 185- Hex format, lower case = ',st_20.format(255))

#t.Hex format, upper case
#Use "X" to convert the number into upper-case Hex format:
st_21 = "The Hexadecimal version of {0} is {0:X}"
print('\n line 185- Hex format, upper-case = ',st_21.format(255))

#u.Percentage format
#Use "%" to convert the number into a percentage format:
st_22= "You scored {:%}"
print('\n line 195- Percentage format= ',st_22.format(0.25))  # result: You scored 25.000000%(add 6 zeros)
#Or, without any decimals:
st_22a = "You scored {:.0%}"
print('\n line 195- Percentage format= ',st_22a.format(0.25)) # result: You scored 25%
print('\n')



#10. format_map() : Formats specified values in a string
#11. index() : Searches the string for a specified value and returns the position of where it was found
#12. isalnum() : Returns True if all characters in the string are alphanumeric
#13. isalpha() : Returns True if all characters in the string are in the alphabet
#14. isascii() : Returns True if all characters in the string are ascii characters
#15. isdecimal(): Returns True if all characters in the string are decimals
#16.	isdigit()	: Returns True if all characters in the string are digits
#17.	isidentifier() : Returns True if the string is an identifier
#18.	islower() : Returns True if all characters in the string are lower case
# 19.	isnumeric() : Returns True if all characters in the string are numeric
# 20.	isprintable() : Returns True if all characters in the string are printable
# 21.	isspace() : Returns True if all characters in the string are whitespaces
# 22.	istitle()	: Returns True if the string follows the rules of a title
# 23.	isupper() : Returns True if all characters in the string are upper case
# 24.	join() : Converts the elements of an iterable into a string
# 25.	ljust() : Returns a left justified version of the string
# 26.	lower() : Converts a string into lower case
# 27.	lstrip() : Returns a left trim version of the string
# 28. maketrans() : Returns a translation table to be used in translations
#29.	partition() : Returns a tuple where the string is parted into three parts
#30.	replace() : a string where a specified value is replaced with a specified value
#31.	rfind() : Searches the string for a specified value and returns the last position of where it was found
#32.	rindex()	: Searches the string for a specified value and returns the last position of where it was found
#33.	rjust(): Returns a right justified version of the string
#34.	rpartition() : Returns a tuple where the string is parted into three parts
#35.	rsplit() : Splits the string at the specified separator, and returns a list
#36.	rstrip()	: Returns a right trim version of the string
#37.	split() : Splits the string at the specified separator, and returns a list
#38.	splitlines() : Splits the string at line breaks and returns a list
#39.	startswith() : Returns true if the string starts with the specified value
#40.	strip() : Returns a trimmed version of the string
#41.	swapcase() : Swaps cases, lower case becomes upper case and vice versa
#42.	title() : Converts the first character of each word to upper case
#43.	translate() : Returns a translated string
#44.	upper() : Converts a string into upper case
#45.	zfill() : Fills the string with a specified number of 0 values at the beginning
