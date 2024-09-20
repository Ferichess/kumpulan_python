
import yt_dlp

def download_video(url, output_path):
    ydl_opts = {
        'format': 'best',
        'outtmpl': output_path,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download selesai!")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengunduh video: {e}")

# Contoh penggunaan
download_video('https://www.youtube.com/watch?v=Ks-_Mh1QhMc', 'video.mp4')
