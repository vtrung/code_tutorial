def uppercase_name(name):
    try:
        print("here")
        # words are just list of letters. list are indexes starting at 0. 
        # so name[0] is the first letter
        first_letter = name[0].upper()

        # you can use this format to get value from list
        # [0:10] would mean getting the first letter and 10 letters after
        # i used [1:], i want to skip 0 and leaving the second part empty, means to get the rest
        rest_of_name = name[1:].lower()
        name = first_letter + rest_of_name
        return name
    except Exception as e:
        print(str(e))

