# Batch Clips Downloader for Twitch
![example-gif](https://github.com/amiechen/twitch-batch-loader/blob/master/batchloader.gif)

### Pre-Install:

1) Get a twitch Client_Id Token by registering a twitch app [here](https://dev.twitch.tv/dashboard/apps/create).
Once finished, copy the `Client ID`. You will need it to run the script.

2) Install python on your machine if you haven't.

### Install:

1) Install several python packages
```
pip install request progressbar2
```

2) Then run the batchloader script with your new Client Id
```
cd twitch-batch-loader
python batchloader.py <YOUR AWESOME CLIENT ID>
```

Voila! check your downloads folder and you should see the videos there once you see the finished message in your terminal