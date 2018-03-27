from api import *
from sys import argv

wid=long(argv[1])

secret=""
with open ("secret.txt", "r") as myfile:
    secret=myfile.readlines()[0].strip()

myacc = getAccountId(secret)
print "Resolved account id:",myacc
    
print "Cancelling Work:"
print "---------------------------"
print "ID:",wid
print "Result:",cancelWork(secret,wid) 


