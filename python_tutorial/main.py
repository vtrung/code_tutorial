from library import utilities
## importing a library. make sure you put an empty __init__.py file in library folder or python may not detect it

## better to use functions
def func_1():
    print("we are in function 1")
    print("do anything contained in function when called")

def anyname():
    print("name functions anyname but has to start with a letter")

def process_input(num1, num2):
    # this is a try/catch. useful if something can go wrong. in this case if someone doesn't pass in numbers
    try:
        # you can define a function with input like this
        print("{} + {} = {}".format(num1, num2, num1 + num2))
    except Exception as e:
        print("Something was wrong with your code so it threw an exception")
        print(str(e))
    
if __name__ == "__main__":
    # "if __name__ == "__main__" is how python know what to run if you call it. especially if it is just functions
    # useful or makes more sense later on when you create your own library w/o anything to run
    print("we are starting the run here")

    # calling functions
    func_1()
    anyname()

    process_input(1, 4)
    process_input(100, 40)
    process_input(2, "ok")

    # using a library
    name = utilities.uppercase_name("ving")
    print(name)