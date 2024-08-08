import cv2
import os
import cv2.data
import time

# Create the data folder if it does not exist
DATA_FOLDER = 'data'
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)


# This function captures the face of a user.
# It receives the username as a parameter.
# It saves a set of images in the data folder.
def capture_face(username):
        # Open the camera
        cap = cv2.VideoCapture(0)
        count = 0
        os.makedirs(f"data/{username}", exist_ok=True)

        # Capture the face for 15 seconds
        start_time = time.time()
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        while start_time + 15 > time.time():
            ret, frame = cap.read()
            if not ret:
                break

            # Detect the faces
            faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)

            key = cv2.waitKey(1)
            if key & 0xFF == ord('q'):
                break

            # Resize and save the images
            for (x, y, w, h) in faces:
                cv2.imshow('Face Capture', frame)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray_face = gray[y:y+h, x:x+w]
                gray_face = cv2.resize(gray_face, (150, 150))
            if count % 20 == 0: 
                img_name = f"data/{username}/image_{count//20}.jpg"
                cv2.imwrite(img_name, gray_face)
            
            count += 1

        # Release the camera and close the windows
        cap.release()
        cv2.destroyAllWindows()

# This function recognizes the face of a user.
# It receives the username as a parameter.
# It returns True if the face was recognized successfully, False otherwise.
def recognize_face(username):
        # Open the camera
        cap = cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        # Show the camera for 2 seconds
        time_wait = time.time() + 2
        while time.time() < time_wait:
            ret, frame = cap.read()
            cv2.imshow('Face Recognition', frame)
            cv2.waitKey(1)

        # Try to recognize the face for 15 seconds
        time_wait = time.time() + 15
        while time.time() < time_wait:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow('Face Recognition', frame)

            # Detect the faces
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)
            for (x, y, w, h) in faces:
                face = frame[y:y+h, x:x+w]
                face = cv2.resize(face, (150, 150))
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]

                # Compare the face with the images of the user
                for images in os.listdir(f"data/{username}"):
                    img_path = os.path.join(f"data/{username}", images)
                    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                    img = cv2.resize(img, (w, h))

                    # Get the correlation between the images
                    res = cv2.matchTemplate(roi_gray, img, cv2.TM_CCOEFF_NORMED)
                    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

                    # If the face is recognized, return True
                    if max_val > 0.87:
                        cap.release()
                        cv2.destroyAllWindows()
                        return True

            # If the user presses 'q', return False
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the camera and close the windows
        cap.release()
        cv2.destroyAllWindows()
        print(f"Usuario {username} no autenticado")
        return False


# Test the functions

# if __name__ == "__main__":
#     username = input("Ingrese el nombre de usuario: ")
#     capture_face(username)
#     recognize_face(username)