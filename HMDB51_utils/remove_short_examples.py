#!/usr/bin/env python3
"""
Script to remove video examples with less than N frames.
It is assumed the frames from each example are stored in a
separate subdirectory.
"""
import os
import sys
import shutil

def main(root: str, min_frames: int):
    for curr_dir, dirs, files in os.walk(root):
        for d in dirs:
            path = os.path.join(curr_dir, d)
            num_frames = len(os.listdir(path))
            print(f"{d} has {num_frames} frames")
            if num_frames < min_frames:
                shutil.rmtree(path)
                print(f'removed {path}')

if __name__ == '__main__':
    root_dir = sys.argv[1]
    min_frames = int(sys.argv[2])
    main(root_dir, min_frames)