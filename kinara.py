from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample student data
students = [
    {"id": 1, "name": "John Doe", "total_marks": 80},
    {"id": 2, "name": "Jane Smith", "total_marks": 90},
    {"id": 3, "name": "Alice Johnson", "total_marks": 75},
    {"id": 4, "name": "Bob Williams", "total_marks": 85},
    {"id": 5, "name": "Emily Davis", "total_marks": 95},
    # Add more student records as needed
]

# Constants for pagination
PAGE_SIZE = 2

@app.route("/students", methods=["GET"])
def get_students():
    # Get pagination parameters from query string
    page = int(request.args.get("page", 1))
    start_index = (page - 1) * PAGE_SIZE
    end_index = start_index + PAGE_SIZE

    # Perform server-side filtering if filter criteria are provided
    filter_criteria = request.args.get("filter")
    if filter_criteria:
        filtered_students = []
        for student in students:
            # Perform filtering based on specific criteria (e.g., name)
            if filter_criteria.lower() in student["name"].lower():
                filtered_students.append(student)
        
        # Apply pagination to filtered results
        paginated_students = filtered_students[start_index:end_index]
        total_count = len(filtered_students)
    else:
        # Apply pagination to all students if no filter criteria are provided
        paginated_students = students[start_index:end_index]
        total_count = len(students)

    response = {
        "students": paginated_students,
        "total_count": total_count,
        "page": page,
        "page_size": PAGE_SIZE
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run()
