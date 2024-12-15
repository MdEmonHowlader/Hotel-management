import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
\
FACEBOOK_BLUE = "#3b5998"

def insert_guest(guest_name, phone, email, address, id_proof):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hotel_management"
        )
        cursor = conn.cursor()
        query = '''INSERT INTO guests (guest_name, phone, email, address, id_proof) 
                   VALUES (%s, %s, %s, %s, %s)'''
        values = (guest_name, phone, email, address, id_proof)
        cursor.execute(query, values)
        conn.commit()
        messagebox.showinfo("Success", "Guest added successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        conn.close()


# GUI setup
def main_window():
    root = tk.Tk()
    root.title("Hotel Management System")
    root.geometry("1000x600")
    root.configure(bg="LightGray")

    # Heading
    tk.Label(root, text="Hotel Management System", font=("times new roman", 24, "bold"), bg="mediumaquamarine", fg="black").pack(pady=10)

    # Button frame
    button_frame = tk.Frame(root, bg="LightGray")
    button_frame.pack(pady=20)

    tk.Button(button_frame, text="Guest Management", font=("helvetica", 14), bg="DodgerBlue", fg="white", command=guest_management).grid(row=0, column=0, padx=10)
    tk.Button(button_frame, text="Room Management", font=("helvetica", 14), bg="DodgerBlue", fg="white", command=room_management).grid(row=0, column=1, padx=10)
    tk.Button(button_frame, text="Booking Management", font=("helvetica", 14), bg="DodgerBlue", fg="white", command=booking_management).grid(row=0, column=2, padx=10)
    tk.Button(button_frame, text="Staff Management", font=("helvetica", 14), bg="DodgerBlue", fg="white", command=staff_management).grid(row=0, column=3, padx=10)
    tk.Button(button_frame, text="Service Management", font=("helvetica", 14), bg="DodgerBlue", fg="white", command=service_management).grid(row=0, column=4, padx=10)

    root.mainloop()

# Individual management windows
def guest_management():
    def go_back():
        window.destroy()

    def save_guest():
        guest_name = entry_name.get()
        phone = entry_phone.get()
        email = entry_email.get()
        address = entry_address.get()
        id_proof = entry_id_proof.get()
        insert_guest(guest_name, phone, email, address, id_proof)
        show_guests()

    def delete_guest():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a guest to delete.")
            return
        guest_id = tree.item(selected_item)["values"][0]
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="hotel_management"
            )
            cursor = conn.cursor()
            query = '''DELETE FROM guests WHERE guest_id=%s'''
            cursor.execute(query, (guest_id,))
            conn.commit()
            messagebox.showinfo("Success", "Guest deleted successfully!")
            show_guests()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}")
        finally:
            conn.close()

    def show_guests():
        for row in tree.get_children():
            tree.delete(row)
        guests = fetch_guests()
        for guest in guests:
            tree.insert("", tk.END, values=guest)

    window = tk.Toplevel()
    window.title("Guest Management")
    window.geometry("900x600")
    window.configure(bg="LightGray")

    tk.Label(window, text="Guest Management", font=("times new roman", 20, "bold"), bg="mediumaquamarine", fg="black").pack(pady=10)

    # Input Fields
    tk.Label(window, text="Name", font=("helvetica", 14), bg="LightGray").place(x=50, y=80)
    entry_name = tk.Entry(window, font=("helvetica", 14))
    entry_name.place(x=200, y=80)

    tk.Label(window, text="Phone", font=("helvetica", 14), bg="LightGray").place(x=50, y=130)
    entry_phone = tk.Entry(window, font=("helvetica", 14))
    entry_phone.place(x=200, y=130)

    tk.Label(window, text="Email", font=("helvetica", 14), bg="LightGray").place(x=50, y=180)
    entry_email = tk.Entry(window, font=("helvetica", 14))
    entry_email.place(x=200, y=180)

    tk.Label(window, text="Address", font=("helvetica", 14), bg="LightGray").place(x=50, y=230)
    entry_address = tk.Entry(window, font=("helvetica", 14))
    entry_address.place(x=200, y=230)

    tk.Label(window, text="ID Proof", font=("helvetica", 14), bg="LightGray").place(x=50, y=280)
    entry_id_proof = tk.Entry(window, font=("helvetica", 14))
    entry_id_proof.place(x=200, y=280)

    # Buttons
    tk.Button(window, text="Save Guest", font=("helvetica", 14), bg="green3", fg="white", command=save_guest).place(x=50, y=350)
    tk.Button(window, text="Delete Guest", font=("helvetica", 14), bg="red", fg="white", command=delete_guest).place(x=200, y=350)
    tk.Button(window, text="Back", font=("helvetica", 14), bg="blue", fg="white", command=go_back).place(x=350, y=350)

    # Guest Table
    columns = ("guest_id", "guest_name", "phone", "email", "address", "id_proof")
    tree = ttk.Treeview(window, columns=columns, show="headings", height=10)
    tree.place(x=50, y=400, width=800)

    for col in columns:
        tree.heading(col, text=col.capitalize())
        tree.column(col, width=150)

    show_guests()

