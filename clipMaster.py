# Import necessary libraries and modules
from moviepy.editor import VideoFileClip, concatenate_videoclips
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QLineEdit, QLabel, QPushButton, QHBoxLayout, QMessageBox, QSlider, QVBoxLayout
from PyQt5 import Qt

# Create main application
app = QApplication([])

# Create a widget to hold GUI elements
window = QWidget()
window.setWindowTitle("PyQt5 Video Splitter")

# Create a label and input field for  video file
video_label = QLabel("Video file:")
video_input = QLineEdit()
video_input.setReadOnly(True)

# Create a button to open file dialog
video_button = QPushButton("Choose File")

# Define a function to handle file dialog
def select_file():
    # Open  file dialog and get selected file
    filename, _ = QFileDialog.getOpenFileName(window, "Select a video file")

    # Check if file is a valid video file
    allowed_extensions = ["mp4", "avi", "mkv", "mov"]
    file_extension = filename.split(".")[-1]
    if file_extension not in allowed_extensions:
        # Display an error message if  file is not a valid video file
        error_message = f"Error: {file_extension.upper()} is not a supported file type. Please select a video file with one of  following extensions: {', '.join(allowed_extensions)}"
        QMessageBox.warning(window, "Error", error_message)
    else:
        # Set  text of input field to  selected file
        video_input.setText(filename)

# Connect button's clicked signal to  select_file function
video_button.clicked.connect(select_file)

# Create a label and input field for timestamps
timestamps_label = QLabel("Timestamps:")
timestamps_input = QLineEdit()

# Create a button to split  video
split_button = QPushButton("Split Video")

# Create a horizontal layout for button
button_layout = QHBoxLayout()
button_layout.addStretch()
button_layout.addWidget(video_button)
button_layout.addWidget(split_button)
button_layout.addStretch()

# Add  button layout to main window
window.setLayout(button_layout)

# Define a function to split video
def split_video():
    # Get video file and timestamps from input fields
    filename = video_input.text()
    timestamps = timestamps_input.text()

    # Open selected video file using MoviePy
    video = VideoFileClip(filename)

    # Split video into clips at  specified timestamps
    clips = []
    for timestamp in timestamps.split(","):
        start, end = timestamp.split("-")
        clip = video.subclip(start, end)
        clips.append(clip)

    # Concatenate clips into a single video
    final_video = concatenate_videoclips(clips)

    # Prompt user to specify a directory and file naming convention for  resulting clips
    directory = QFileDialog.getExistingDirectory(window, "Select a directory to save  clips")
    file_prefix, _ = QFileDialog.getSaveFileName(window, "Enter a file prefix for  clips")

    # Save resulting clips to individual files
    for i, clip in enumerate(clips):
        clip.write_videofile(f"{directory}/{file_prefix}_{i}.mp4")

    # Display a message to indicate that video has been split and saved successfully
    window.setWindowTitle("Video split and saved successfully!")

# Connect  button's clicked signal to split_video function
split_button.clicked.connect(split_video)

# Create a vertical layout for timestamps label and input field
timestamps_layout = QVBoxLayout()
timestamps_layout.addWidget(timestamps_label)
timestamps_layout.addWidget(timestamps_input)

# Add timestamps layout to  main layout
button_layout.addLayout(timestamps_layout)

# Show  widget and run  main application loop
window.show()
app.exec_()