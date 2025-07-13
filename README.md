How to Use:
Install PyInstaller
You can do this by running the following command in your terminal:

bash
Copy
Edit
pip install pyinstaller
Place this Python file in your desired directory.

Create the executable
Run the following command in the terminal (replace main.py with your filename):

bash
Copy
Edit
pyinstaller main.py --onefile --noconsole
Troubleshooting:
If it doesn't work:

Check if you're in the correct directory where the .py file is located.

Try using the full path to PyInstaller directly:

bash
Copy
Edit
"C:\Users\{YOUR_USER}\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\pyinstaller.exe" main.py --onefile --noconsole
Alternatives:
You can also run the script directly in Visual Studio Code.

Or ask an AI assistant for help if you're stuck.

⚠ Limitations:
This version cannot handle input() statements or import statements.

