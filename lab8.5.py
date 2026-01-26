try:
    with open("example.txt", "r") as file:
        pass
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to access the file.")
except IOError:
    print("An I/O error occurred while accessing the file.")
except FileExistsError:
    print("File already exists and cannot be overwritten.")
except Exception as e:
    print("An unexpected error occurred:", e)
