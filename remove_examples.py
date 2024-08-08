#!/usr/bin/env python3

import os
import sys
import shutil

def main(root: str, min_frames: int):
    for curr_dir, dirs, files in os.walk(root):
        for d in dirs:
            path = os.path.join(curr_dir, d)
            num_frames = len(os.listdir(path))
            if num_frames < min_frames:
                shutil.rmtree(path)
                print(f'removed {path}')

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))