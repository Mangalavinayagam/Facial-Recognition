# Face Recognition

This project is a real-time face recognition application that uses a webcam feed to identify individuals based on pre-defined reference images. It leverages the **DeepFace** library for facial recognition and OpenCV for video capture and display.

## Features

- **Real-Time Recognition:** Continuously analyzes webcam frames for face matching.
- **Multiple Face Matching:** Compares input frames against multiple reference images.
- **Threaded Processing:** Uses multithreading for efficient face verification.
- **Feedback Overlay:** Displays real-time feedback on the video feed, indicating recognized individuals or "No Match."

## Prerequisites

- Python 3.x
- OpenCV library
- DeepFace library
- A webcam or compatible video input device

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd face-recognition
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Place reference images in the project directory and name them appropriately (e.g., `Photo1.jpg`, `Photo2.jpeg`, `Photo3.jpeg`).

## Usage

1. Run the script:
   ```bash
   python Face_Recognition.py
   ```

2. The webcam feed will open in a new window, and the application will process the frames to identify individuals.

3. Press `q` to quit the application.

## How It Works

1. The application uses OpenCV to capture video frames from the webcam.
2. Frames are passed to the `DeepFace.verify()` function for comparison against pre-loaded reference images.
3. Multithreading ensures that face verification does not block frame capture, maintaining smooth video feed performance.
4. Based on the results:
   - Recognized individuals are labeled (e.g., "Person1," "Person2," etc.).
   - Unmatched faces are labeled as "NO MATCH."

## Customization

- **Reference Images:** Add or replace reference images in the project directory and update the file names in the script.
- **Recognition Logic:** Modify the `check_face()` function to include additional or alternative recognition criteria.
- **Frame Rate:** Adjust the `counter` variable's frequency to control how often frames are analyzed.

## Limitations

- Limited to the reference images provided.
- Accuracy depends on the quality and resolution of the reference images.
- Designed for real-time use and may struggle with low-light or poor video quality.

## Future Improvements

- Support for additional recognition models or algorithms.
- Improved GUI for user interaction.
- Database integration for scalable reference image management.
- Enhanced error handling and feedback mechanisms.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements or bug fixes.

