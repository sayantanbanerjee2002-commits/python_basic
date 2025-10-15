def generate_email(first, last, dept, existing):
    import re
    base = f"{first}.{last}".replace(" ", "").replace("'", "").lower()
    email = f"{base}@company.com"
    if email in existing:
        email = f"{base}.{dept.lower()}@company.com"
    count = 2
    while email in existing:
        email = f"{base}.{dept.lower()}{count}@company.com"
        count += 1
    print(f"Generated Email: {email}")
    return email


existing = ["john.doe@company.com", "john.doe.sales@company.com"]
generate_email("John", "Doe", "Sales", existing)