def fetch_guests():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hotel_management"
        )
        cursor = conn.cursor()
        query = '''SELECT * FROM guests'''
        cursor.execute(query)
        return cursor.fetchall()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")
    finally:
        conn.close()
    def save_guest():
        guest_name = entry_name.get()
        phone = entry_phone.get()
        email = entry_email.get()
        address = entry_address.get()
        id_proof = entry_id_proof.get()
        insert_guest(guest_name, phone, email, address, id_proof)

    window = tk.Toplevel()
    window.title("Guest Management")
    window.geometry("800x500")
    window.configure(bg="LightGray")

    tk.Label(window, text="Guest Management", font=("times new roman", 20, "bold"), bg="mediumaquamarine", fg="black").pack(pady=10)

    # Input Fields
    tk.Label(window, text="Name", font=("helvetica", 14), bg="LightGray").place(x=50, y=80)
    entry_name = tk.Entry(window, font=("helvetica", 14))
    entry_name.place(x=200, y=80)

    tk.Label(window, text="Phone", font=("helvetica", 14), bg="LightGray").place(x=50, y=130)
    entry_phone = tk.Entry(window, font=("helvetica", 14))
    entry_phone.place(x=200, y=130)

    tk.Label(window, text="Email", font=("helvetica", 14), bg="LightGray").place(x=50, y=180)
    entry_email = tk.Entry(window, font=("helvetica", 14))
    entry_email.place(x=200, y=180)

    tk.Label(window, text="Address", font=("helvetica", 14), bg="LightGray").place(x=50, y=230)
    entry_address = tk.Entry(window, font=("helvetica", 14))
    entry_address.place(x=200, y=230)

    tk.Label(window, text="ID Proof", font=("helvetica", 14), bg="LightGray").place(x=50, y=280)
    entry_id_proof = tk.Entry(window, font=("helvetica", 14))
    entry_id_proof.place(x=200, y=280)

    # Save Button
    tk.Button(window, text="Save Guest", font=("helvetica", 14), bg="green3", fg="white", command=save_guest).place(x=200, y=350)

    # Additional implementation for guest management will go here


