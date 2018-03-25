from api import *
secret=""
def pprinttable(rows):
  if len(rows) > 1:
    headers = rows[0]
    rows.pop(0)
    lens = []
    for i in range(len(rows[0])):
      lens.append(len(max([x[i] for x in rows] + [headers[i]],key=lambda x:len(str(x)))))
    formats = []
    hformats = []
    for i in range(len(rows[0])):
      if isinstance(rows[0][i], int):
        formats.append("%%%dd" % lens[i])
      else:
        formats.append("%%-%ds" % lens[i])
      hformats.append("%%-%ds" % lens[i])
    pattern = " | ".join(formats)
    hpattern = " | ".join(hformats)
    separator = "-+-".join(['-' * n for n in lens])
    print hpattern % tuple(headers)
    print separator
    _u = lambda t: t.decode('UTF-8', 'replace') if isinstance(t, str) else t
    for line in rows:
        print pattern % tuple(_u(t) for t in line)
  elif len(rows) == 1:
    row = rows[0]
    hwidth = len(max(row._fields,key=lambda x: len(x)))
    for i in range(len(row)):
      print "%*s = %s" % (hwidth,row._fields[i],row[i])
with open ("secret.txt", "r") as myfile:
    secret=myfile.readlines()[0]

myacc = getAccountId(secret)
print "Resolved account id:",myacc
    
print "Here are your workpackages:"
print "---------------------------"

table = []
table.append(["id", "active", "#pow","of","#bty","of","iteration","of","time out in"])

wp = getWork(myacc)
for x in wp:
    act = "ACTIVE"
    timeout = "n/a"
    if x["closed"]:
        act = "CLOSED"
    else:
        timeout = str(x["max_closing_height"]-x["work_at_height"]) + " blks"
    
    table.append([str(x["id"]), act, str(x["received_pows"]),str(x["cap_number_pow"]),str(x["received_bounties"]),str(x["iterations"]*x["bounty_limit_per_iteration"]),str(x["iterations"]-x["iterations_left"]),str(x["iterations"]),timeout])
print ""
pprinttable(table)