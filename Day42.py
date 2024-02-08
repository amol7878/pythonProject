

class Person:
    country = "india"
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayCountry(self):
        print(self.country)

    @classmethod
    def updateCountry(cls,uc):
        cls.country = uc

chinmay = Person("chinmay","deshpande")
amol = Person("amol","rao")
chinmay.displayCountry()


amol.displayCountry()
Person.updateCountry("bharat")
chinmay.displayCountry()
amol.displayCountry()

amol.country = "nepal"
chinmay.displayCountry()
amol.displayCountry()


class PersonB:
    count = 0
    def __init__ (self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        PersonB.count = PersonB.count + 1

    @staticmethod
    def numberOfObjects():
        return PersonB.count

amol1 = PersonB("amol","rao")
amol2 = PersonB("amolB","rao")
amol3 = PersonB("amolC","rao")
amol4 = PersonB("amolD","rao")

print(PersonB.numberOfObjects())

class PersonC:

    country ="india"

    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def  updateFirstName(self,fn):
        self.firstName = fn

    def updateLastName(self,ln):
        self.lastName = ln

amolR = PersonC("amolR","raoR")
amolR.updateLastName("dev")
amolR.updateFirstName("ram")

# instance // classmethod // staticmethod


















