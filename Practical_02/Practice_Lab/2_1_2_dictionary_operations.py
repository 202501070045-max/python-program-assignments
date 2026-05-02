# 2.1.2. Dictionary Operations

student = {
    1: "Amit",
    2: "Riya",
    3: "Kiran",
    4: "Neha",
    5: "Arjun",
    6: "Pooja",
    7: "Rahul",
    8: "Sneha",
    9: "Vikram",
    10: "Anjali"
}

def main():
    print(f"Original Dictionary: {student}")

    # Insertion
    try:
        insert_key = int(input())
        insert_value = input()
        student[insert_key] = insert_value
    except (ValueError, EOFError):
        pass
    print(f"After Insertion: {student}")

    # Update
    try:
        update_key = int(input())
        update_value = input()
        if update_key in student:
            student[update_key] = update_value
    except (ValueError, EOFError):
        pass
    print(f"After Update: {student}")

    # Deletion
    try:
        delete_key = int(input())
        if delete_key in student:
            del student[delete_key]
    except (ValueError, EOFError):
        pass
    print(f"After Deletion: {student}")

    # Traversal
    print("Traversing Dictionary:")
    for key, value in student.items():
        print(f"{key} : {value}")

if __name__ == "__main__":
    main()
