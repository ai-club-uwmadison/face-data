#!/bin/bash

python3 split_videos_into_frames.py
read -p "Your images may be rotated. Please manually fix them and then press [ENTER] to continue." input
python3 resize.py 1 &
python3 resize.py -1 
python3 move.py

