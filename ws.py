# StuyHacksXIPythonWorkshop
Open In Colab
i = 5       # integer
f = 5.5     # float/double
s = 'hello' # string
b = False   # boolean
if not b:
  print('no')
no
ftoi = int(f) # convert f from a float to an integer
print(ftoi)

# int from float cuts off anything after the decimal point, regardless of whether we should round up or down
# [FLOOR]
5
intstring = '5'
print(type(intstring))
stoi = int(intstring) # convert intstring from a string to an integer

print(type(stoi))
<class 'str'>
<class 'int'>
i+f # addition
10.5
i-f # subtraction
-0.5
s1 = 'hello'
s2 = 'world'
s1 + ' ' + s2 # concatenation
'hello world'
for character in s: # goes thru each character of s (one at a time, without skipping)
  print(character)

# h
# e
# l
# l
# o
h
e
l
l
o
# len(s) -> length of string s [in this case 5]
# range(n) -> gives you a group of numbers to loop over
# range(5) -> 0, 1, 2, 3, 4
for index in range(len(s)):
  print(index)
  print(s[index])
0
h
1
e
2
l
3
l
4
o
# len(s) -> length of string s [in this case 5]
# range(n) -> gives you a group of numbers to loop over
# range(4) -> 0, 1, 2, 3
for index in range(len(s) - 1):
  print(s[index] + s[index + 1])
he
el
ll
lo
# len(s) -> length of string s [in this case 5]
# range(n) -> gives you a group of numbers to loop over
# range(4) -> 0, 1, 2, 3
for index in range(len(s) - 1):
  if s[index] == s[index + 1]: # check if 2 characters in a row are the same
    print("2 CHARS IN A ROW")
    print(s[index] + s[index + 1])

# he
# el
# ll <- enter the if statement here [prints stuff]
# lo
2 CHARS IN A ROW
ll
# len(s) -> length of string s [in this case 5]
# range(n) -> gives you a group of numbers to loop over
# range(4) -> 0, 1, 2, 3
for index in range(len(s) - 1):
  if s[index] == s[index + 1]: # check if 2 characters in a row are the same
    print("2 CHARS IN A ROW")
    print(s[index] + s[index + 1])

  if s[index] != s[index + 1]: # check if 2 characters in a row are different
    print("2 CHARS NOT IN A ROW")
    print(s[index] + s[index + 1])
2 CHARS NOT IN A ROW
he
2 CHARS NOT IN A ROW
el
2 CHARS IN A ROW
ll
2 CHARS NOT IN A ROW
lo
inputstring = input("type string here: ")

for index in range(len(inputstring) - 1):
  if inputstring[index] == inputstring[index + 1]:
    print("2 CHARS IN A ROW")
    print(inputstring[index] + inputstring[index + 1])

# bi
# il
# ll <- enter the if statement here [prints stuff]
type string here: bill
2 CHARS IN A ROW
ll
#             inputs  [can be nothing]
#                |
#                v
# function -> factory [does something/nothing]
#                |
#                v
#             outputs [can be nothing]

def funK(string1, string2):
  return string1[0] == string2[0] # returns if first character of each string are the same
funK('hello', 'world') # h is not w
False
funK('hello', 'hi') # h is h
True
teststring1 = input('type first string here: ')
teststring2 = input('type second string here: ')

while teststring1 != 'quit prog' and teststring2 != 'quit prog': # check if teststring1 or teststring2 is equal to 'quit prog', and if so, then quit
  print('are first characters the same: ' + str(funK(teststring1, teststring2)))

  teststring1 = input('type first string here: ')
  teststring2 = input('type second string here: ')

# teststring1 == quit prog | teststring2 == quit prog | stop program
#                     True |                     True | Yes
#                    False |                     True | Yes
#                     True |                    False | Yes
#                    False |                    False | No
type first string here: quit prog
type second string here: quintessential
teststring1 = input('type first string here: ')
teststring2 = input('type second string here: ')

while teststring1 == 'quit prog' or teststring2 == 'quit prog': # check if teststring1 or teststring2 is equal to 'quit prog', and if so, then quit
  print('are first characters the same: ' + str(funK(teststring1, teststring2))) # print if 2 characters are same

  teststring1 = input('type first string here: ') # read input1 again
  teststring2 = input('type second string here: ') # read input2 again

# teststring1 == quit prog | teststring2 == quit prog | stop program
#                     True |                     True | Yes
#                    False |                     True | Yes
#                     True |                    False | Yes
#                    False |                    False | No
with open('sample_data/README.md', 'r') as f: # reads the file
  print(f.read())
testtest
f = open('sample_data/README.md', 'r') 
print(f.read())
f.close()
test
with open('sample_data/README.md', 'w') as f: # wipes and restarts the file
  f.write('test')
with open('sample_data/README.md', 'a') as f: # appends to the end of the file
  f.write('test')
l = ['x', 5, 3, 'six'] # list

for element in l: # loop thru list
  print(element)
x
5
3
six
l = ['x', 5, 3, 'six'] # list

for index in range(len(l)): # loop thru list
  print(index)
0
1
2
3
l = ['x', 5, 3, 'six'] # list

for index in range(len(l) - 1): # loop thru list
  print(l[index], l[index + 1])
x 5
5 3
3 six
tpl = ('x', 5, 3, 'six') # tuple

print(tpl)

for index in range(len(tpl) - 1): # loop thru list
  print(tpl[index], tpl[index + 1])
('x', 5, 3, 'six')
x 5
5 3
3 six
l[0] = 'ten' # modify list
print(l)
['ten', 5, 3, 'six']
print(l == ['ten', 5, 3, 'six']) # list equality
print(l == ['ten', 6, 3, 'six'])
True
False
tpl[0] = 'ten' # "try to" modify tuple
print(tpl)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-57-b236ea5b60c8> in <module>()
----> 1 tpl[0] = 'ten'
      2 print(tpl)

TypeError: 'tuple' object does not support item assignment
st = set(['x', 5, 3, 'six']) # set

print(st)
{3, 5, 'x', 'six'}
st.add('x')
print(st)
{3, 5, 'x', 'six'}
st[0] # 'try to' access set by index
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-71-028cc1d9138b> in <module>()
----> 1 st[0]

TypeError: 'set' object is not subscriptable
for element in st: # loop thru set
  print(element)
3
5
x
six
sttol = list(st) # convert set to list
print(sttol)
[3, 5, 'x', 'six']
dct = {} # dictionary

dct['bill'] = 'ni'
dct['abir'] = 'taheer' # assigning keys values

print(dct['bill']) # looking up values from keys
ni
for key in dct:
  print(key + ' ' + dct[key]) # looping thru a dictionary
bill ni
abir taheer
