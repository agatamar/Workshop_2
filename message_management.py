import argparse
from db_connection import get_connection
from models import User,Message
from clcrypto import check_password
import datetime

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username",  help="Username")
parser.add_argument("-p", "--password", help="User's pass")
parser.add_argument("-l", "--list", action="store_true", help="Users list")
parser.add_argument("-t", "--to", help="Set Email to")
parser.add_argument("-s", "--send", help="Send message")
args = parser.parse_args()
print(args)

cnx = get_connection()


# create table message (
# id serial,
# from_id int,
# to_id int,
# text text,
# creation_date timestamp,
# primary key(id),
# foreign key(from_id) references Users(id),
# foreign key(to_id) references Users(id)
# )

if cnx:
    cursor = cnx.cursor()
    if (args.username and args.password) and args.list:
        u = User.load_user_by_email(cursor, args.username)
        if check_password(args.password, u.hashed_password):
            print("The pass is correct")
            list_of_messages_to_user = []
            list_of_messages_to_user = Message.load_all_messages_for_user(cursor,u.id)
            for l in list_of_messages_to_user:
                print(l)
        else:
            print("Provided Username or password is incorrect")
    elif (args.username and args.password) and args.to and args.send:
        u = User.load_user_by_email(cursor, args.username)
        t = User.load_user_by_email(cursor,args.to)
        from_id=u.id
        to_id=t.id
        if check_password(args.password, u.hashed_password):
            if t:
                new = Message()
                new.to_id = to_id
                new.from_id=from_id
                new.text= args.send
                new.creation_date=datetime.datetime.now()
                new.save_to_db(cursor)
                cnx.commit()
            else:
                print("The reciepient does not exist ")
        else:
            print("Provided Username or password is incorrect")
    elif (args.username and args.password) and args.to and not args.send:
        print("The message has not been provided.")
    else:
        print("Please type the following command to check all available options:\n python3 message_management.py --help")


cursor.close()
cnx.close()




