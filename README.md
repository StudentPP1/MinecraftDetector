# MinecraftDetector
This project uses YOLOv8 object detection model to detect players in Minecraft and display a bounding box around them on screen using Tkinter. 

# Installation
Clone the repository:
```
git clone https://github.com/StudentPP1/MinecraftDetector.git
```

# Install the required packages:
```
pip install -r requirements.txt
```
Download the 'best.pt' file from the repository and place it in the project directory.

# Usage
Run the following command in the project directory to start the program: ```python main.py```

The user can enable players detecting by pressing '+' on your keyboard. The program will start capturing the screen and detecting players. If a player is detected, a bounding box will be drawn around them. Disable players detecting press '-', to end the program press '0'.

# Note
This project is designed to work on a Windows machine with the required packages installed. It may not work as intended on other platforms.
