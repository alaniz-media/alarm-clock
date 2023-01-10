from moviepy.editor import AudioFileClip, VideoFileClip

def video_to_audio(path_to_file):
    processed_video = VideoFileClip(path_to_file)
    processed_audio = processed_video.audio
    return processed_audio, processed_video