import tkinter as tk
from tkinter import ttk

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
    print("Printing receipt...")  # Placeholder for print functionality

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
