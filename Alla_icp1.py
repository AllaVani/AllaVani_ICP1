#program1
import random

def main():
    # give the input string
    input_string = input("Enter a string: ")

    # Convert the string to a list of characters
    char_list = list(input_string)

    # Delete random characters
    num_deletions = random.randint(2, min(2, len(char_list))) 
    for _ in range(num_deletions):
        if len(char_list) >= 2:
            index_to_delete = random.randint(0, len(char_list) - 1)
            del char_list[index_to_delete]
        else:
            print("String is too short to delete more characters.")
            break

    # Reverse the output string
    reversed_string = ''.join(reversed(char_list))

    # Print the reversed string
    print("Reversed string:", reversed_string)

if __name__ == "__main__":
    main()

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # writing formulas for all the arthimetic operations
        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2

        # logic to avoid dividing by zero
        if num2 != 0:
            division = num1 / num2
        else:
            division = "Cannot divide by zero"

        print("Addition:", addition)
        print("Subtraction:", subtraction)
        print("Multiplication:", multiplication)
        print("Division:", division)

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

        #Program2

if __name__ == "__main__":
    main()

def main():
    sentence = input("Enter a sentence: ")

    # given condition to replace the word python with pythons
    updated_sentence = sentence.replace('python', 'pythons')

    # Print the output
    print("updated sentence:", updated_sentence)
#program3

if __name__ == "__main__":
    main()

def main():
    try:
        class_score = float(input("Enter the class score: "))



        # Check whether if the class score is greater than 100
        if class_score > 100:
            print("Invalid input. Class score cannot exceed 100.")
            return

        # write the if else conditions based on the grading scale
        if class_score >= 90:
            letter_grade = 'A'
        elif class_score >= 80:
            letter_grade = 'B'
        elif class_score >= 70:
            letter_grade = 'C'
        elif class_score >= 60:
            letter_grade = 'D'
        else:
            letter_grade = 'F'

        # Print the grade
        print("Letter grade:", letter_grade)

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()