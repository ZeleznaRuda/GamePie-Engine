import os

def main():
    folder_path = os.path.dirname(os.path.abspath(__file__))
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    print("Use commands:")
    print("\tpython -m gamepie.commands.<command>\n")
    print("Commands list:")
    for f in files:
        name_without_ext = os.path.splitext(f)[0]
        print(f"\t- {name_without_ext}")

if __name__ == "__main__":
    main()
