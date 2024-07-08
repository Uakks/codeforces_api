import hashlib
import requests


def get(url):
    response = requests.get(url)
    return response.json()


def Sha512(txt):
    Hashed_link = hashlib.sha512(txt.encode()).hexdigest()
    return Hashed_link


def appending(choice, required, last_handle):
    if choice == 3:
        num = input("Choose submission count: ")
        required.append(f"count={num}")
    elif choice == 4:
        if last_handle != "":
            handle = input(f"Use {last_handle} as your handle? (Y/N): ")
            if handle != "Y" and handle != "y":
                handle = input(f"Enter your handle: ")
                with open("last_handle", "w") as f:
                    f.write(handle)
            else:
                handle = last_handle
        else:
            handle = input(f"Enter your handle: ")
            with open("last_handle", "w") as f:
                f.write(handle)
        required.append(f"handle={handle}")


def get_last_handle():
    with open("last_handle", "r") as f:
        last_handle = f.readline()
        return last_handle


def add_reqs(additional_link, required):
    for req in required:
        additional_link += req + "&"
    additional_link = additional_link[0:-1]
    return additional_link


def write_all(choice, data):
    if choice == 1:
        with open("list.json", "w") as f:
            f.write(data)
    elif choice == 2:
        with open("problemset.json", "w") as f:
            f.write(data)
    elif choice == 3:
        with open("stats.json", "w") as f:
            f.write(data)
    elif choice == 4:
        with open("user_status.json", "w") as f:
            f.write(data)
