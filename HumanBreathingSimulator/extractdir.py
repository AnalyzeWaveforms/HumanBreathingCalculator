import os

def display_directory_tree(path, level=0):
    if not os.path.exists(path):
        print(f"{path} does not exist.")
        return
    
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        
        if os.path.isdir(full_path):
            print(f"{'    ' * level}|__ {entry}/")
            display_directory_tree(full_path, level + 1)
        else:
            print(f"{'    ' * level}|__ {entry}")

# Replace 'your_directory_path' with the path to the directory you want to display
your_directory_path = r"C:\Users\Garage\OneDrive\Documents\HumanBreathingSimulator"
display_directory_tree(your_directory_path)
