import os
import customtkinter as ctk
from tkinter import filedialog
import nltk
from collections import Counter
import string

# Download necessary NLTK data
nltk.download('punkt')

def list_directory_structure(startpath, indent=''):
    """
    Recursively lists the directory structure in a tree format.
    Displays the directory contents inside the GUI textbox.
    """
    files = sorted(os.listdir(startpath))
    for index, file in enumerate(files):
        path = os.path.join(startpath, file)
        is_last = index == len(files) - 1
        prefix = '└── ' if is_last else '├── '
        textbox.insert("end", indent + prefix + file + "\n")
        if os.path.isdir(path):
            extension = '    ' if is_last else '│   '
            list_directory_structure(path, indent + extension)

def extract_common_words(folder_path):
    """
    Extracts the most common words from file names in the selected folder.
    """
    words = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            filename = os.path.splitext(file)[0]  # Remove file extension
            filename = filename.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
            words.extend(nltk.word_tokenize(filename))  # Tokenize words
    common_words = Counter(words).most_common(15)  # Get the 15 most common words
    return common_words

def analyze_folder(folder_path):
    """
    Analyzes the folder structure and provides insights including:
    - Number of files and folders
    - File type distribution
    - Common words in file names
    - Suggestions for better organization
    """
    file_types = Counter()
    num_files = 0
    num_folders = 0
    empty_folders = 0
    duplicate_extensions = Counter()
    
    for root, dirs, files in os.walk(folder_path):
        num_folders += len(dirs)
        num_files += len(files)
        if not files and not dirs:
            empty_folders += 1  # Count empty folders
        
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            file_types[ext] += 1
            duplicate_extensions[file.lower()] += 1
    
    common_words = extract_common_words(folder_path)
    
    # Display analysis results
    analysis_textbox.configure(state="normal")
    analysis_textbox.delete("1.0", "end")
    analysis_textbox.insert("end", f"Total Folders: {num_folders}\n")
    analysis_textbox.insert("end", f"Total Files: {num_files}\n")
    analysis_textbox.insert("end", f"Empty Folders: {empty_folders}\n")
    analysis_textbox.insert("end", "File Type Distribution:\n")
    for ext, count in file_types.most_common():
        analysis_textbox.insert("end", f"{ext if ext else 'No Extension'}: {count}\n")
    
    # Display common words in file names
    analysis_textbox.insert("end", "\nCommon Words in File Names:\n")
    for word, count in common_words:
        analysis_textbox.insert("end", f"{word}: {count}\n")
    
    # Provide organizational suggestions based on analysis
    analysis_textbox.insert("end", "\nSuggestions:\n")
    if file_types['.txt'] > 10:
        analysis_textbox.insert("end", "You have many text files. Consider categorizing them into subfolders.\n")
    if file_types['.mp3'] > 5:
        analysis_textbox.insert("end", "Consider organizing audio files into separate folders.\n")
    if num_folders > num_files:
        analysis_textbox.insert("end", "You have more folders than files. Consider merging redundant folders.\n")
    if file_types['.png'] + file_types['.jpg'] + file_types['.jpeg'] > 10:
        analysis_textbox.insert("end", "Organize images into Screenshots, Photos, and Artwork folders.\n")
    if empty_folders > 0:
        analysis_textbox.insert("end", "Several empty folders found. Consider deleting them.\n")
    if any(count > 1 for count in duplicate_extensions.values()):
        analysis_textbox.insert("end", "Duplicate filenames detected. Consider renaming them.\n")
    
    analysis_textbox.configure(state="disabled")

def select_folder():
    """
    Opens a dialog box to select a folder and displays its structure.
    """
    folder_path = filedialog.askdirectory()
    if folder_path:
        textbox.configure(state="normal")
        textbox.delete("1.0", "end")
        textbox.insert("end", folder_path + "/\n")
        list_directory_structure(folder_path)
        textbox.configure(state="disabled")
        analyze_folder(folder_path)

# Initialize the main application window
app = ctk.CTk()
app.geometry("600x600")
app.title("Folder Structure & Analysis")
app.resizable(False, False)

# Create a frame to hold UI elements
frame = ctk.CTkFrame(app, width=580, height=580)
frame.pack(pady=10, padx=10, fill="both", expand=True)

# Textbox to display the directory structure
textbox = ctk.CTkTextbox(frame, width=560, height=250, state="disabled", border_width=2, corner_radius=10)
textbox.pack(pady=10, padx=10)

# Textbox to display analysis results
analysis_textbox = ctk.CTkTextbox(frame, width=560, height=250, state="disabled", border_width=2, corner_radius=10)
analysis_textbox.pack(pady=10, padx=10)

# Button to select a folder
button = ctk.CTkButton(frame, text="Select Folder", command=select_folder, height=40, width=200)
button.pack(pady=10)

# Run the main event loop
app.mainloop()
