from api import *
secret=""
from sys import argv

wid=int(argv[1])
with open ("secret.txt", "r") as myfile:
    secret=myfile.readlines()[0]

myacc = getAccountId(secret)
print "Resolved account id:",myacc
    
print "Here here is your latest storage:"
print "---------------------------------"

table = []
table.append(["id", "active", "#pow","of","#bty","of","iteration","of","time out in"])

# def getWorkById(account, wid, id):
wp = getWorkById(myacc, wid, 0)[0]
print "Works ID:",wp["id"]
print "Works current height:",wp["work_at_height"]
print "Works storage size:",wp["storage_size"]
print "Works storage slot:",wp["storage_id"]
print "Works storage:\n",wp["storage"]
