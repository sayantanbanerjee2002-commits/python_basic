from datetime import datetime

def calculate_fine(issue_date, return_date, book_type, member_type):

    print("\n  --- Library Fine Calculator ---")
    print(f"Issue Date: {issue_date} | Return Date: {return_date}")
    print(f"Book Type: {book_type.title()} | Member Type: {member_type.title()}")

  
    due_periods = {"regular": 14, "reference": 7, "bestseller": 5}

    fine_rates = {"student": 0.50, "faculty": 0.75, "public": 1.00}

    fmt = "%Y-%m-%d"
    issue = datetime.strptime(issue_date, fmt)
    ret = datetime.strptime(return_date, fmt)

    total_days = (ret - issue).days
    due_days = due_periods.get(book_type.lower(), 14)
    overdue_days = total_days - due_days

    if overdue_days <= 0:
        print(" Book returned on time. No fine.")
        return 0

    
    rate = fine_rates.get(member_type.lower(), 1.00)
    fine = overdue_days * rate

    
    if book_type.lower() == "reference":
        fine *= 2

    
    print(f"Overdue by: {overdue_days} days")
    print(f"Fine Rate: ${rate:.2f} per day")
    print(f"Total Fine: ${fine:.2f}")

    return fine



calculate_fine("2024-01-01", "2024-01-20", "regular", "student")
calculate_fine("2024-01-05", "2024-01-20", "reference", "faculty")
calculate_fine("2024-02-01", "2024-02-10", "bestseller", "public")