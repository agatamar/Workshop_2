import argparse

from main import get_connection
from models import User
from clcrypto import check_password

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username",  help="Nazwa użyszkodnika")
parser.add_argument("-p",  help="Hasło użyszkodnika")
parser.add_argument("-n",  help="nowe hasło użytkownika")
parser.add_argument("-l",  help="lista użytkowników")
parser.add_argument("-d",  help="usuń użytkownika")
parser.add_argument("-e",  action="store_true", help="edycja użytkownika")
args = parser.parse_args()
print(args)

cnx = get_connection()

"""
Założono, że username i email to te same pole ponieważ, w treści zadania 
brakuje przełączników do przekazania adresu email.
"""

if cnx:
    cursor = cnx.cursor()
    if (args.username and args.p) and (not args.e and not args.d and not args.n):
        u = User.load_user_by_email(cursor, args.username)
        if u:
            raise Exception("Użyszkodnik istnieje")
        nowy = User()
        nowy.email = args.username
        nowy.set_hashed_password(args.p)
        nowy.username = args.username
        nowy.save_to_db(cursor)
        cnx.commit()
    elif args.username and args.p and args.e and args.n:
        u = User.load_user_by_username(cursor, args.username)
        if u and check_password(args.p, u.hashed_password):
            u.set_hashed_password(args.n)
            u.save_to_db(cursor)
            cnx.commit()
            print("udało się")
        else:
            print("nie udało się")
cursor.close()
cnx.close()