import re
#n=input('enter n value:')
data= "^[A-Za-z.]+[\._-]?[A-Z|a-z0-9.-_]+[@]\w+[.]\w{2,3}$"
def check(email):
    if (re.search(data,email)):
        print("valid email: ",email)
    else:
        print("invalid email",email)
if __name__ == '__main__':
    email = ".karunkumar@gmail.com"
    check(email)
    email="harsha@gmail.in"
    check(email)
    email="praveencsharpcorner@gmail.com"
    check(email)
    email="1jaga@gmail.com"
    check(email)
    email="kumar_Ka%run@gmail.com"
    check(email)
    email="my.ownsiteour-earth@gmail.com"
    check(email)