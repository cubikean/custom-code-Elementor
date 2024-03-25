from moviepy.editor import VideoFileClip

def compress_video(input_path, output_path, target_bitrate):
    video = VideoFileClip(input_path)
    
    # Compress the video by applying the specified target bitrate (in kbps)
    compressed_video = video.resize(width=video.w // 2)  # Reduce the video size
    
    # Save the compressed video with target bitrate
    compressed_video.write_videofile(output_path, codec="libx264", audio_codec="aac", bitrate=target_bitrate)
    
    print("The video has been compressed successfully!")

# Example usage
input_path = "C:/Users/Beekom/Desktop/dev/IAE/Pages_Site/Pages_Formations/video.mp4"
output_path = "C:/Users/Beekom/Desktop/dev/IAE/Pages_Site/Pages_Formations/video_export.mp4"
target_bitrate = "1000k"  # Target bitrate for compression in kbps

compress_video(input_path, output_path, target_bitrate)
