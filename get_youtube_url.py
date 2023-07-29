from youtubesearchpython import VideosSearch
import sys

def get_video_link():
    if len(sys.argv) > 1:
        return VideosSearch(sys.argv[1], limit=1).result()['result'][0]['link']
    else:
        return "No input provided."

if __name__ == "__main__":
    get_video_link()

