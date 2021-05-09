def f1():
    tmp1 = int(input("enter the roll no of student"))
    return (tmp1)


def f2():
    tmp2 = str(input("enter the name of student"))
    return (tmp2)


def f3():
    tmp3 = int(input("enter the class of student"))
    return (tmp3)


def f4():
    tmp4 = str(input("enter the section of student"))
    return (tmp4)


def f5():
    tmp5 = float(input("enter the marks of first subject"))
    return (tmp5)


def f6():
    tmp6 = float(input("enter the marks of second subject"))
    return (tmp6)


def f7():
    tmp7 = float(input("enter the marks of third subject"))
    return (tmp7)


def f8():
    tmp8 = float(input("enter the marks of fourth subject"))
    return (tmp8)


def f9():
    tmp9 = float(input("enter the marks of fifth subject"))
    return (tmp9)


def f10(s1, s2, s3, s4, s5):
    total = s1 + s2 + s3 + s4 + s5
    return (total)


def f11(total):
    avg = total / 5
    return avg


def f12(avg):
    if avg >= 91 and avg <= 100:
        print("Grade = A1")
    elif avg >= 81 and avg < 91:
        print("Grade = A2")
    elif avg >= 71 and avg < 81:
        print("Grade = B1")
    elif avg >= 61 and avg < 71:
        print("Grade = B2")
    elif avg >= 51 and avg < 61:
        print("Grade = C1")
    elif avg >= 41 and avg < 51:
        print("Grade = C2")
    elif avg >= 33 and avg < 41:
        print("Grade = D")
    elif avg >= 21 and avg < 33:
        print("Grade = E1")
    elif avg >= 0 and avg < 21:
        print("Grade = E2")
    else:
        print("Invalid Input!")


