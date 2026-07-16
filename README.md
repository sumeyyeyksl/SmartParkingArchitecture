# Smart Parking Architecture

A Python-based smart parking system developed as part of a Software Architecture course project. The system detects vehicle license plates, manages resident and guest parking records, monitors parking duration, and sends notification emails when the parking time limit is exceeded.

## Features

- License Plate Recognition
- Resident and Guest Vehicle Management
- Parking Time Monitoring
- Email Notification System
- Database Integration
- Desktop User Interface

## Technologies

- Python
- OpenCV
- EasyOCR
- SQLAlchemy
- MySQL
- Tkinter

## Project Structure

```
images/
db.py
mail_send.py
plate_recognition.py
time_check.py
viewer.py
requirements.txt
```

## Installation

1. Clone the repository.

```bash
git clone https://github.com/sumeyyeyksl/SmartParkingArchitecture.git
```

2. Install the required packages.

```bash
pip install -r requirements.txt
```

3. Configure your MySQL database connection in `db.py`.

4. Configure your email credentials in `mail_send.py`.

5. Run the application.

## Author

Meryem Sümeyye Yüksel
