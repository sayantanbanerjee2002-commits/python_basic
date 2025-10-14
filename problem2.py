import re

def check_password_strength(password):
    missing = []
    if len(password) < 8: missing.append("minimum 8 characters")
    if not re.search(r"[A-Z]", password): missing.append("uppercase letter")
    if not re.search(r"[a-z]", password): missing.append("lowercase letter")
    if not re.search(r"[0-9]", password): missing.append("digit")
    if not re.search(r"[@#$%&]", password): missing.append("special character")

    valid = len(missing) == 0
    if valid:
        strength = "Strong" if len(password) > 12 else "Medium"
    else:
        strength = "Weak"

    return {"valid": valid, "missing": missing, "strength": strength}



print(check_password_strength("Hello123"))
print(check_password_strength("Hello@123"))
print(check_password_strength("Hello@123World"))
print(check_password_strength("H1@w"))
print(check_password_strength("helloworld"))