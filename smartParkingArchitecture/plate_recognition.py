import cv2
import easyocr
from db import session, Resident, Guest
from datetime import datetime


reader = easyocr.Reader(['en'], gpu=False)


image_paths = [
    "images/Cars102.png",
    "images/Cars75.png",
    "images/Cars77.png",
    "images/Cars80.png",
    "images/Cars9.png",
    "images/Cars98.png"
]

def is_resident(plate):
    result = session.query(Resident).filter_by(plate=plate).first()
    return result is not None


def process_plate(plate):
    now = datetime.now()

    if is_resident(plate):
        print(f"Resident vehicle detected: {plate}")
    else:
        guest = session.query(Guest).filter_by(plate=plate).first()
        if guest:
            guest.exit_time = now
            session.commit()
            print(f"Guest vehicle exit recorded: {plate}")
        else:
            new_guest = Guest(plate=plate, entry_time=now)
            session.add(new_guest)
            session.commit()
            print(f"New guest vehicle recorded: {plate}")


for image_path in image_paths:
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Unable to load image at {image_path}")
        continue


    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    gray = cv2.equalizeHist(gray)


    blur = cv2.bilateralFilter(gray, 11, 17, 17)


    edged = cv2.Canny(blur, 30, 200)


    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    plate_img = None
    for c in contours:

        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * peri, True)

        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(c)
            plate_img = img[y:y+h, x:x+w]
            break

    if plate_img is None:
        print(f"Plate not found in {image_path}")
        continue


    plate_gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)
    results = reader.readtext(plate_gray, detail=0, paragraph=False)


    for plate in results:
        plate = plate.strip().replace(" ", "").upper()
        print(f"Detected Plate: {plate}")
        process_plate(plate)








