import urllib.request
import requests
import json
import sys
from progressbar import ProgressBar, Percentage, Bar

basepath = 'downloads/'
base_clip_path = 'https://clips-media-assets.twitch.tv/'
pbar = ProgressBar(widgets=[Percentage(), Bar()])

def retrieve_mp4_url(slug):
    cid = sys.argv[1]
    clip_info = requests.get("https://api.twitch.tv/kraken/clips/" + slug.strip(), headers={"Client-ID": cid, "Accept": "application/vnd.twitchtv.v5+json" }).json()
    return clip_info['tracking_id']

def dlProgress(count, blockSize, totalSize):
    pbar.update( int(count * blockSize * 100 / totalSize) )

# for each clip in clips.txt
for clip in open('clips.txt', 'r'):
    slug = clip.split('/')[3]
    outputpath = (basepath + slug + '.mp4').replace('\n', '')
    clip_path = base_clip_path + retrieve_mp4_url(slug) + '.mp4'

    print('start downloading clip ' + clip_path)
    urllib.request.urlretrieve(clip_path, outputpath, reporthook=dlProgress)
    print('finish downloading')

print('Finished downloading all the videos.')