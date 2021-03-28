import unittest


file_name = "directory.txt"


class directory():

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
#        print(f"Added {name} {email} {age} {country}\n")

    def deleteRecord(name, email, age, country):
        if not isinstance(name, str):
            return "Name is not a string"

        if not isinstance(email, str):
            return "Email is not a string"

        if not isinstance(age, int):
            return "Age is not an int"

        if not isinstance(country, str):
            return "Country is not a string"

        fd = open(file_name, 'r')
        lines = fd.readlines()
        fd.close()

        found = False
        newFile = open(file_name, "w+")
        for line in lines:
            parsed_line = line.rstrip('\n').split(" ")
            if name == parsed_line[0] and email == parsed_line[1] \
               and age == int(parsed_line[2]) and country == parsed_line[3]:
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
            if email == parsed_line[1] and age == int(parsed_line[2]):
                result = line
        fd.close()
        if result != '':
            return result

    def listAllRecords():
        fd = open(file_name, 'r', 1)
        lines = fd.readlines()
        fd.close()
        for line in lines:
            print(f"{line}")
        return lines

    def clearAllRecords():
        clnfd = open(file_name, 'w').close()


class Test_Lab33(unittest.TestCase):
    # Right
    def test_clearAllRecords(self):
        self.assertIsNone(directory.clearAllRecords())
        self.assertEqual(directory.listAllRecords(), [])

    def test_addRecords(self):
        self.assertIsNone(directory.addRecord("Juan", "juan@mail.com", 30,
                                              "Mexico"))

    def test_deleteRecords(self):
        self.assertIsNone(directory.addRecord("delete", "delete@mail.com",
                                              15, "Delete"))
        self.assertIsNone(directory.deleteRecord("delete", "delete@mail.com",
                                                 15, "Delete"))

    def test_lookRecords(self):
        self.assertIsNone(directory.addRecord("look", "look@mail.com", 85,
                                              "look"))
        self.assertEqual(directory.lookRecord("look@mail.com", 85),
                         "look look@mail.com 85 look\n")

    def test_listAllRecords(self):
        self.assertIsNone(directory.clearAllRecords())
        self.assertIsNone(directory.addRecord("Juan", "juan@mail.com", 30,
                                              "Mexico"))
        self.assertIsNone(directory.addRecord("Pedro", "pedro@mail.com", 20,
                                              "Zapopan"))
        self.assertEqual(directory.listAllRecords(),
                         ['Juan juan@mail.com 30 Mexico\n',
                          'Pedro pedro@mail.com 20 Zapopan\n'])

    # Boundaries

    # Inverse relationships

    # Cross-check results by other means

    # Errors forced to happen
    def test_addRecords_invName(self):
        self.assertEqual(directory.addRecord(5, "invalid@mail.com", 0,
                                             "Invalid"),
                         "Name is not a string")

    def test_addRecords_invEmail(self):
        self.assertEqual(directory.addRecord("Invalid", 5, 0, "Invalid"),
                         "Email is not a string")

    def test_addRecords_invAge(self):
        self.assertEqual(directory.addRecord("Invalid", "invalid@mail.com",
                                             "Invalid", "Invalid"),
                         "Age is not an int")

    def test_addRecords_invCountry(self):
        self.assertEqual(directory.addRecord("Invalid", "invalid@mail.com", 0,
                                             0),
                         "Country is not a string")

    def test_deleteRecords_invName(self):
        self.assertEqual(directory.deleteRecord(5, "invalid@mail.com", 0,
                                                "Invalid"),
                         "Name is not a string")

    def test_deleteRecords_invEmail(self):
        self.assertEqual(directory.deleteRecord("Invalid", 5, 0, "Invalid"),
                         "Email is not a string")

    def test_deleteRecords_invAge(self):
        self.assertEqual(directory.deleteRecord("Invalid",
                                                "invalid@mail.com", "Invalid",
                                                "Invalid"),
                         "Age is not an int")

    def test_deleteRecords_invCountry(self):
        self.assertEqual(directory.deleteRecord("Invalid",
                                                "invalid@mail.com", 0, 0),
                         "Country is not a string")

    def test_deleteRecords_notFound(self):
        self.assertEqual(directory.deleteRecord("notFound",
                                                "notFound@mail.com", 0,
                                                "NotFound"),
                         "Record not Found")

    def test_lookRecords_notFound(self):
        self.assertIsNone(directory.lookRecord("NotFound@mail.com", 0))

    # Performance


if __name__ == '__main__':
    unittest.main()
