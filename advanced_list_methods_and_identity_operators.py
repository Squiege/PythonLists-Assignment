# Task 1

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

if "Alice" in submitted:
    print("Alice has submitted!")
    if "Alice" in attended:
        print("Alice has attended")
    else:
        print("Alice has not attended")
else:
    print("Alice has not submitted")