def room_management():
    def go_back():
        window.destroy()
        
    def save_room():
        room_data = {
            "room_type": entry_type.get(),
            "availability": entry_availability.get(),
            "price": float(entry_price.get()),
            "capacity": int(entry_capacity.get())
        }
        manage_rooms("add", data=room_data)
        show_rooms()

    def delete_room():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a room to delete.")
            return
        room_id = tree.item(selected_item)["values"][0]
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="hotel_management"
            )
            cursor = conn.cursor()
            query = '''DELETE FROM rooms WHERE room_id=%s'''
            cursor.execute(query, (room_id,))
            conn.commit()
            messagebox.showinfo("Success", "Room deleted successfully!")
            show_rooms()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}")
        finally:
            conn.close()

    def show_rooms():
        for row in tree.get_children():
            tree.delete(row)
        rooms = manage_rooms("show")
        for room in rooms:
            tree.insert("", tk.END, values=room)

    window = tk.Toplevel()
    window.title("Room Management")
    window.geometry("900x600")
    window.configure(bg="LightGray")

    tk.Label(window, text="Room Management", font=("times new roman", 20, "bold"), bg="mediumaquamarine", fg="black").pack(pady=10)

    # Input Fields
    tk.Label(window, text="Room ID", font=("helvetica", 14), bg="LightGray").place(x=50, y=80)
    entry_room_id = tk.Entry(window, font=("helvetica", 14))
    entry_room_id.place(x=200, y=80)

    tk.Label(window, text="Room Type", font=("helvetica", 14), bg="LightGray").place(x=50, y=130)
    entry_type = tk.Entry(window, font=("helvetica", 14))
    entry_type.place(x=200, y=130)

    tk.Label(window, text="Availability", font=("helvetica", 14), bg="LightGray").place(x=50, y=180)
    entry_availability = tk.Entry(window, font=("helvetica", 14))
    entry_availability.place(x=200, y=180)

    tk.Label(window, text="Price", font=("helvetica", 14), bg="LightGray").place(x=50, y=230)
    entry_price = tk.Entry(window, font=("helvetica", 14))
    entry_price.place(x=200, y=230)

    tk.Label(window, text="Capacity", font=("helvetica", 14), bg="LightGray").place(x=50, y=280)
    entry_capacity = tk.Entry(window, font=("helvetica", 14))
    entry_capacity.place(x=200, y=280)

    # Buttons
    tk.Button(window, text="Save Room", font=("helvetica", 14), bg="green3", fg="white", command=save_room).place(x=50, y=350)
    tk.Button(window, text="Delete Guest", font=("helvetica", 14), bg="red", fg="white", command=delete_room).place(x=200, y=350)
    tk.Button(window, text="Back", font=("helvetica", 14), bg="blue", fg="white", command=go_back).place(x=350, y=350)

    # Room Table
    columns = ("room_id", "room_type", "availability", "price", "capacity")
    tree = ttk.Treeview(window, columns=columns, show="headings", height=10)
    tree.place(x=50, y=400, width=800)

    for col in columns:
        tree.heading(col, text=col.capitalize())
        tree.column(col, width=150)
    show_rooms()
def booking_management():
    def go_back():
        window.destroy()
    def save_booking():
        booking_data = {
            "guest_id": entry_guest_id.get(),
            "room_id": entry_room_id.get(),
            "check_in": entry_check_in.get(),
            "check_out": entry_check_out.get()
        }
        manage_bookings("add", data=booking_data)
        show_bookings()
    def delete_booking():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a booking to delete.")
            return
        booking_id = tree.item(selected_item)["values"][0]
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="hotel_management"
            )
            cursor = conn.cursor()
            query = '''DELETE FROM bookings WHERE booking_id=%s'''
            cursor.execute(query, (booking_id,))
            conn.commit()
            messagebox.showinfo("Success", "Booking deleted successfully!")
            show_bookings()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}")
        finally:
            conn.close()
        

    def show_bookings():
        for row in tree.get_children():
            tree.delete(row)
        bookings = manage_bookings("show")
        for booking in bookings:
            tree.insert("", tk.END, values=booking)

    window = tk.Toplevel()
    window.title("Booking Management")
    window.geometry("900x600")
    window.configure(bg="LightGray")

    tk.Label(window, text="Booking Management", font=("times new roman", 20, "bold"), bg="mediumaquamarine", fg="black").pack(pady=10)

    # Input Fields
    tk.Label(window, text="Booking ID", font=("helvetica", 14), bg="LightGray").place(x=50, y=80)
    entry_booking_id = tk.Entry(window, font=("helvetica", 14))
    entry_booking_id.place(x=200, y=80)

    tk.Label(window, text="Guest ID", font=("helvetica", 14), bg="LightGray").place(x=50, y=130)
    entry_guest_id = tk.Entry(window, font=("helvetica", 14))
    entry_guest_id.place(x=200, y=130)

    tk.Label(window, text="Room ID", font=("helvetica", 14), bg="LightGray").place(x=50, y=180)
    entry_room_id = tk.Entry(window, font=("helvetica", 14))
    entry_room_id.place(x=200, y=180)

    tk.Label(window, text="Check-in Date", font=("helvetica", 14), bg="LightGray").place(x=50, y=230)
    entry_check_in = tk.Entry(window, font=("helvetica", 14))
    entry_check_in.place(x=200, y=230)

    tk.Label(window, text="Check-out Date", font=("helvetica", 14), bg="LightGray").place(x=50, y=280)
    entry_check_out = tk.Entry(window, font=("helvetica", 14))
    entry_check_out.place(x=200, y=280)

    # Buttons


    tk.Button(window, text="Save Room", font=("helvetica", 14), bg="green3", fg="white", command=save_booking).place(x=50, y=350)
    tk.Button(window, text="Delete Guest", font=("helvetica", 14), bg="red", fg="white", command=delete_booking).place(x=200, y=350)
    tk.Button(window, text="Back", font=("helvetica", 14), bg="blue", fg="white", command=go_back).place(x=350, y=350)

    # Booking Table
    columns = ("booking_id", "guest_id", "room_id", "check_in", "check_out")
    tree = ttk.Treeview(window, columns=columns, show="headings", height=10)
    tree.place(x=50, y=400, width=800)

    for col in columns:
        tree.heading(col, text=col.capitalize())
        tree.column(col, width=150)

    show_bookings()
    window = tk.Toplevel()
    window.title("Booking Management")
    window.geometry("800x500")
    window.configure(bg="LightGray")
    tk.Label(window, text="Booking Management", font=("times new roman", 20, "bold"), bg="mediumaquamarine", fg="black").pack(pady=10)
    # Additional implementation for booking management will go here

