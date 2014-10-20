__author__ = 'Ayla'


# Put the variables that the program needs to remember outside of functions. Make them global
first = ""
dob = ""
last=""
ss=""
zip=""
street= ""
city= ""
# remove the () after userschoice() because () is only used to call a function
def menu():
    while True:
        print("a. employee first name")
        print("b. employee last name")
        print("c. employee DOB")
        print("d. employee SS#")
        print("e. employee street address")
        print("f. employee city")
        print("g. employee zip")
        print("h. employee information")
        print("i. quit")
        userschoice = input("enter choice a, b, c, d, e, f, g, h, or i: ")
        if userschoice == "a" or userschoice == "b" or userschoice == "c" or userschoice == "d" or \
            userschoice == "e" or userschoice == "f" or userschoice == "g" or userschoice == "h" or userschoice == "i":
            return userschoice






def formatname(s):

    s=""

    return "s.capitalize():", s.capitalize()




def firstname():


    first=input('employee first name:')
    return first.capitalize()


def lastname():

    last=input('employee last name:')
    return last.capitalize()



def DOB():

    #date = input('Date (m/dd/yyyy): ')

    valid_choice = 0
    while not valid_choice:
        month = input('Month of birth ')
        if(int(month) >= 1 and int(month) <= 12):
            valid_choice = 1


    valid_choice=0
    while not valid_choice:
        day = input('Day of birth ')
        if(int(day)>=1 and int(day) <=31):
             valid_choice = 1


    valid_choice= 0
    while not valid_choice:
         year = input('Year of birth ')
         if(int(year) >=1990 and int(year)<=2014):
            valid_choice = 1



    date = month.strip() + "/" + day.strip() + "/" + year.strip()

    return date



def securitynumber():

    #securitynumber = input('employee SS# XXX-XXX-XXXX: ')


    valid_choice = 0

    while not valid_choice:

        two = input('first two numbers ')
        if len(two)== 2:
            valid_choice = 1


    valid_choice=0

    while not valid_choice:
        three = input('next three numbers ')
        if len(three)== 3:
             valid_choice = 1


    valid_choice= 0

    while not valid_choice:
            four = input('last four numbers ' )
            if len(four) == 4:
                 valid_choice = 1

    securitynumber = two.strip() + "-" + three.strip() + "-" + four.strip()

    return securitynumber



def streetname():

   #address=input("employee street address:" )

   valid_choice = 0
   while not valid_choice:
       number = input("house number: ")
       if int(number) > 0:
            valid_choice = 1



   valid_choice= 0
   while not valid_choice:
    name = input('street name ')
    if len(name)>= 1:
            valid_choice = 1


    address=number.strip() + " " + name.strip()

    return address


def cityname():
    cityname=input("employee city: ")

    return cityname


def zipcode():
    zipcode=input("employee zipcode: xxxxx")
    return zipcode





# I used printAll() instead of print() because of confusion with the built in print() function
# Note that because first is defined globally its value is available to this function.
def printAll():
    print('first name: ' + first )
    print('last name: ' + last)
    print('date of birth: ' + dob)
    print('social security number: '+ ss)
    print('street address: ' + address)
    print('name of city: ' + city)
    print('zipcode: ' + zip)

userschoice = "0"
while not userschoice == 'i':
                userschoice = menu()
                if (userschoice == "a"): first = firstname()
                if (userschoice == "b"): last = lastname()
                if (userschoice == "c"): dob = DOB()
                if (userschoice == "d"): ss = securitynumber()
                if (userschoice == "e"): address = streetname()
                if (userschoice == "f"): city = cityname()
                if (userschoice == "g"): zip = zipcode()
                if (userschoice == "h"):  printAll()



printAll()

