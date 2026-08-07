import time
history = []
def rate_limiter(max_calls):
    def decorator(func):
        calls = {}
        def wrapper(*args):
            nonlocal calls
            username = args[0]
            status = ""
            if username not in calls:
                calls[username] = 1
                status = "Accepted"
            if calls[username] > max_calls:
                print(f"Dear {username} your quota has expired for api call{func.__name__}, please try again later!\n")
                status = "Blocked"
                history.append({
                    "username" : username,
                    "api" : func.__name__,
                    "status" : status,
                    "time" : time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                })
                return
            print(f"Welcome \"{func(*args)}\"\nRemaining quota for api \"{func.__name__}\": {max_calls - calls[username]}\n")
            status = "Accepted"
            history.append({
                    "username" : username,
                    "api" : func.__name__,
                    "status" : status,
                "time" : time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                })
            calls[username] = calls[username] + 1
        return wrapper
    return decorator

@rate_limiter(4)
def login(username):
    return username

@rate_limiter(7)
def download_file(username):
    return username

@rate_limiter(10)
def upload_file(username):
    return username

def api_report(username,api,hist):
    accepted = 0
    blocked = 0
    for i in hist:
        if i["username"] == username and i["api"] == api:
            if i["status"] == "Accepted":
                accepted = accepted + 1
            if i["status"] == "Blocked":
                blocked = blocked + 1
    print("________________________API REPORT______________________________\n")
    print(f"                    Username : {username}\n")
    print(f"                         API : {api}\n")
    print(f"                    Accepted : {accepted}\n")
    print(f"                     Blocked : {blocked}\n")

login("Vimal")
login("Vimal")
login("Vimal")
login("Vimal")
login("Vimal")
login("Vimal")
login("Vimal")
login("Vimal")
login("Vimal")
login("Vimal")
login("Vimal")
login("Vimal")
login("Vimal")
login("Vimal")
login("Vimal")
login("Vimal")
login("Vimal")
login("Vimal")

download_file("Vimal")

login("Jansen")
login("Jansen")
login("Jansen")
login("Jansen")
login("Jansen")

api_report("Vimal","login",history)
api_report("Vimal","download_file",history)
api_report("Jansen","login",history)

print(history)
