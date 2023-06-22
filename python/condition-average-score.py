math_score = int(input("Enter your math score: "))
physic_score = int(input("Enter your physic score: "))
chemistry_score = int(input("Enter your chemistry score: "))

average_score = (math_score + physic_score + chemistry_score) / 3
if average_score >= 90:
    print("Your average score is:", average_score, "A")
elif average_score >= 80:
    print("Your average score is:", average_score, "B")
elif average_score >= 70:
    print("Your average score is:", average_score, "C")
elif average_score >= 60:
    print("Your average score is:", average_score, "D")
else:
    print("Your average score is:", average_score, "F")