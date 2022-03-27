import os
import shutil
import tempfile
import traceback
from importlib.metadata import version
from pathlib import Path

import aiohttp
import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import Bot
from PIL import Image
from pycord import video_reader

bot = Bot(["pycord!", "pc!", "nextcord!", "nc!"])


@bot.command("frame")
async def convert_command(ctx: commands.Context, frame: int = 0):
    if not ctx.message.attachments:
        return await ctx.send("No attachment found")

    temp_dir = Path(tempfile.mkdtemp())

    try:
        videos = [
            v
            for v in ctx.message.attachments
            if v.content_type and "video" in v.content_type
        ]

        async with aiohttp.ClientSession() as session:
            for video in videos:
                async with session.get(video.url) as response:
                    await video.save(temp_dir / video.filename)

                    reader = video_reader.VideoReader(temp_dir / video.filename)

                    first_frame = await bot.loop.run_in_executor(
                        None, lambda: reader.get_batch([frame])
                    )  # Not sure if this is needed but it is probably a good idea

                    img = Image.frombuffer(
                        "RGB", (reader.width, reader.height), first_frame.flatten()
                    )
                    img.save(temp_dir / f"{video.filename}.png", "png")

                    await ctx.send(
                        file=nextcord.File(temp_dir / f"{video.filename}.png")
                    )

    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)

    shutil.rmtree(temp_dir)


@bot.command("version")
async def info_command(ctx: commands.Context):
    pycord_version = version("pycord")
    nextcord_version = version("nextcord")

    await ctx.send(
        f"pycord version: {pycord_version} and nextcord version: {nextcord_version}"
    )


bot.run(os.environ["DISCORD_TOKEN"])
