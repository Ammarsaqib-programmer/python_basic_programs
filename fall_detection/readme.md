# Fall Detection using MediaPipe & OpenCV

It works in real-time using your computer's webcam.

---

## 📌 Features
- Real-time full-body pose detection
- Simple rule-based fall detection logic
- Alerts with `"FALL DETECTED!"` on the video feed when a fall is suspected
- Uses lightweight and fast MediaPipe Pose
---

## ⚙️ How It Works

* The script uses **MediaPipe Pose** to track 33 body landmarks.
* It checks the height of the **nose** and **hip** in the video frame.
* If both are close to the bottom of the frame for more than `fall_threshold_seconds` (default: 2 seconds), a fall alert is triggered.

---

## 🖼️ Example Output

When a fall is detected, the webcam feed will display:

```
FALL DETECTED!
```

With a red warning message on the screen.

---

## ⚠️ Limitations

* May produce false positives if the person is sitting or lying intentionally.
* Works best with a camera at chest/head height.
* Not suitable for overhead cameras without adjustment.

---

## 📜 License

This project is licensed under the MIT License — feel free to modify and use it in your own projects.


