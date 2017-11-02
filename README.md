# Batch Clips Downloader for Twitch

### prerequisite:
1.Get a twitch Client_Id Token by registering a twitch app (here)[https://dev.twitch.tv/dashboard/apps/create]. You can just put http://localhost for the `OAuth Redirect URI` section.

Once you finished, copy the `Client ID`. You will need it to run the script.

2. Install python on your machine if you haven't.

### Install:
Install several python packages
```
pip install request progressbar2
```

Then run the batchloader script with your new Client Id
```
cd twitch-batch-loader
python batchloader.py <YOUR AWESOME CLIENT ID>
```
Voila! check your downloads folder and you should see the videos there once you see the finished message in your terminal