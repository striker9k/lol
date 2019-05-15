import os
from PIL import Image
from time import sleep
from userbot import bot, HELPER
from telethon import events
from selenium import webdriver
from urllib.parse import quote_plus
from userbot.events import register
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

@register(pattern=r".setlang", outgoing=True)
async def setlang(prog):
    if not prog.text[0].isalpha() and prog.text[0] not in ("/", "#", "@", "!"):
        global lang
        lang = prog.text.split()[1]
        await prog.edit(f"language set to {lang}")


@register(outgoing=True, pattern="^.carbon")
async def carbon_api(e):
 if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
   """ A Wrapper for carbon.now.sh """
   await e.edit("Processing...")
   CARBON = 'https://carbon.now.sh/?l=python&code={code}'
   textx = await e.get_reply_message()
   pcode = e.text
   if pcode[8:]:
         pcode = str(pcode[8:])
   elif textx:
         pcode = str(textx.message) # Importing message to module
   code = quote_plus(pcode) # Converting to urlencoded 
   url = CARBON.format(code=code)
   chrome_options = Options()
   chrome_options.add_argument("--headless")
   chrome_options.add_argument("--window-size=1920x1080")
   chrome_options.add_argument("--disable-dev-shm-usage")
   chrome_options.add_argument("--no-sandbox")
   chrome_options.add_argument('--disable-gpu')
   prefs = {'download.default_directory' : '/'}
   chrome_options.add_experimental_option('prefs', prefs)


   driver = webdriver.Chrome(options=chrome_options)
   driver.get(url)
   download_path = '/home/Telegram-UserBot/'
   driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
   params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_path}}
   command_result = driver.execute("send_command", params)

   driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
   sleep(2)  # this might take a bit.
   await e.edit("Processing 50%")
   driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
   sleep(2) #Waiting for downloading
   
   await e.edit("Processing 90%")
   file = await bot.upload_file('carbon.png')
   await e.edit("Done!!")
   await bot.send_file(
         e.chat_id,
         file,
         reply_to=e.message.id,
           )
 
   os.remove('carbon.png')

HELPER.update({
      "carbon":"Beautify your code \n Usage: .carbon <text>"
})
HELPER.update({
    'setlang':".setlang <Lang> \
            \nUsage: It will set language for you carbon module "
})
  
