import tkinter as tk
import os
from tkinter import ttk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

# Read receipt details from file
fo1 = open("recipt.txt", "r")
list1 = fo1.readlines()
# fo1.close()

# Clean data
# del list1[1:6]  # Remove unnecessary lines
# list1 = [line.strip() for line in list1]
del list1[1]
del list1[2]
del list1[3]
del list1[4]
del list1[5]
list1[0]=list1[0][:-1]
list1[1]=list1[1][:-1]
list1[2]=list1[2][:-1]
list1[3]=list1[3][:-1]
list1[4]=list1[4][:-1]

# Receipt details
name, address, mobile, room_no, total_bill = list1[0], list1[1], list1[2], list1[3], list1[4]

def print_receipt():
    # Create a folder named "Receipts" if it doesn't exist
    folder_name = "Receipts"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Generate a unique file name using the guest's name and current timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    pdf_file = os.path.join(folder_name, f"receipt_{name}_{timestamp}.pdf")

    c = canvas.Canvas(pdf_file, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 750, "5STAR HOTEL AND RESORTS")
    c.setFont("Helvetica", 12)
    c.drawString(220, 730, "Serving Guests Since 1998")
    c.line(50, 720, 550, 720)

    # Add receipt details
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 700, "Name:")
    c.setFont("Helvetica", 12)
    c.drawString(150, 700, name)

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 680, "Address:")
    c.setFont("Helvetica", 12)
    c.drawString(150, 680, address)

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 660, "Mobile No.:")
    c.setFont("Helvetica", 12)
    c.drawString(150, 660, mobile)

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 640, "Room No.:")
    c.setFont("Helvetica", 12)
    c.drawString(150, 640, room_no)

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 620, "Total Bill (Rs.):")
    c.setFont("Helvetica", 12)
    c.drawString(150, 620, total_bill)

    # Save PDF
    c.save()
    print(f"Receipt saved as {pdf_file}")

# GUI Window
root = tk.Tk()
root.geometry("600x600")
root.title("Hotel Receipt")
root.configure(background="#ffffff")

# Header Label
header_label = tk.Label(root, text="PROJECTWORLDS HOTEL AND RESORTS", font=("Arial", 18, "bold"), fg="#ffffff", bg="#3f51b5", pady=10)
header_label.pack(fill="x")

sub_header_label = tk.Label(root, text="Serving Guests Since 1998", font=("Arial", 14, "italic"), fg="#ffffff", bg="#3f51b5")
sub_header_label.pack(fill="x")

ttk.Separator(root, orient="horizontal").pack(fill="x", padx=10)

# Receipt Frame
frame = tk.Frame(root, bg="#ffffff")
frame.pack(pady=20)

def add_label(text, value, color):
    row = tk.Frame(frame, bg="#ffffff")
    row.pack(anchor="w", pady=5)
    tk.Label(row, text=text, font=("Arial", 12, "bold"), fg=color, bg="#ffffff").pack(side="left")
    tk.Label(row, text=value, font=("Arial", 12), fg="#333333", bg="#ffffff").pack(side="left", padx=10)

add_label("Name:", name, "#ff5733")
add_label("Address:", address, "#33aaff")
add_label("Mobile No.:", mobile, "#ff33aa")
add_label("Room No.:", room_no, "#33ffaa")
add_label("Total Bill (Rs.):", total_bill, "#ffaa33")

ttk.Separator(root, orient="horizontal").pack(fill="x", padx=10, pady=10)

# Print Button
print_button = tk.Button(root, text="Print Receipt", command=print_receipt, font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5)
print_button.pack(pady=10)

root.mainloop()
