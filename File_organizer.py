import os
import shutil

def organize_files(directory):
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    extensions = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.pptx', '.xlsx'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac'],
        'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
        'Code': ['.py', '.java', '.cpp', '.html', '.css', '.js'],
        'Others': []  # For files without a matching extension
    }

    for folder in extensions.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            moved = False
            for folder, exts in extensions.items():
                if any(file.lower().endswith(ext) for ext in exts):
                    shutil.move(file_path, os.path.join(directory, folder, file))
                    moved = True
                    break
            if not moved:  
                shutil.move(file_path, os.path.join(directory, 'Others', file))

    print(f"Files in '{directory}' have been organized.")

if __name__ == "__main__":
    target_directory = input("Enter the path of the directory to organize: ")
    organize_files(target_directory)
