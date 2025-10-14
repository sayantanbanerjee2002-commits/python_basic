def generate_report(student):
    subjects = student["subjects"]
    avg = {s: sum(marks)/len(marks) for s, marks in subjects.items()}
    overall = sum(avg.values()) / len(avg)
    grade = "A" if overall >= 90 else "B" if overall >= 80 else "C" if overall >= 70 else "D" if overall >= 60 else "F"
    best = max(avg, key=avg.get)
    worst = min(avg, key=avg.get)
    needs = [s for s,a in avg.items() if a < 80]

    print(f"Student: {student['name']}")
    print(f"Average Marks: {avg}")
    print(f"Overall: {overall:.2f}%, Grade: {grade}")
    print(f"Best: {best}, Worst: {worst}")
    print("Needs improvement:", needs)
    return avg, overall, grade


student_data = {
    "name": "Debasish",
    "subjects": {
        "Math": [85, 90, 78, 92],
        "Science": [88, 85, 90, 87],
        "English": [75, 80, 82, 78]
    }
}
generate_report(student_data)