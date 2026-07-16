from db import session, Resident, Guest
from datetime import datetime, timedelta


def check_guest_time_limit():
    now = datetime.now()
    guests_list = session.query(Guest).all()

    for guest in guests_list:

        if not guest.entry_time:
            continue


        if (now - guest.entry_time) > timedelta(minutes=5):
            print(f"ALERT: Guest vehicle {guest.plate} has exceeded 24 hours!")


            new_resident = Resident(plate=guest.plate)
            session.add(new_resident)
            session.commit()


            session.delete(guest)
            session.commit()

            print(f"Guest vehicle {guest.plate} moved to Resident.")
        else:
            print(f"Guest vehicle {guest.plate} is still within the time limit.")


check_guest_time_limit()









