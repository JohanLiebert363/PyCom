import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
import sys
import io

class PythonCompilerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Code Runner")

        # Always dark mode
        self.root.config(bg="#181818")

        self.code_area = scrolledtext.ScrolledText(
            root, width=80, height=20, font=("Consolas", 12),
            fg="#d4d4d4", bg="#1e1e1e", insertbackground="#d4d4d4"
        )
        self.code_area.pack(padx=10, pady=10)

        self.run_button = tk.Button(
            root, text="Run Code", command=self.run_code,
            bg="#232323", fg="#d4d4d4", activebackground="#333", activeforeground="#fff"
        )
        self.save_button = tk.Button(
            root, text="Save Code", command=self.save_code,
            bg="#232323", fg="#d4d4d4", activebackground="#333", activeforeground="#fff"
        )
        self.save_button.pack(pady=5)
        self.run_button.pack(pady=5)

        self.output_area = scrolledtext.ScrolledText(
            root, width=80, height=10, font=("Consolas", 12),
            state='disabled', bg="#232323", fg="#00ff00"
        )
        self.output_area.pack(padx=10, pady=10)

    def run_code(self):
        code = self.code_area.get("1.0", tk.END)
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = io.StringIO()
        sys.stderr = sys.stdout
        try:
            exec(code, {})
        except Exception as e:
            print(f"Error: {e}")
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        self.output_area.config(state='normal')
        self.output_area.delete("1.0", tk.END)
        self.output_area.insert(tk.END, output)
        self.output_area.config(state='disabled')

    def save_code(self):
        code = self.code_area.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(
            defaultextension=".py",
            filetypes=[("Python Files", "*.py"), ("All Files", "*.*")]
        )
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(code)

if __name__ == "__main__":
    root = tk.Tk()
    app = PythonCompilerApp(root)
    root.mainloop()