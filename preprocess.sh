#!/bin/bash

python3 split_videos_into_frames.py
python3 resize.py 1 &
python3 resize.py -1 
python3 move.py

