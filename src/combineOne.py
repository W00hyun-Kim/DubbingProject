from moviepy.editor import * 
videoclip = VideoFileClip("Caillou with subtitle.mp4")
audioclip = AudioFileClip("output.mp3")
audioclip2 = AudioFileClip("Caillou-with-subtitle.mp3")
new_audioclip = CompositeAudioClip([audioclip, audioclip2])
videoclip.audio = new_audioclip
videoclip.write_videofile("result.mp4")