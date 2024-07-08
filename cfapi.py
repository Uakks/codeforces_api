import datetime
import os
import random
import string
from data_get import *
from KEY_SEC import *
from main_ops import *

current_time = int(datetime.datetime.now().timestamp())
rand6 = ''.join(random.choices(string.digits + string.ascii_lowercase + string.ascii_uppercase, k=6))

print("Choose what you need: ")
choices = ["contest list:",
           "problems from problemset:",
           "problem status:",
           "user submissions:"]

for ch, i in enumerate(choices):
    print(i, ch + 1)
choice = int(input("Enter a number: "))

useful_requests = ["contest.list",
                   "problemset.problems",
                   "problemset.recentStatus",
                   "user.status"]

main_link = f"https://codeforces.com/api/{useful_requests[choice - 1]}"
additional_link = f"?"
apiSig = f"&apiSig={rand6}"
required = [f"apiKey={KEY}",
            f"time={current_time}"]

if os.path.exists("last_handle"):
    last_handle = get_last_handle()
else:
    last_handle = ""
appending(choice, required, last_handle)
required.sort()
additional_link = add_reqs(additional_link, required)

input("Press any key to continue...")

cod = Sha512(f"{rand6}/{useful_requests[choice - 1]}{additional_link}#{SECRET}")
main_link += additional_link + apiSig + cod

print(main_link)

data = json.dumps(get(main_link), indent=4)
retrieved = functionality(choice, data)
for r in retrieved[2]:
    print(r)

write_all(choice, data)

# I need only contestId, name, rating, tags, solved_cnt
