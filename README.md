# Motion Extraction with MoviePy and OpenCV

This project demonstrates how to process videos using the MoviePy and OpenCV libraries in Python. The script takes a video file as input, applies a series of transformations to it, and outputs the result as a new video file. The transformations include converting the video to grayscale, inverting the colors, and overlaying the difference between frames in a range to extract motion.

## Requirements

- Python 3.6 or higher
- MoviePy
- OpenCV
- tqdm

You can install the required packages using PDM:

- pip install pdm
- pdm install


## Usage

1. Update the `clip_path` variable in the script with the path to your video file.
2. Run the script. This will create a series of frames with different effects applied.
3. The final video will be saved as `output.mp4`.

## Note

This script uses a significant amount of memory due to the processing of individual frames. Ensure you have sufficient memory available before running the script.

## Motion Extraction

The script implements a form of motion extraction by calculating the difference between frames in a range and overlaying this difference on the original grayscale frames. This allows for the visualization of motion in the video.

This project was inspired by Posy - https://www.youtube.com/watch?v=NSS6yAMZF78