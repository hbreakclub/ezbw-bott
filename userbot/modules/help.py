# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio
from userbot import CMD_HELP
from userbot.events import register

modules = CMD_HELP


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("**Maaf Lord, Saya Tidak Punya Perintah Itu ć**")
            await asyncio.sleep(200)
            await event.delete()
    else:
        await event.edit("ššÆšš¬")
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t  "
        await event.edit("**ā Daftar Perintah Untuk\nLord-Userbot:\n\nāāāāāāāāāāāāāāāāāāā\n**"
                         f"ā°{string}ā± ā"
                         "\nāāāāāāāāāāāāāāāāāāā\n**Ketik Contoh** `.help afk` **Dengan nama perintah untuk melihat cara menggunakannya.**")
        await asyncio.sleep(1000)
        await event.delete()
