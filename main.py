import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Initialize the GUI application
root = tk.Tk()
root.title("PDF File Picker")
root.geometry("400x350")

# List to store selected PDF file paths
pdf_files = []

# Function to pick files
def pick_files():
    # Open file dialog to select multiple PDF files
    files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if files:
        pdf_files.extend(files)  # Add the selected files to the list
        update_listbox()         # Update the listbox display

# Function to update the listbox with the selected file paths
def update_listbox():
    listbox.delete(0, tk.END)  # Clear current listbox
    for file in pdf_files:
        listbox.insert(tk.END, file)  # Add files to the listbox

# Function to save the list of files
def save_list():
    if pdf_files:
        # Save the list or do something with it (e.g., print to console)
        print("Selected PDF files:")
        for file in pdf_files:
            print(file)
        messagebox.showinfo("Success", "Files saved!")
    else:
        messagebox.showwarning("No Files", "No PDF files selected!")

# Function to process the files
def process_files():
    if pdf_files:
        try:
            # Call your custom function to process the files
            your_processing_function(pdf_files)
            messagebox.showinfo("Success", "Files processed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("No Files", "No PDF files to process!")

# Dummy processing function (replace with your actual function)
def your_processing_function(file_list):
    # Example: print each file being processed
    print("Processing files...")
    for file in file_list:
        print(f"Processing: {file}")
    # Add your actual processing logic here

# Add buttons and a listbox to the GUI
pick_button = tk.Button(root, text="Pick PDF Files", command=pick_files)
pick_button.pack(pady=10)

save_button = tk.Button(root, text="Save List", command=save_list)
save_button.pack(pady=10)

# New button to process the picked files
process_button = tk.Button(root, text="Process Files", command=process_files)
process_button.pack(pady=10)

# Listbox to display selected PDF files
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