def manage_bookings(action, data=None, booking_id=None):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hotel_management"
        )
        cursor = conn.cursor()

        if action == "add":
            if not data:
                messagebox.showerror("Error", "Data is required for adding a booking!")
                return
            query = '''INSERT INTO bookings (guest_id, room_id, check_in, check_out) 
                       VALUES (%s, %s, %s, %s)'''
            values = (data["guest_id"], data["room_id"], data["check_in"], data["check_out"])
            cursor.execute(query, values)

        elif action == "update":
            if not booking_id or not data:
                messagebox.showerror("Error", "Booking ID and data are required for updating!")
                return
            query = '''UPDATE bookings SET guest_id=%s, room_id=%s, check_in=%s, check_out=%s 
                       WHERE booking_id=%s'''
            values = (data["guest_id"], data["room_id"], data["check_in"], data["check_out"], booking_id)
            cursor.execute(query, values)

        elif action == "delete":
            if not booking_id:
                messagebox.showerror("Error", "Booking ID is required for deletion!")
                return
            query = '''DELETE FROM bookings WHERE booking_id=%s'''
            cursor.execute(query, (booking_id,))

        elif action == "show":
            query = '''SELECT * FROM bookings'''
            cursor.execute(query)
            return cursor.fetchall()

        conn.commit()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")
    finally:
        conn.close()

def staff_management():
    def go_back():
        window.destroy()
    def save_staff():
        staff_data = {
        "name": entry_name.get(),
        "position": entry_position.get(),
        "phone": entry_phone.get(),
        "email": entry_email.get()[:50]  # Limit email length to 50 characters
    }
        manage_staff("add", data=staff_data)
        show_staff()

    def delete_staff():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a staff member to delete.")
            return
        staff_id = tree.item(selected_item)["values"][0]
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="hotel_management"
            )
            cursor = conn.cursor()
            query = '''DELETE FROM staff WHERE staff_id=%s'''
            cursor.execute(query, (staff_id,))
            conn.commit()
            messagebox.showinfo("Success", "Staff member deleted successfully!")
            show_staff()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}")
        finally:
            conn.close()
     

    def show_staff():
        for row in tree.get_children():
            tree.delete(row)
        staff = manage_staff("show")
        for member in staff:
            tree.insert("", tk.END, values=member)

    window = tk.Toplevel()
    window.title("Staff Management")
    window.geometry("900x600")
    window.configure(bg="LightGray")

    tk.Label(window, text="Staff Management", font=("times new roman", 20, "bold"), bg="mediumaquamarine", fg="black").pack(pady=10)

    # Input Fields
    tk.Label(window, text="Staff ID", font=("helvetica", 14), bg="LightGray").place(x=50, y=80)
    entry_staff_id = tk.Entry(window, font=("helvetica", 14))
    entry_staff_id.place(x=200, y=80)

    tk.Label(window, text="Name", font=("helvetica", 14), bg="LightGray").place(x=50, y=130)
    entry_name = tk.Entry(window, font=("helvetica", 14))
    entry_name.place(x=200, y=130)

    tk.Label(window, text="Position", font=("helvetica", 14), bg="LightGray").place(x=50, y=180)
    entry_position = tk.Entry(window, font=("helvetica", 14))
    entry_position.place(x=200, y=180)

    tk.Label(window, text="Phone", font=("helvetica", 14), bg="LightGray").place(x=50, y=230)
    entry_phone = tk.Entry(window, font=("helvetica", 14))
    entry_phone.place(x=200, y=230)

    tk.Label(window, text="Email", font=("helvetica", 14), bg="LightGray").place(x=50, y=280)
    entry_email = tk.Entry(window, font=("helvetica", 14))
    entry_email.place(x=200, y=280)

    # Buttons
    tk.Button(window, text="Save Room", font=("helvetica", 14), bg="green3", fg="white", command=save_staff).place(x=50, y=350)
    tk.Button(window, text="Delete Guest", font=("helvetica", 14), bg="red", fg="white", command=delete_staff).place(x=200, y=350)
    tk.Button(window, text="Back", font=("helvetica", 14), bg="blue", fg="white", command=go_back).place(x=350, y=350)


    # Staff Table
    columns = ("staff_id", "name", "position", "phone", "email")
    tree = ttk.Treeview(window, columns=columns, show="headings", height=10)
    tree.place(x=50, y=400, width=800)

    for col in columns:
        tree.heading(col, text=col.capitalize())
        tree.column(col, width=150)

    show_staff()

