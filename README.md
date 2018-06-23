# Twitch Clip Batch Downloader  
![example-gif](https://github.com/daevski/twitch-batch-loader/blob/master/batchloader.gif)

### Pre-Install:

1) Get a twitch `Client ID` by registering a twitch app [here](https://dev.twitch.tv/dashboard/apps/create).
Once finished, copy the `Client ID`. You will need it to run the script.

2) Install python on your machine if you haven't.

### Usage:

1) Install several python packages
```
pip install request progressbar2
```

2) Delete the example clips in `clips.txt` and the ones your want. Make sure it has no trailing spaces nor comma (I'm too lazy to strip it out).

3) Then run the batchloader script with your new Client Id
```
cd twitch-batch-loader
python batchloader.py <YOUR AWESOME CLIENT ID>
```

Voila! once you see the finished message in your terminal, check the `downloads` folder in this repo and you should see the videos there.