import string,  hashlib

def pwd_checker(pwd):
    suggestions = []
    score_lst = 0

    if len(pwd)>= 8:
        score_lst += 1
    else:
        suggestions.append("Password should be at least 8 character long")

    if any(x in string.ascii_uppercase for x in pwd):
        score_lst +=1
    else:
        suggestions.append("Password must containe one uppercase character")
    
    if any(y in string.ascii_lowercase for y in pwd):
        score_lst+=1
    else:
        suggestions.append("Passwrod must contain at least one lowercase character")

    if any(z in string.punctuation for z in pwd):
        score_lst+=1
        print(score_lst)
    else:
        suggestions.append("Passwrod must contain at least one special character!")
        print(suggestions)
        
        hashing = hashlib.sha3_256()
        hashing.update(pwd.encode("utf8"))
        final_hasing = hashing.hexdigest()
        print("Your password %s is stored in hash form %s, with %s point of strongness" %(pwd, final_hasing, score_lst))
        
by_user = input("Enter: ")
pwd_checker(by_user)


