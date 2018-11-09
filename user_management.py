import argparse
from db_connection import get_connection
from models import User
from clcrypto import check_password

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username",  help="Username")
parser.add_argument("-p", "--password", help="User's pass")
parser.add_argument("-n", "--new_pass",  help="New user's pass")
parser.add_argument("-l", "--list", action="store_true", help="Users list")
parser.add_argument("-d", "--delete", action="store_true", help="Delete user")
parser.add_argument("-e", "--edit", action="store_true", help="Edit user")
args = parser.parse_args()
print(args)

cnx = get_connection()

"""
Założono, że username i email to to samo pole ponieważ, w treści zadania 
brakuje przełączników do przekazania adresu email.
"""

if cnx:
    cursor = cnx.cursor()
    if (args.username and args.password) and (not args.edit and not args.delete and not args.new_pass):
        u = User.load_user_by_email(cursor, args.username)
        if u:
            print("User already exists")
        new = User()
        new.email = args.username
        new.set_hashed_password(args.password)
        new.username = args.username
        new.save_to_db(cursor)
        cnx.commit()
    elif args.username and args.password and args.edit and args.new_pass:
        u = User.load_user_by_username(cursor, args.username)
        if u and check_password(args.password, u.hashed_password):
            u.set_hashed_password(args.new_pass)
            u.save_to_db(cursor)
            cnx.commit()
            print("Password has been changed successfully")
        else:
            print("Password change has not succeeded")
    elif args.username and args.password and args.delete:
        u = User.load_user_by_username(cursor, args.username)
        if u and check_password(args.password,u.hashed_password):
            u.delete(cursor)
            cnx.commit()
        else:
            print("User doesn't exist or the typed pass was incorrect")
    elif args.list:
        list_of_users=[]
        list_of_users= User.load_all_users(cursor)
        for l in list_of_users:
            print(l)
    else:
        print("Please type: python3 user_management.py --help to check the available options")
cursor.close()
cnx.close()