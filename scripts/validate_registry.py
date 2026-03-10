import json

def validate_student(file):
    with open(file) as f:
        data = json.load(f)

    required = ["student_id","name"]

    for field in required:
        if field not in data:
            print("Missing field:", field)

    print("Validation complete")