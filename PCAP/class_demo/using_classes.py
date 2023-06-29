from employee import Employee

file_name = "test_file.txt"

with open(file_name, "w") as file:
    (
        [
            "Kevin Bacon,kbacon@example.com,CEO,555-867-5309\n",
            "Bruce Wayne,bwayne@example.com,President,\n",
        ]
    )

employees = Employee.get_all(file_name)
