import unittest

file_name = "directory.txt"

class directory():
 #   def __init__(self, name, email, age, country):
 #       self.name = name
 #       self.email = email
 #       self.age = age
 #       self.country = country
    
    def addRecord(name, email, age, country):
        if not isinstance(name, str):
            return "Name is not a string"

        if not isinstance(email, str):
            return "Email is not a string"

        if not isinstance(age, int):
            return "Age is not an int"

        if not isinstance(country, str):
            return "Country is not a string"

        fd = open(file_name, "a+")
        fd.write("%s %s %d %s\n" % (name, email, age, country))
        fd.close()
        print("Added %s %s %d %s\n" % (name, email, age, country))

    def deleteRecord(name, email, age, country):
        if not isinstance(name, str):
            return "Name is not a string"

        if not isinstance(email, str):
            return "Email is not a string"

        if not isinstance(age, int):
            return "Age is not an int"

        if not isinstance(country, str):
            return "Country is not a string"

        fd = open(file_name, 'r', 1)
        lines = fd.readlines()
        fd.close()
 
        print("Delete Record called with %s %s %d %s\n" % (name, email, age, country))
 
        found = False
        newFile = open(file_name, "w+")
        for line in lines:
            parsed_line = line.rstrip('\n').split(" ")
            print(parsed_line)
            if name == parsed_line[0] and email == parsed_line[1] and age == parsed_line[2] and country == parsed_line[3]:
                print("Found %s %s %d %s" % (parsed_line[0], parsed_line[1], parsed_line[2], parsed_line[3]))
                found = True
            else:
                newFile.write(line)
                

        newFile.close()

        if not found:
            return "Record not Found"
        else:
            return


    def lookRecord(email, age):
        if not isinstance(email, str):
            return "Email is not a string"

        if not isinstance(age, int):
            return "Age is not an int"

        fd = open(file_name, 'r', 1)
        result = ''
        for line in fd:
            parsed_line = line.rstrip('\n').split(" ")
            print(parsed_line)
            if email == parsed_line[1] and age == parsed_line[2]:
                print("%s %s %d %s\n" % (parsed_line[0], parsed_line[1], parsed_line[2], parsed_line[3]))
                result = line
        fd.close()
        return line

    def listAllRecords():
        fd = open(file_name, 'r', 1)
        lines = fd.readlines()
        fd.close()
        for line in lines:
            print("%s" % line)
        return lines

    def clearAllRecords():
        clnfd = open(file_name, 'w').close()

class Test_Lab33(unittest.TestCase):
    #Right
    def test_clearAllRecords(self):
        self.assertIsNone(directory.clearAllRecords())

    def test_addRecords(self):
        self.assertIsNone(directory.addRecord("Juan", "juan@mail.com", 30, "Mexico"))

    def test_deleteRecords(self):
        self.assertIsNone(directory.addRecord("delete", "delete@mail.com", 30, "Delete"))
        self.assertIsNone(directory.deleteRecord("delete", "delete@mail.com", 30, "Delete"))

    def test_lookRecords(self):
        self.assertIsNone(directory.addRecord("look", "look@mail.com", 30, "look"))
        self.assertEqual(directory.lookRecord("delete@mail.com", 30), "look look@mail.com 30 look\n")

    #Boundaries

    #Inverse relationships

    #Cross-check results by other means
    
    #Errors forced to happen
    def test_addRecords_invName(self):
        self.assertEqual(directory.addRecord(5, "invalid@mail.com", 0, "Invalid"), "Name is not a string")

    def test_addRecords_invEmail(self):
        self.assertEqual(directory.addRecord("Invalid", 5, 0, "Invalid"), "Email is not a string")

    def test_addRecords_invAge(self):
        self.assertEqual(directory.addRecord("Invalid", "invalid@mail.com", "Invalid", "Invalid"), "Age is not an int")

    def test_addRecords_invCountry(self):
        self.assertEqual(directory.addRecord("Invalid", "invalid@mail.com", 0, 0), "Country is not a string")

    def test_deleteRecords_invName(self):
        self.assertEqual(directory.deleteRecord(5, "invalid@mail.com", 0, "Invalid"), "Name is not a string")

    def test_deleteRecords_invEmail(self):
        self.assertEqual(directory.deleteRecord("Invalid", 5, 0, "Invalid"), "Email is not a string")

    def test_deleteRecords_invAge(self):
        self.assertEqual(directory.deleteRecord("Invalid", "invalid@mail.com", "Invalid", "Invalid"), "Age is not an int")

    def test_deleteRecords_invCountry(self):
        self.assertEqual(directory.deleteRecord("Invalid", "invalid@mail.com", 0, 0), "Country is not a string")

    def test_deleteRecords_notFound(self):
        self.assertEqual(directory.deleteRecord("notFound", "notFound@mail.com", 0, "NotFound"), "Record not found")

    def test_lookRecords_notFound(self):
        self.assertIsNone(directory.lookRecord("NotFound@mail.com", 0))

    #Performance
    

if __name__ == '__main__':
    unittest.main()