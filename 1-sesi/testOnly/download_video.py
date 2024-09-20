from pytube import YouTube
import pytube

try:
    # URL video YouTube yang valid dan dapat diakses
    video_url = 'https://www.youtube.com/watch?v=Ks-_Mh1QhMc'
    yt = YouTube(video_url)

    # Mendapatkan stream dengan resolusi tertinggi
    stream = yt.streams.get_highest_resolution()

    # Mengunduh video ke jalur yang diinginkan
    stream.download(output_path='path/to/download', filename='video.mp4')
    print("Download selesai!")
except pytube.exceptions.AgeRestrictedError:
    print("Video ini dibatasi usia dan tidak bisa diakses tanpa login.")
except pytube.exceptions.VideoUnavailable:
    print("Video tidak tersedia.")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
