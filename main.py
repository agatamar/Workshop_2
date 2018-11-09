from models import User
from db_connection import get_connection



if __name__=='__main__':
    cnx=get_connection()
    if cnx:
        cursor=cnx.cursor()
        # u = User()
        # u.set_hashed_password("dziendobry")
        # u.email = "eopl@e1.pl"
        # u.username = "Elfi"
        # print(u.hashed_password)
        #
        # u.save_to_db(cursor)
        # print(u.id)
        # cnx.commit()
        #
        # u2 = User()
        # u2.set_hashed_password("dziendobry")
        # u2.email = "b113@b.pl"
        # u2.username = "Bob311"
        # print(u2.hashed_password)
        #
        # u2.save_to_db(cursor)
        # print(u2.id)
        # cnx.commit()

        u3=User.load_user_by_id(cursor,user_id=2)
        u3.email="wypas@wp.pl"
        u3.save_to_db(cursor)
        cnx.commit()
        u=User.load_user_by_id(cursor,user_id=11)
        u.delete(cursor)
        cnx.commit()
        print(u3)
        print("--------------------------------------")
        lista_uzytkownikow=User.load_all_users(cursor)
        for uzytkownik in lista_uzytkownikow:
            print(uzytkownik)

        cursor.close()
        cnx.close()
    else:
        print("Nieudane połaczenie")



# w konsoli
# virtualenv : source ~/virtualenv/module_1/bin/activate
# python user_management.py --help
# python user_management.py --u abc --p ppp
# python user_management.py -u abc -p bbb -n ccc -e
