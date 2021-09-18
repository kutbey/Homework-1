def letterNote(paramAvNote: float) -> str:
    """Letter Grade based on GPA"""
    if 0 <= paramAvNote < 45:return "FF"
    elif 45 <= paramAvNote < 50:return "FD"
    elif 50 <= paramAvNote < 55:return "DD"
    elif 55 <= paramAvNote < 65:return "DC"
    elif 65 <= paramAvNote < 75:return "CC"
    elif 75 <= paramAvNote < 80:return "CB"
    elif 80 <= paramAvNote < 85:return "BB"
    elif 85 <= paramAvNote < 90:return "BA"
    elif 90 <= paramAvNote <= 100:return "AA"
    else:return "--"


def truncate(f, n):
    """
    To get 2 digits after the comma
    :param f:number
    :param n:how digits
    """
    from math import floor
    return floor(f * 10 ** n) / 10 ** n


def isPassed(ex1: float, ex2: float, fin: float, midterm_rate: float = 0.3, final_rate: float = 0.4, \
             passingGrade: float = 60.0, finalGrade: float = 70.0) -> tuple:
    """
    Returns a tuple showing the student's passing status
    :param ex1: midterm 1
    :param ex2: midterm 1
    :param fin: final exam
    :param midterm_rate: midterm rate
    :param final_rate: final rate
    :param passingGrade: passing grade
    :param finalGrade: final grade
    :return: tuple(bool,float,str)
    :average calculation
    avarageCalcFormul=avarageNote = ((ex1 + ex2) * midterm_rate) + (fin * final_rate)
    class passing conditions
    1st condition:
     avarageNote >= passingGrade and fin >= finalGrade:
    2st condition:
    avarageNote >= passingGrade and fin <= finalGrade
    """

    ex1, ex2, fin = float(ex1), float(ex2), float(fin)
    avarageNote = ((ex1 + ex2) * midterm_rate) + (fin * final_rate)
    avarageNote = truncate(avarageNote, 2)
    if avarageNote >= passingGrade and fin >= finalGrade:return (True, avarageNote, letterNote(avarageNote))
    elif avarageNote >= passingGrade and fin <= finalGrade:return (False, avarageNote, "FF")
    else:return (False, avarageNote, "FF")


def scanFile(fileName: str) -> list:
    """
    Takes files from filename and converts them to the appropriate format
    :param fileName:for example data.txt
    :return:list object
    base data:
    Eleanor-Taylor Fizik 78/90/70
    parsed data:
    ('Eleanor', 'Taylor', 'Fizik', '78', '90', '70', 78.4, 'CB', True)
    """
    studentsList = []
    try:
        with open(fileName, "r", encoding="utf-8", errors="replace") as noteFile:
            for line, row in enumerate(noteFile, 1):
                if line == 1: continue
                item = row.split()  # ['Cora-Gill-Maryam', 'Matematik', 'Müh', '76/78/93']
                name_surname = item[0].split("-")
                name, surname = " ".join(name_surname[:-1]), name_surname[-1]
                department = " ".join(item[1:-1])
                ex1, ex2, fin = item[-1].split("/")
                status, note, letterNote_ = isPassed(ex1, ex2, fin)
                studentsList.append((name, surname, department, ex1, ex2, fin, note, letterNote_, status))
                print((name, surname, department, ex1, ex2, fin, note, letterNote_, status))
        return studentsList
    except Exception as err:
        print("Failed to Parse Data in File!")
        print(err)
        studentsList.append(('Hata', 'Hata', 'Hata', 1, 1, 1, 1, "--", False))
    finally:return studentsList


def createFiles(param_studentsList: list, sort, reverse=False) -> None:
    """
    This function sorts the data retrieved and parsed from the data.txt file.
    And then it creates the remainders.txt and passers.txt files according to the
    students' grade passing status and writes the data into them.
    :param param_studentsList: list from scanfile function
    :param sort: sort alphabetically and by grade point average
    :param reverse:
    :return:
    """
    try:
        remainders = open("remainders.txt", "w", encoding="utf-8", errors="replace")
        passersby = open("passersby.txt", "w", encoding="utf-8", errors="replace")
        title = lambda: f"{'Name':<17}{'Surname':<17}{'Department':<20}{'E1':<8}{'E2':<8}{'Fin':<8}{'Average':<12}{'Letter':<12}{'Status':<8}\n\n"
        passersby.write(title())
        remainders.write(title())
        for name, surname, department, ex1, ex2, fin, note, letterNote_, status in sorted(param_studentsList, key=sort,reverse=reverse):
            if status:passersby.write(f"{name:<17}{surname:<17}{department:<20}{ex1:<8}{ex2:<8}{fin:<8}{note:<12.2f}{letterNote_:<12}{'Passed':<8}\n")
            else: remainders.write( f"{name:<17}{surname:<17}{department:<20}{ex1:<8}{ex2:<8}{fin:<8}{note:<12.2f}{letterNote_:<12}{'Failed':<8}\n")
    except Exception as err:print(err)
    finally:
        passersby.close()
        remainders.close()


def DisplayMenu():
    print("\n1-Alphabetical Order\n2-Ranking by Average\n")
    option = input("Option:")
    if option == "1": createFiles(param_studentsList=scanFile("data.txt"), sort=lambda student: student[0], reverse=False)
    elif option == "2":createFiles(param_studentsList=scanFile("data.txt"), sort=lambda student: student[6], reverse=True)
    else:
        print("Incorrect Entry!")
        exit(-1)


if __name__ == "__main__":
    DisplayMenu()
