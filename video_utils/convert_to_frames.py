import os
import sys
import cv2
from tqdm import tqdm

def extract_frames(video_path, output_dir, width=320, height=320):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Open the video file
    video = cv2.VideoCapture(video_path)
    
    # Get video properties
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Iterate through frames
    for frame_number in tqdm(range(frame_count), desc=f"Processing {os.path.basename(video_path)}"):
        # Read frame
        ret, frame = video.read()
        if not ret:
            break

        # resize
        resized_image = cv2.resize(frame, (width, height))

        # Save frame as JPEG
        output_path = os.path.join(output_dir, f"frame_{frame_number:06d}.jpg")
        cv2.imwrite(output_path, resized_image)
    
    # Release video object
    video.release()

def process_directory(input_dir, output_base_dir):
    # Iterate through files in input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".mp4"):
            video_path = os.path.join(input_dir, filename)
            video_name = os.path.splitext(filename)[0]
            output_dir = os.path.join(output_base_dir, video_name)
            
            extract_frames(video_path, output_dir)

if __name__ == "__main__":
    input_directory = sys.argv[1]
    output_base_directory = sys.argv[2]
    
    process_directory(input_directory, output_base_directory)