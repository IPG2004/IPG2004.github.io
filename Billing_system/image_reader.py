# from PIL import Image
import cv2
from pyzbar import pyzbar
import time

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    # cv2.imshow('frame', frame)
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    barcodes = pyzbar.decode(frame)

    for barcode in barcodes:
        x, y, w, h = barcode.rect
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, barcode_info, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        print(barcode_info)
    cv2.imshow('Scanner', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# ret, frame = cap.read()
# cv2.imwrite('image.jpg', frame)

# cap.release()