def manage_staff(action, data=None, staff_id=None):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hotel_management"
        )
        cursor = conn.cursor()

        if action == "add":
            if not data:
                messagebox.showerror("Error", "Data is required for adding staff!")
                return
            query = '''INSERT INTO staff (name, position, phone, email) 
           VALUES (%s, %s, %s, %s)'''

            values = (data["name"], data["position"], data["phone"], data["email"])
            cursor.execute(query, values)

        elif action == "update":
            if not staff_id or not data:
                messagebox.showerror("Error", "Staff ID and data are required for updating!")
                return
            query = '''UPDATE staff SET name=%s, position=%s, phone=%s, email=%s 
                       WHERE staff_id=%s'''
            values = (data["name"], data["position"], data["phone"], data["email"], staff_id)
            cursor.execute(query, values)

        elif action == "delete":
            if not staff_id:
                messagebox.showerror("Error", "Staff ID is required for deletion!")
                return
            query = '''DELETE FROM staff WHERE staff_id=%s'''
            cursor.execute(query, (staff_id,))

        elif action == "show":
            query = '''SELECT * FROM staff'''
            cursor.execute(query)
            return cursor.fetchall()

        conn.commit()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")
    finally:
        conn.close()

def service_management():
    def go_back():
        window.destroy()
    def save_service():
        service_data = {
            "service_name": entry_name.get(),
            "description": entry_description.get(),
            "price": float(entry_price.get())
        }
        manage_services("add", data=service_data)
        show_services()

    def delete_service():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a service to delete.")
            return
        service_id = tree.item(selected_item)["values"][0]
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="hotel_management"
            )
            cursor = conn.cursor()
            query = '''DELETE FROM services WHERE service_id=%s'''
            cursor.execute(query, (service_id,))
            conn.commit()
            messagebox.showinfo("Success", "Service deleted successfully!")
            show_services()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}")
        finally:
            conn.close()

    def show_services():
        for row in tree.get_children():
            tree.delete(row)
        services = manage_services("show")
        for service in services:
            tree.insert("", tk.END, values=service)

    window = tk.Toplevel()
    window.title("Service Management")
    window.geometry("900x600")
    window.configure(bg="LightGray")

    tk.Label(window, text="Service Management", font=("times new roman", 20, "bold"), bg="mediumaquamarine", fg="black").pack(pady=10)

    # Input Fields
    tk.Label(window, text="Service ID", font=("helvetica", 14), bg="LightGray").place(x=50, y=80)
    entry_service_id = tk.Entry(window, font=("helvetica", 14))
    entry_service_id.place(x=200, y=80)

    tk.Label(window, text="Service Name", font=("helvetica", 14), bg="LightGray").place(x=50, y=130)
    entry_name = tk.Entry(window, font=("helvetica", 14))
    entry_name.place(x=200, y=130)

    tk.Label(window, text="Description", font=("helvetica", 14), bg="LightGray").place(x=50, y=180)
    entry_description = tk.Entry(window, font=("helvetica", 14))
    entry_description.place(x=200, y=180)

    tk.Label(window, text="Price", font=("helvetica", 14), bg="LightGray").place(x=50, y=230)
    entry_price = tk.Entry(window, font=("helvetica", 14))
    entry_price.place(x=200, y=230)

    # Buttons
    tk.Button(window, text="Save Service", font=("helvetica", 14), bg="green3", fg="white", command=save_service).place(x=50, y=350)
    tk.Button(window, text="Delete Service", font=("helvetica", 14), bg="red", fg="white", command=delete_service).place(x=350, y=350)
    tk.Button(window, text="Back", font=("helvetica", 14), bg="blue", fg="white", command=go_back).place(x=500, y=350)

    # Service Table
    columns = ("service_id", "service_name", "description", "price")
    tree = ttk.Treeview(window, columns=columns, show="headings", height=10)
    tree.place(x=50, y=400, width=800)

    for col in columns:
        tree.heading(col, text=col.capitalize())
        tree.column(col, width=150)

    show_services()

