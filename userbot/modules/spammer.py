
# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#

from asyncio import wait

from userbot import BOTLOG_CHATID, BOTLOG,  CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.spam")
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[6:8])
        spam_message = str(e.text[8:])

        await wait(
            [e.respond(spam_message) for i in range(counter)]
            )

        await e.delete()
        if BOTLOG:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#SPAM \n\n"
                "Spam was executed successfully"
                )


@register(outgoing=True, pattern="^.bigspam")
async def bigspam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[9:13])
        spam_message = str(e.text[13:])

        for i in range(1, counter):
            await e.respond(spam_message)

        await e.delete()
        await e.client.send_message(BOTLOG_CHATID, "bigspam was successful"
                )


@register(outgoing=True, pattern="^.picspam")
async def tiny_pic_spam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        text = message.split()
        counter = int(text[1])
        link = str(text[2])
        if range(1, counter):
            await e.client.send_file(e.chat_id, link)
        await e.delete()
        if BOTLOG:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#PICSPAM \n\n"
                "PicSpam was executed successfully"
                )
