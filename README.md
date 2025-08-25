# 📂 File Handling + Error Handling Assignment

This is a simple **Python program** that demonstrates file handling and error handling.  
It allows the user to enter a filename, read its contents, modify the text (convert to uppercase), and save the modified version into a **new file**.

---

## ✨ Features
- Reads file content safely.  
- Handles errors gracefully (e.g., file not found, permission denied).  
- Converts the file’s text to **uppercase**.  
- Saves the modified content into a new file with the prefix: `modified_`.  
- Always completes execution with a final message, whether successful or not.  

---

## 📖 How It Works
1. The program asks the user to input a filename.  
2. If the file exists, it reads the content and displays it.  
3. The content is converted to uppercase.  
4. A new file is created with the prefix `modified_` and the modified content is written to it.  
5. Errors (such as missing files) are caught and displayed without crashing the program.  

---

## 🛠️ Usage
1. Make sure you have **Python 3.x** installed.  
2. Save the program in a file, for example: `file_handler.py`.  
3. Run the program from your terminal:

```bash
python file_handler.py
