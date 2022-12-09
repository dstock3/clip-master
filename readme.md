PyQt5 Video Splitter
PyQt5 Video Splitter is a GUI application that allows you to split a video into multiple clips. It uses the moviepy library to handle the actual video manipulation, and PyQt5 for the GUI elements.

Installation
To install PyQt5 Video Splitter, you need to have the following dependencies installed:

Python 3.6 or later
PyQt5
moviepy
You can install these dependencies using pip:

Copy code
pip install PyQt5 moviepy
Once the dependencies are installed, you can download or clone the PyQt5 Video Splitter repository, and run the main.py script to start the application:

Copy code
git clone https://github.com/<username>/pyqt5-video-splitter
cd pyqt5-video-splitter
python main.py
Usage
To use PyQt5 Video Splitter, follow these steps:

Click the "Choose File" button to select the video file that you want to split.
In the "Timestamps" input field, specify the start and end times for each of the clips that you want to create. Separate multiple timestamps with a comma. For example, to create two clips at the 1 minute and 2 minute marks, you would enter 0:01:00-0:02:00, 0:02:00-0:03:00.
Click the "Split Video" button to split the video into the specified clips.
In the file dialog that appears, select the directory where you want to save the resulting clips, and enter a file prefix for the clips.
The resulting clips will be saved to individual files in the specified directory, using the specified file prefix and a numeric suffix (e.g. <file_prefix>_0.mp4, <file_prefix>_1.mp4, etc.). A message will be displayed indicating that the video has been split and saved successfully.