import subprocess
import yt_dlp

def download_with_idm(url, output_dir, filename):
    # Path to IDM executable
    idm_path = r'C:\Program Files (x86)\Internet Download Manager\IDMan.exe'

    # IDM command line arguments
    idm_command = [
        idm_path,
        '/d', url,
        '/p', output_dir,
        '/f', filename,
        '/a',  # Start the download automatically
    ]

    try:
        subprocess.run(idm_command, check=True)
        print(f"Download started for {url} with IDM.")
    except subprocess.CalledProcessError as e:
        print(f"Error starting download with IDM: {e}")

def get_video_url(video_url):
    ydl_opts = {
        'format': 'best',
        'quiet': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            return info_dict['url']
    except Exception as e:
        print(f"Error extracting video URL: {e}")
        return None

# Contoh penggunaan untuk dua video
youtube_video_urls = [
    'https://www.youtube.com/shorts/NfhaOmPYkeI',
    'https://www.youtube.com/shorts/M1x1Pbj1iNI'
]
download_directory = 'C:\\path\\to\\download\\folder'
file_names = ['downloaded_video1.mp4', 'downloaded_video2.mp4']

for video_url, file_name in zip(youtube_video_urls, file_names):
    video_direct_url = get_video_url(video_url)
    if video_direct_url:
        download_with_idm(video_direct_url, download_directory, file_name)
