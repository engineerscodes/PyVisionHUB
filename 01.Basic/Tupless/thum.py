from moviepy.editor import *
import numpy as np
from PIL import Image as im
clip = VideoFileClip("example.mp4")
clip=clip.resize(width=800)
frames=clip.save_frame("thumbnail.jpg",t=0.10)

print(clip.get_frame(1))

data = im.fromarray(clip.get_frame(1))

print(data)

call=data.save('gfg_dummy_pic.png')
