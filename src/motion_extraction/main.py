#%%

from moviepy.editor import VideoFileClip, ImageSequenceClip
from moviepy.editor import ipython_display

import cv2
import numpy as np
from IPython.display import display, Image
from tqdm import tqdm
import sys

import gc


#%%
clip_path = r"C:\Users\user\Downloads\VID_asdf.mp4"  



def unloadModule(mod):
    search_mod_name = mod.__name__
    for mod_name, mod_val in sys.modules.items():
        if mod_val.__name__ is search_mod_name:
            del sys.modules[mod_name]            
            break

clip  = VideoFileClip(clip_path)

# get frames of greyscale and inverted greyscale
from moviepy.video.fx.all import invert_colors, blackwhite
video_a = clip.without_audio().fx(blackwhite)
video_b = video_a.fx(invert_colors)
frames_a = list(video_a.iter_frames())
frames_b = list(video_b.iter_frames())
unloadModule(invert_colors)
unloadModule(blackwhite)
del clip
gc.collect()



#%%
# get the difference betweeen the frames in a range and overlay that to the original greyscale
diff_start = 1
diff_stop = 55
diff_step = 1
final_frames = []
for i_frame in tqdm(range(len(frames_a)), desc="Creating final frames"):
    frame_a = frames_a[i_frame]
    frame_b = frames_b[i_frame]
    final_frame = cv2.addWeighted(frame_a, 0.5, frame_b, 0.5, 0)
    #for lowest impact of last diff, add the diffs in reverse
    for i_diff in range(diff_stop, diff_start, -diff_step): 
        if i_frame-i_diff > 0:
            frame_b = frames_b[i_frame-i_diff]
            diff_frame = cv2.addWeighted(frame_a, 0.5, frame_b, 0.5, 0)
            final_frame = cv2.addWeighted(final_frame, 0.5, diff_frame, 0.5, 0)
        
    final_frames.append(final_frame)

video_c = ImageSequenceClip(final_frames, fps=video_a.fps)

#%%
ipython_display(video_c)
#%%
video_c.write_videofile("output.mp4")
