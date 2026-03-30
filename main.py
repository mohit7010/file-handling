from pathlib import Path
import os 

def read_file_and_folder():
    path = Path('.')
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")

def createfile():
    try:
        read_file_and_folder()
        name = input("Enter file name: ")
        p = Path(name)

        if not p.exists():
            data = input("Enter content: ")
            p.write_text(data)
            print("File created successfully")
        else:
            print("File already exists")

    except Exception as err:
        print(f"Error: {err}")

def readfile():
    try:
        read_file_and_folder()
        name = input("Enter file name to read: ")
        p = Path(name)

        if p.exists() and p.is_file():
            print(p.read_text())
        else:
            print("File does not exist")

    except Exception as err:
        print(f"Error: {err}")

def updatefile():
    try:
        read_file_and_folder()
        name = input("Enter file name to update: ")
        p = Path(name)

        if p.exists() and p.is_file():
            print("1. Rename file")
            print("2. Overwrite file")
            print("3. Append to file")

            res = int(input("Choose option: "))

            if res == 1:
                new_name = input("Enter new file name: ")
                p.rename(new_name)

            elif res == 2:
                data = input("Enter new content: ")
                p.write_text(data)

            elif res == 3:
                data = input("Enter content to append: ")
                with open(p, 'a') as f:
                    f.write(" " + data)

    except Exception as err:
        print(f"Error: {err}")

def deletefile():
    try:
        read_file_and_folder()
        name = input("Enter file name to delete: ")
        p = Path(name)

        if p.exists() and p.is_file():
            p.unlink()
            print("File deleted successfully")
        else:
            print("File not found")

    except Exception as err:
        print(f"Error: {err}")

# Menu
print("1. Create file")
print("2. Read file")
print("3. Update file")
print("4. Delete file")

try:
    choice = int(input("Enter your choice: "))
except:
    print("Invalid input")
    exit()

if choice == 1:
    createfile()
elif choice == 2:
    readfile()
elif choice == 3:
    updatefile()
elif choice == 4:
    deletefile()
else:
    print("Invalid choice")