from youtubesearchpython import VideosSearch
import sys
import subprocess



def get_video_link():
    bash_command = "mpv "
    if len(sys.argv) > 1:
        bash_command += VideosSearch(sys.argv[1], limit=1).result()['result'][0]['link']
        result = subprocess.run(bash_command, shell=True, capture_output=True, text=True)

    else:
        return "No input provided."

if __name__ == "__main__":
    get_video_link()