def manage_services(action, data=None, service_id=None):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hotel_management"
        )
        cursor = conn.cursor()
        if action == "add":
            if not data:
                messagebox.showerror("Error", "Data is required for adding a service!")
                return
            query = '''INSERT INTO services (service_name, description, price) 
                       VALUES (%s, %s, %s)'''
            values = (data["service_name"], data["description"], data["price"])
            cursor.execute(query, values)

        elif action == "update":
            if not service_id or not data:
                messagebox.showerror("Error", "Service ID and data are required for updating!")
                return
            query = '''UPDATE services SET service_name=%s, description=%s, price=%s 
                       WHERE service_id=%s'''
            values = (data["service_name"], data["description"], data["price"], service_id)
            cursor.execute(query, values)

        elif action == "delete":
            if not service_id:
                messagebox.showerror("Error", "Service ID is required for deletion!")
                return
            query = '''DELETE FROM services WHERE service_id=%s'''
            cursor.execute(query, (service_id,))

        elif action == "show":
            query = '''SELECT * FROM services'''
            cursor.execute(query)
            return cursor.fetchall()

        conn.commit()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")
    finally:
        conn.close()

def manage_rooms(action, data=None, room_id=None):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hotel_management"
        )
        cursor = conn.cursor()

        if action == "add":
            if not data:
                messagebox.showerror("Error", "Data is required for adding a room!")
                return
            query = '''INSERT INTO rooms (room_type, availability, price, capacity) 
                       VALUES (%s, %s, %s, %s)'''
            values = (data["room_type"], data["availability"], data["price"], data["capacity"])
            cursor.execute(query, values)

        elif action == "update":
            if not room_id or not data:
                messagebox.showerror("Error", "Room ID and data are required for updating!")
                return
            print(f"Updating room: {room_id}, Data: {data}")
            query = '''UPDATE rooms SET room_type=%s, availability=%s, price=%s, capacity=%s 
                       WHERE room_id=%s'''
            values = (data["room_type"], data["availability"], data["price"], data["capacity"], room_id)
            cursor.execute(query, values)

            rows_affected = cursor.rowcount
            if rows_affected == 0:
                messagebox.showerror("Error", "No rows were updated. Check if the Room ID exists.")
                return

        elif action == "delete":
            if not room_id:
                messagebox.showerror("Error", "Room ID is required for deletion!")
                return
            print(f"Deleting room: {room_id}")
            query = '''DELETE FROM rooms WHERE room_id=%s'''
            cursor.execute(query, (room_id,))

            rows_affected = cursor.rowcount
            if rows_affected == 0:
                messagebox.showerror("Error", "No rows were deleted. Check if the Room ID exists.")
                return
            print(f"Deleting room: {room_id}")
            query = '''DELETE FROM rooms WHERE room_id=%s'''
            cursor.execute(query, (room_id,))

            rows_affected = cursor.rowcount
            if rows_affected == 0:
                messagebox.showerror("Error", "No rows were deleted. Check if the Room ID exists.")
                return

        elif action == "show":
            query = '''SELECT * FROM rooms'''
            cursor.execute(query)
            return cursor.fetchall()

        conn.commit()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")
        

    finally:
        conn.close()
# Run setup and start the app
main_window()