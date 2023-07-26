def student_helper(student) -> dict:
    return {
        'id': str(student['_id']),
        'full_name': student['full_name'],
        'email': student['email'],
        'course_of_study': student['course_of_study'],
        'year': student['year'],
        'GPA': student['gpa']
    }

