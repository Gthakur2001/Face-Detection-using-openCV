
import cv2


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

image = cv2.imread('C:/Users/user/Pictures/i2.jpg')


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(gray_image, 1.1)


for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)


cv2.imshow("image_faces", image)


# video_cap = cv2.VideoCapture(0)
#
# while True:
#
#     ret, frame = video_cap.read()
#
#     if not ret:
#         print("Error: Failed to capture frame")
#         break
#
#     gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#
#     faces = face_cascade.detectMultiScale(gray_frame, 1.1)
#
#
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#
#     cv2.imshow("video_live", frame)
#
#     if cv2.waitKey(1) == ord('q'):
#         break
#
#
# video_cap.release()



cv2.waitKey(0)

cv2.destroyAllWindows()
