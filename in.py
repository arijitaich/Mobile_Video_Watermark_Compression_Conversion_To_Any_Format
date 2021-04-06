import moviepy.editor as mp

inp = 'in/XYZ.mp4'
out = 'out/XYZ.webm'

video = mp.VideoFileClip(inp)
if video.rotation == 90:
    video = video.resize(video.size[::-1])
    video.rotation = 0
    
logo = (mp.ImageClip("logo.png")
          .set_duration(video.duration)
          .resize(height=50) # if you need to resize...
          .margin(right=8, top=8, opacity=0) # (optional) logo-border padding
          .set_pos(("right","top")))

final = mp.CompositeVideoClip([video, logo])
final.write_videofile(out)