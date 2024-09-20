import subprocess
import os

def combine_videos_and_add_gif(video1_path, video2_path, gif_path, output_path):
    # Mendapatkan informasi tentang video
    def get_video_info(video_path):
        cmd = ['ffprobe', '-v', 'error', '-select_streams', 'v:0', 
               '-count_packets', '-show_entries', 'stream=width,height,duration,nb_read_packets', 
               '-of', 'csv=p=0', video_path]
        output = subprocess.check_output(cmd).decode('utf-8').strip().split(',')
        return {'width': int(output[0]), 'height': int(output[1]), 
                'duration': float(output[2]), 'frames': int(output[3])}

    video1_info = get_video_info(video1_path)
    video2_info = get_video_info(video2_path)

    # Menentukan durasi output (menggunakan video terpendek)
    output_duration = min(video1_info['duration'], video2_info['duration'])

    # Menghitung ukuran frame output
    output_width = video1_info['width'] + video2_info['width']
    output_height = max(video1_info['height'], video2_info['height'])

    # Membuat command FFmpeg
    cmd = [
        'ffmpeg',
        '-i', video1_path,
        '-i', video2_path,
        '-i', gif_path,
        '-filter_complex',
        f'[0:v]scale={video1_info["width"]}:{output_height}[v0];'
        f'[1:v]scale={video2_info["width"]}:{output_height}[v1];'
        f'[v0][v1]hstack[bg];'
        f'[2:v]scale=100:100,loop={int(output_duration)}:0:1[gif];'
        f'[bg][gif]overlay=10:10',
        '-t', str(output_duration),
        '-y',
        output_path
    ]

    # Menjalankan command FFmpeg
    subprocess.run(cmd, check=True)

    print(f"Video berhasil dibuat: {output_path}")

# Contoh penggunaan
video1_path = 'path/to/cat_video.mp4'
video2_path = 'path/to/dog_video.mp4'
gif_path = 'path/to/animation.gif'
output_path = 'output_video.mp4'

combine_videos_and_add_gif(video1_path, video2_path, gif_path, output_path)