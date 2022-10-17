users={
    'Admin': {'password': 1111},
    'User': {'password': 2222},
    'Guest': {'password': 3333}
}

login=str(input("Write your login: "))
password=int(input("Write your password: "))
login_confirm=False
password_confirm=False

def login_check(users_dict,login_acept):
    for i in users_dict:
        if i==login_acept:
            return True
    return False        

def password_check(users_dict,pas,login):
    for i in users_dict:
        if i == login:
            user_key=users_dict.get(login)
            password_key=user_key.get('password')
            if password_key==pas:
                return True
            else:
                return False

login_confirm=login_check(users,login)
password_confirm=password_check(users,password,login)

if login_confirm==False:
    print("Invalid login!!!")
elif password_confirm==False:
    print("Invalid password!!!")
else:
    print("Access is allowed!!!")