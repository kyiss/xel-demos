import requests
    
def get(url):
    r = requests.get(url)
    return r.json()

def getReq(type, args):
    url = "http://localhost:16876/nxt?requestType=" + type + "&" + args
    res =  get(url)
    return res

def postReq(type, args):
    r = requests.post("http://localhost:16876/nxt?requestType=" + type, args)
    return r.json()

def getAccountId(secret):
    res =  getReq("getAccountId","secretPhrase=" + secret)["account"]
    if "errorDescription" in res:
        return "ERROR: " + res["errorDescription"]
    else:
        return res

def getWork(account):
    res =  getReq("getWork","account=" + account)["work_packages"]
    if "errorDescription" in res:
        return "ERROR: " + res["errorDescription"]
    else:
        return res

def getWorkById(account, wid, id):
    res =  getReq("getWork","account=" + account + "&with_storage=true&storage_id=" + str(id) + "&work_id=" + str(wid) )["work_packages"]
    if "errorDescription" in res:
        return "ERROR: " + res["errorDescription"]
    else:
        return res

def cancelWork(secret, wid):
    res = postReq("cancelWork",{"secretPhrase":secret, "work_id":wid})
    if "errorDescription" in res:
        return res["errorDescription"]
    else:
        return res

def createWork(secret, code, bounties_per_it, it, cappow, btyprice, powprice):
    res = postReq("createWork",{"secretPhrase":secret,"source_code":code, "work_deadline":250, "xel_per_bounty":btyprice, "xel_per_pow":powprice, "bounty_limit_per_iteration":bounties_per_it, "cap_pow":cappow, "iterations":it})
    if "errorDescription" in res:
        return res["errorDescription"]
    else:
        return res