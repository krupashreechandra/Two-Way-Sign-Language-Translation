import cv2

print("🎥 Checking if OpenCV can access your camera...")

cap = cv2.VideoCapture(0)  # Try 0 first; if external cam, use 1 or 2

if not cap.isOpened():
    print("❌ Camera not detected. Try changing the index to 1 or 2.")
else:
    print("✅ Camera opened successfully! Press 'q' to close the window.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Frame not captured. Check your webcam connection.")
            break

        cv2.imshow("Camera Test - OpenCV", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("👋 Exiting camera test...")
            break

cap.release()
cv2.destroyAllWindows()
