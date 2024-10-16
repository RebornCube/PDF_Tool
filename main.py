import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pypdf import PdfWriter

# Initialize the GUI application
root = tk.Tk()
root.title("PDF Merger")
root.geometry("400x450")

# List to store selected PDF file paths
pdf_files = []
save_location = ""

# Function to merge files
def join_pdf(pdfs, save_path, filename):
    if not save_path or not filename:
        messagebox.showwarning("Missing Information", "Please select a save location and enter a file name.")
        return
    
    merger = PdfWriter()
    for pdf in pdfs:
        merger.append(pdf)

    # Save the merged PDF to the selected location with the entered filename
    output_path = f"{save_path}/{filename}.pdf"
    try:
        merger.write(output_path)
        merger.close()
        messagebox.showinfo("Success", f"File created: {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the file: {e}")

# Function to pick files
def pick_files():
    # Open file dialog to select multiple PDF files
    files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if files:
        pdf_files.extend(files)  # Add the selected files to the list
        update_listbox()         # Update the listbox display

# Function to pick the save location
def pick_save_location():
    global save_location
    save_location = filedialog.askdirectory()
    if save_location:
        save_location_label.config(text=f"Save Location: {save_location}")

# Function to update the listbox with the selected file paths
def update_listbox():
    listbox.delete(0, tk.END)  # Clear current listbox
    for file in pdf_files:
        listbox.insert(tk.END, file)  # Add files to the listbox

# Function to process the files
def process_files():
    if pdf_files and save_location and filename_entry.get():
        try:
            # Call the join_pdf function, passing the pdf list, save location, and file name
            join_pdf(pdf_files, save_location, filename_entry.get())
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Missing Information", "Please ensure files are selected, save location is chosen, and a file name is entered.")

# Add buttons and a listbox to the GUI
pick_button = tk.Button(root, text="Pick PDF Files", command=pick_files)
pick_button.pack(pady=10)

save_button = tk.Button(root, text="Save List", command=process_files)
save_button.pack(pady=10)

# Button to select save location
save_location_button = tk.Button(root, text="Pick Save Location", command=pick_save_location)
save_location_button.pack(pady=10)

# Label to display the selected save location
save_location_label = tk.Label(root, text="Save Location: Not selected")
save_location_label.pack(pady=10)

# Entry box for the user to input the desired file name
filename_entry = tk.Entry(root, width=40)
filename_entry.pack(pady=10)
filename_entry.insert(0, "Enter output file name")  # Placeholder text

# New button to process the picked files
process_button = tk.Button(root, text="Process Files", command=process_files)
process_button.pack(pady=10)

# Listbox to display selected PDF files
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()

