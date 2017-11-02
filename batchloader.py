import requests
import calendar
import json

def create_request(slug):
    cid = "blah"
    print(type(slug))
    print(slug)
    clip_info = requests.get("https://api.twitch.tv/kraken/clips/" + slug, headers={"Client-ID": cid, "Accept": "application/vnd.twitchtv.v5+json" }).json()
    return clip_info

# for each clip in clips.txt
for clip in open('clips.txt', 'r'):
    slug = clip.split('/')[3]
    print(create_request(slug))