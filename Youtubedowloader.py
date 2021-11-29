from pytube import YouTube
import os
print("YOUTUBE VIDEO DOWNLOADER")
url = input("\nPaste your video url: ")
video = YouTube(url)


print(f"\nTitle: {video.title}")
streamlist = []
try:
    for stream in video.streams:
        if stream.resolution is None or stream.resolution in streamlist or stream.resolution in ("144p", "240p"):
            continue
        streamlist.append(stream.resolution)

    print(f'\nResolutions available: {", ".join(streamlist)}.')

    resolution = input("Type a resolution: ")
    stream = video.streams.get_by_resolution(resolution=resolution)
    while stream == None:
        resolution = input(
            "Resolution don't available. Try another resolution: ")
        stream = video.streams.get_by_resolution(resolution=resolution)

    path = os.path.join(os.environ['USERPROFILE'], "Downloads")

    print("\nDownloading the video, please wait...")
    if os.path.exists(path):
        stream.download(output_path=path)
    else:
        stream.download()
    print("\nVideo Downloaded. Check it out in your downloads directory or at the same path that you runned this script\n")

except BaseException:
    print(f"Can't download this. Try another one")
