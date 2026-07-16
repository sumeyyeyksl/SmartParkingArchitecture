import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
from db import session, Resident, Guest


warned_plates = set()

def fetch_residents():
    residents = session.query(Resident).all()
    return [(r.id, r.plate) for r in residents]

def fetch_guests():
    guests = session.query(Guest).all()
    return [(g.id, g.plate, g.entry_time, g.exit_time) for g in guests]

def populate_residents():
    tree_resident.delete(*tree_resident.get_children())
    for row in fetch_residents():
        tree_resident.insert("", tk.END, values=row)

def populate_guests():
    tree_guest.delete(*tree_guest.get_children())
    for row in fetch_guests():
        tree_guest.insert("", tk.END, values=row)

def check_guest_parking_time():
    now = datetime.now()
    guests = session.query(Guest).filter(Guest.exit_time == None).all()

    for guest in guests:
        if guest.entry_time:
            parked_duration = now - guest.entry_time
            minutes_over = int(parked_duration.total_seconds() // 60)


            if parked_duration > timedelta(minutes=5):
                if guest.plate not in warned_plates:
                    warned_plates.add(guest.plate)

                    fine_amount = 50

                    message = (f"Plaka: {guest.plate}\n"
                               f"Geçen Süre: {minutes_over} dakika\n"
                               f"Ceza: {fine_amount} TL")

                    messagebox.showerror("Süre Aşıldı!", message)


    root.after(60000, check_guest_parking_time)


root = tk.Tk()
root.title("Resident ve Guest Kayıtları")
root.geometry("800x600")


tk.Label(root, text="Residents", font=("Arial", 16)).pack()
columns_resident = ("ID", "Plate")
tree_resident = ttk.Treeview(root, columns=columns_resident, show="headings")
for col in columns_resident:
    tree_resident.heading(col, text=col)
tree_resident.pack(expand=True, fill="both", pady=10)


tk.Label(root, text="Guests", font=("Arial", 16)).pack()
columns_guest = ("ID", "Plate", "Entry Time", "Exit Time")
tree_guest = ttk.Treeview(root, columns=columns_guest, show="headings")
for col in columns_guest:
    tree_guest.heading(col, text=col)
tree_guest.pack(expand=True, fill="both", pady=10)


populate_residents()
populate_guests()


root.after(1000, check_guest_parking_time)


root.mainloop()










