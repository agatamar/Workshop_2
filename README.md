#### Console application that manages users and messages.

Technical requirements: Python 3.6, Argparse, please see requirements.txt

There are two main files:
1. user_management.py
2. message_management.py

To check what arguments are allowed, please type in the terminal:
python3 user_management.py -h
python3 message_management.py -h


Examples:
To create a new user, please type similar command to the below example:
python3 user_management.py -u agata -p agata
To edit existing user, please type similar command to the below example:
python3 user_management.py -u agata -p agata -e -n agata1
To delete existing user, please type similar command to the below example:
python3 user_management.py -u agata -p agata -d
To list all users:
python3 user_management.py -l

To send a message,please type similar command to the below example:
python3 message_management.py -u agata -p agata -t "eopl@e1.pl" -s "message"









