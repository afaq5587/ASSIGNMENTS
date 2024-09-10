students_data = [
    {
        'name': 'John Doe',
        'marks': {
            'Math': 85,
            'English': 90,
            'Science': 78
        }
    },
    {
        'name': 'Jane Smith',
        'marks': {
            'Math': 75,
            'English': 82,
            'Science': 89
        }
    },
    {
        'name': 'Emily Davis',
        'marks': {
            'Math': 93,
            'English': 87,
            'Science': 85
        }
    },
    {
        'name': 'Michael Brown',
        'marks': {
            'Math': 65,
            'English': 70,
            'Science': 60
        }
    },
    {
        'name': 'Chris Johnson',
        'marks': {
            'Math': 88,
            'English': 85,
            'Science': 90
        }
    }
]

def grades(total):
    if total < 30:
        return "fail"
    elif 30 <= total < 45:
        return "E"
    elif 45 <= total < 55:
        return "D"
    elif 55 <= total < 65:
        return "C"
    elif 65 <= total < 75:
        return "B"
    elif 75 <= total <= 100:
        return "A"
    else:
        return "Invalid"

for student in students_data:
    sum = student["marks"]["Math"] + student["marks"]["English"] + student["marks"]["Science"]
    name = student["name"]
    total = sum * 100 / 300
    grade = grades(total)
   
    print(f"Dear {name}, your total marks are {sum} and your grade is {grade}. Keep it up!")
