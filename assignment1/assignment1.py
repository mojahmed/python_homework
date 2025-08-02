# Write your code here.

# Task 1
def hello():
    return "Hello!"

# Task 2
# def greet(name):
#     return f"Hello, {name}!"
def greet(name):
    return "Hello, {}!".format(name)

# Task 3
def calc(a, b, operation="multiply"):
    try:
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            return a / b
        elif operation == "modulo":
            return a % b
        elif operation == "int_divide":
            return a // b
        elif operation == "power":
            return a ** b
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

# Task 4 
def data_type_conversion(value, type_name):
    try:
        if type_name == "int":
            return int(value)
        elif type_name == "float":
            return float(value)
        elif type_name == "str":
            return str(value)
    except:
        return "You can't convert {} into a {}.".format(value, type_name)

# Task 5 
def grade(*args):
    try:
        total = sum(args)
        count = len(args)
        average = total / count

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except:
        return "Invalid data was provided."


# Task 6
def repeat(text, count):
    result = ""
    for i in range(count):
        result = result + text
    return result

# Task 7
def student_scores(mode, **kwargs):
    try:
        if mode == "mean":
            total = 0
            count = 0
            for score in kwargs.values():
                total += score
                count += 1
            return total / count
        elif mode == "best":
            best_score = None
            best_student = None
            for student, score in kwargs.items():
                if best_score is None or score > best_score:
                    best_score = score
                    best_student = student
            return best_student
    except:
        return "Invalid data"

# Task 8
def titleize(text):
    small_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = text.split()
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            words[i] = word.capitalize()
        else:
            if word in small_words:
                words[i] = word 
            else:
                words[i] = word.capitalize()
    return " ".join(words)

# Task 9
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result


# Task 10
def pig_latin(text):
    vowels = "aeiou"
    words = text.split()
    result_words = []

    for word in words:
        if word[0] in vowels:
            new_word = word + "ay"
        else:
            if word.startswith("qu"):
                new_word = word[2:] + "quay"
            else:
                i = 0
                while i < len(word) and word[i] not in vowels:
                    if i + 1 < len(word) and word[i:i+2] == "qu":
                        i += 2
                        break
                    i += 1
                new_word = word[i:] + word[:i] + "ay"
        result_words.append(new_word)

    return " ".join(result_words)




# using this to printing the test manual (python3 assignment1.py)

if __name__ == "__main__":
    # Task 1
    print("Task 1 - hello():", hello())  

    # Task 2
    print("Task 2 - greet('Mohammed'):", greet("Mohammed")) 

    # Task 3
    print("Task 3 - calc(5, 6):", calc(5, 6))  # 30 (multiply default)
    print("Task 3 - calc(12, 4, 'subtract'):", calc(12, 4, "subtract"))  # 8
    print("Task 3 - calc(10, 0, 'divide'):", calc(10, 0, "divide"))  # Can't divide by 0

    # Task 4
    print("Task 4 - convert '5.5' to float:", data_type_conversion("5.5", "float"))  # 5.5
    print("Task 4 - convert 'abc' to int:", data_type_conversion("abc", "int"))  # error message

    # Task 5
    print("Task 5 - grade(75, 85, 95):", grade(75, 85, 95))  # B
    print("Task 5 - grade('a', 'b'):", grade("a", "b"))  # Invalid data was provided.

    # Task 6
    print("Task 6 - repeat('up,', 4):", repeat("up,", 4))  # up,up,up,up,

    # Task 7
    print("Task 7 - student_scores('mean', Tom=75, Dick=89, Angela=91):", student_scores("mean", moh=75, tom=89, sarah=91))  
    print("Task 7 - student_scores('best', Tom=75, Dick=89, Angela=91, Frank=50):", student_scores("best", Tom=75, Mohammed=89, Sarah=91, Ahmed=50))  

    # Task 8
    print("Task 8 - titleize('war and peace'):", titleize("war and peace"))  
    print("Task 8 - titleize('a separate peace'):", titleize("a separate peace")) 

    # Task 9
    print("Task 9 - hangman('difficulty', 'ic'):", hangman("difficulty", "ic"))  # _i__ic____
    print("Task 9 - hangman('alphabet', 'ab'):", hangman("alphabet", "ab"))  # a___ab__

    # Task 10
    print("Task 10 - pig_latin('apple'):", pig_latin("apple"))  
    print("Task 10 - pig_latin('banana'):", pig_latin("banana")) 
    print("Task 10 - pig_latin('cherry'):", pig_latin("cherry")) 
    print("Task 10 - pig_latin('quiet'):", pig_latin("quiet")) 
    print("Task 10 - pig_latin('Good morning'):", pig_latin("Good morning"))  
    print("Task 10 - pig_latin('my name is Mohammed'):", pig_latin("my name is Mohammed"))  


