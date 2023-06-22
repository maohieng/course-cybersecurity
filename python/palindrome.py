# Program to check if a string is palindrome or not
string = input("Enter a string: ")
if string == string[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")