import random
import csv
users = []


def commit():
    with open('data.csv' , 'w' ,newline='') as f:
        writer = csv.writer(f)
        writer.writerows(users)
def add_user(username):
    users.append([username,0])
    commit()
def check_user(username):
    for i in users:
        if i[0] == username:
            return False
    return True
def sign_up(username):

    if check_user(username):
       

        add_user(username)
        

def read_users():
    with open('data.csv' , 'r' , newline='')as f :
        reader = csv.reader(f)
        return list(reader)
    

def game():
    random_int = random.randint(0,101)
    chance = 0

    while True:
        input_usr = int(input('enter your number : '))
        if random_int> input_usr:
            print('number is bigger')
            chance+=1
        elif random_int<input_usr:
            print('number is lower')
            chance+=1
        else:
            chance+=1
            print(f'you won number was {random_int} in {chance} time')

            break

def main():
    global users
    users = read_users()
    username = input('enter your name (username for game) : ')
    sign_up(username)
    # game()


if __name__ == "__main__":
    main()