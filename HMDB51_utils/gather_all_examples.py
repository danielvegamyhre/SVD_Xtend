#!/usr/bin/env python3
"""
Script to copy all video examples to a single directory.
"""

import os
import sys
import shutil

def reorganize(root_dir: str, output_dir: str) -> None:
    for entry in os.listdir(root_dir):
        path = os.path.join(root_dir, entry)
        if os.path.isdir(path):
            for subentry in os.listdir(path):
                subpath = os.path.join(path, subentry)
                if os.path.isdir(subpath):
                    target_dir = os.path.join(output_dir, subentry)
                    print(f"Copying {subpath} to {target_dir}")
                    shutil.copytree(subpath, target_dir)

if __name__ == '__main__':
    root_dir, output_dir = sys.argv[1], sys.argv[2]
    reorganize(root_dir, output_dir)