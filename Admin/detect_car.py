import cv2 as cv

haar_cascade = 'cars.xml'
cap = cv.VideoCapture(0)
car_cascade = cv.CascadeClassifier(haar_cascade)
# loop runs if capturing has been initialized.
while True:
    ret, frames = cap.read()
    cv.rectangle(frames, (730, 485), (2, 250), (0, 0, 255), thickness=2)
    crop = frames[300:495, 2:730]
    gray = cv.cvtColor(crop, cv.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    for (x, y, w, h) in cars:
        cv.rectangle(crop, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv.imshow('video_crop', crop)
    cv.imshow('video', frames)
    # Wait for Esc key to stop
    if cv.waitKey(10) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()









#
#
#
# while True:
#     rat, frame = vid.read()
#     cv.rectangle(frame, (730, 485), (2, 250), (0, 0, 255), thickness=2)
#     crop = frame[300:495, 2:730]
#     cv.imshow("ORG_video", frame)
#     cv.imshow("CROP_video", crop)
#
#
#     if cv.waitKey(100) & 0xFF == ord('q'):
#         break
