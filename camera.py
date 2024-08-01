import cv2
import requests

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)
    heads = face_cascade.detectMultiScale(gray, 1.1, 4)
    num_heads = len(heads)

    data = {"NumberOfHeads": num_heads}
    headers = {"Content-Type": "application/json"}
    
    try:
       # response = requests.post('https://030f0fb7-01b1-4f10-ac37-ef946f269c19-00-sxa8p6gz3kq4.riker.replit.dev/c', json=data, headers=headers)
        response = requests.post('https://a2624187-1683-464a-82d2-b3006519eab0-00-256vgi4swxk6a.picard.replit.dev/c', json=data, headers=headers)
        if response.status_code == 200:
            print("Data sent successfully.")
        else:
            print("Failed to send data. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", e)

    if num_heads > 0:
        cv2.putText(frame, "Passenger count: " + str(num_heads), (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) == ord('r'):
        break

cap.release()
cv2.destroyAllWindows()
