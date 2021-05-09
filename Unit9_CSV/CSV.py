import csv
import sys


# Writing on CSV File
def write_csv1():
    try:
        with open('data1.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["SN", "Name", "Contribution"])
            writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
            writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
            writer.writerow([3, "Guido van Rossum", "Python Programming"])
        print("Write contents on csv file successfully")
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        pass


# Reading from CSV File
def read_csv1():
    try:
        with open('data1.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        pass