## make sure to use python 3 and up
## <-- how to comment

## print anything words
print("Put anything here an you can write to console")

## variables
num1 = 10
num2 = 25
words = "this is some words"

## print variables
## converting num1 to a string because you can't combine a string with a number
print(words + " " + str(num1))
print(words + " " + str(num2))

## add numbers
num3 = num1 + num2

## string formatting
formatted = "{} + {} = {}".format(num1, num2, num3)
print(formatted)

## if statements
if num1 >= 9:
    print("{} is greater than or equal to 9".format(num1))
else:
    print("it is not equal. this is the else statement")


## loops
for i in range(5):
    print("looping")
    print(i)


## another way to loop. google them if you need
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

