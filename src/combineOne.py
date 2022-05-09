from moviepy.editor import *   #import moviepy
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from colorama import Fore, Back, Style

try:  #to prevent pipe broken error

    videoclip = VideoFileClip("Caillou_cookie.mp4") #orgin video with no subtitle
    audioclip = AudioFileClip("Caillou-with-subtitle.mp3") #audio clip
    audioclip2 = AudioFileClip("output.mp3") #background audioclip
    new_audioclip = CompositeAudioClip([audioclip, audioclip2]) #Composite audioclip and audioclip2
    videoclip.audio = new_audioclip
    videoclip.write_videofile("result.mp4")

    generator = lambda txt: TextClip(txt, font='Georgia-Regular', fontsize=30, color='white',stroke_color='black')
    subtitles = SubtitlesClip("subtitle.srt", generator)
    myvideo = VideoFileClip("result.mp4")
    final = CompositeVideoClip([myvideo, subtitles.set_pos(('center','bottom'))])
    final.write_videofile("dubbing_final.mp4", fps=myvideo.fps)

except IOError :
    sys.exit()
