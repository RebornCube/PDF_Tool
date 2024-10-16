import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pypdf import PdfWriter

# Initialize the GUI application
root = tk.Tk()
root.title("PDF Merger")
root.geometry("600x500")

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
        update_textbox()         # Update the textbox display

# Function to pick the save location
def pick_save_location():
    global save_location
    save_location = filedialog.askdirectory()
    if save_location:
        save_location_label.config(text=f"Save Location: {save_location}")

# Function to update the textbox with the selected file paths
def update_textbox():
    textbox.delete(1.0, tk.END)  # Clear current textbox
    for file in pdf_files:
        textbox.insert(tk.END, file + "\n")  # Add files to the textbox with line breaks

# Function to move the selected file up in the list
def move_up():
    try:
        selected_idx = textbox.index(tk.SEL_FIRST).split(".")[0]
        selected_idx = int(selected_idx) - 1  # Convert to 0-based index
        if selected_idx > 0:
            pdf_files[selected_idx], pdf_files[selected_idx - 1] = pdf_files[selected_idx - 1], pdf_files[selected_idx]
            update_textbox()
            textbox.tag_remove(tk.SEL, 1.0, tk.END)  # Clear selection
    except:
        messagebox.showwarning("Select File", "Please select a file to move.")

# Function to move the selected file down in the list
def move_down():
    try:
        selected_idx = textbox.index(tk.SEL_FIRST).split(".")[0]
        selected_idx = int(selected_idx) - 1  # Convert to 0-based index
        if selected_idx < len(pdf_files) - 1:
            pdf_files[selected_idx], pdf_files[selected_idx + 1] = pdf_files[selected_idx + 1], pdf_files[selected_idx]
            update_textbox()
            textbox.tag_remove(tk.SEL, 1.0, tk.END)  # Clear selection
    except:
        messagebox.showwarning("Select File", "Please select a file to move.")

# Function to clear the textbox and the pdf_files list
def clear_files():
    pdf_files.clear()  # Clear the list of PDF files
    textbox.delete(1.0, tk.END)  # Clear the textbox display

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

# Add buttons and a textbox to the GUI
pick_button = tk.Button(root, text="Pick PDF Files", command=pick_files)
pick_button.pack(pady=10)

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

# Create a frame to hold the textbox and scrollbar
frame = tk.Frame(root)
frame.pack(pady=20)

# Add a vertical scrollbar to the frame
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Textbox to display selected PDF files with text wrapping
textbox = tk.Text(frame, width=70, height=10, wrap='word', yscrollcommand=scrollbar.set)
textbox.pack(side=tk.LEFT)

# Configure scrollbar to scroll the textbox
scrollbar.config(command=textbox.yview)

# Create a frame to hold the Move Up and Move Down buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

# Buttons to move selected file up and down (side by side in the button_frame)
move_up_button = tk.Button(button_frame, text="Move Up", command=move_up)
move_up_button.pack(side=tk.LEFT, padx=10)

move_down_button = tk.Button(button_frame, text="Move Down", command=move_down)
move_down_button.pack(side=tk.LEFT, padx=10)

# Button to clear the textbox and the file list
clear_button = tk.Button(root, text="Clear List", command=clear_files)
clear_button.pack(pady=5)

# New button to process the picked files
process_button = tk.Button(root, text="Process Files", command=process_files)
process_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
