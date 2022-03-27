# Frame Extractor

![](https://img.shields.io/badge/code%20style-black-black?style=for-the-badge) ![](https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge) ![](https://img.shields.io/codefactor/grade/github/teaishealthy/frame_extractor?style=for-the-badge)

Discord bot that can extract a single frame from a video.

## Features

prefix is one of [nextcord!, nc!, pycord!, pc!].

| Command | Description |
| ------ | ----------- |
| prefix!version | Displays the versions of the used dependencies |
| prefix!frame \<frame:int>  | Extracts the frame from the video and sends it as a file |

## Using 

 - nextcord https://github.com/nextcord/nextcord
 - pycord https://github.com/alesanfra/pycord 

## Development

* Install requirements.txt
* Make sure ffmpeg and ffprobe binaries are in your PATH
* Export your bot token to the environment variable `DISCORD_TOKEN`
* Run the bot with `python3 main.py`

## Contributing

Contributions are welcome but adhere to the following guidelines

### Adding a dependency

* Make sure it is somewhat related to "discord bot development" and its ecosystem.
* Add the dependency as a prefix to the bot

Have fun!

## License

Licensed under the [MIT License](LICENSE)
