from api import *
from sys import argv

secret=""
with open ("secret.txt", "r") as myfile:
    secret=myfile.readlines()[0]

code=""
with open ("simplejob.epl", "r") as myfile:
    code=myfile.read()

myacc = getAccountId(secret)
print "Resolved account id:",myacc
    
print "Creating Work:"
print "---------------------------"

# def createWork(secret, code, bounties_per_it, it, cappow, btyprice, powprice):
# secret = passphrase
# code = epl code
# bounties_per_it = number of bounties per run
# it = number of runs
# cappow = end after this many pow submissions
# btyprice = price paid per bounty
# powprice = price paid per pow

print "Result:",createWork(secret, code, 10, 1, 100, 1, 1)

