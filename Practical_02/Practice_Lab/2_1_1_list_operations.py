# 2.1.1. List Operations (Menu-driven)

def main():
    my_list = []
    while True:
        print("1. Add")
        print("2. Remove")
        print("3. Display")
        print("4. Quit")
        choice = input("Enter choice: ")

        if choice == "1":
            try:
                val = int(input("Integer: "))
                my_list.append(val)
                print(f"List after adding: {my_list}")
            except ValueError:
                print("Invalid input")

        elif choice == "2":
            if not my_list:
                print("List is empty")
            else:
                try:
                    val = int(input("Integer: "))
                    if val in my_list:
                        my_list.remove(val)
                        print(f"List after removing: {my_list}")
                    else:
                        print("Element not found")
                except ValueError:
                    print("Invalid input")

        elif choice == "3":
            if not my_list:
                print("List is empty")
            else:
                print(my_list)

        elif choice == "4":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
