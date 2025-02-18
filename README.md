# Folder Structure & Analysis

## Overview
This is a Python-based GUI application built using `customtkinter` that allows users to analyze the structure of a selected folder. The tool provides a hierarchical view of the folder's contents and performs an NLP-based analysis on file names using `nltk` to identify common words. Additionally, it gives insights into file types, empty folders, and suggests ways to organize the directory better.

## Features
- **Display Folder Structure:** A visual representation of folder contents.
- **File Type Distribution Analysis:** Categorizes and counts file types.
- **Common Word Extraction:** Uses `nltk` to find frequently used words in file names.
- **Duplicate File Detection:** Identifies duplicate filenames with different extensions.
- **Folder Organization Suggestions:** Provides tips to improve folder organization.

## Installation

### Prerequisites
Ensure you have Python installed (>= 3.7) and install the required dependencies using:

```bash
pip install customtkinter nltk
```

## Usage

1. Run the script:
   ```bash
   python main.py
   ```
2. Click the **"Select Folder"** button to choose a directory.
3. The application will analyze the folder and display results.
4. Review file type distribution, common words, and organization suggestions in the analysis box.

## Technologies Used
- **Python** - Core programming language
- **customtkinter** - For the GUI interface
- **nltk** - Natural Language Processing for file name analysis
- **os** - For file and directory handling
- **collections.Counter** - To count occurrences of file types and words

## Contributing
Feel free to fork this repository and submit pull requests for improvements!

---
**Author:** Vaibhav Pandey

