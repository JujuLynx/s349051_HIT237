def getGrade(mark):
    grades = {
        85: "High Distinction",
        75: "Distinction",
        65: "Credit",
        50: "Pass"
    }
    for score, grade in grades.items():
        if mark >= score:
            return grade
    return "Fail"

def main():
    print("What mark did you receive?")
    validInput = False
    while not validInput:
        mark = input("Score: ")
        try:
            mark = float(mark)
            break
        except:
            print("You didn't input a valid score.")
    myGrade = getGrade(mark)
    print("Your grade: " + myGrade)

main()