import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "26634100")
    API_HASH  = os.environ.get("API_HASH", "9ea49405d5a93e784114c469f5ce4bbd")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7504372339:AAGEAyLI5le3GIj0QnlJa3EJERj_Vl0Shgk") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","AshutoshGoswami24")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://zoey611870:5ErfLUWPKH44hkqK@cluster0.7doyqob.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://telegra.ph/file/8fe5276a43438e5390909.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1302933634').split()]
    # -- FORCE_SUB_CHANNELS = ["BotzPW","AshuSupport","AshutoshGoswami24"] -- # 
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', 'Yugen_Bots').split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002123409511"))
    PORT = int(os.environ.get("PORT", ""))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """Hello {} 
    
âž» This Is An Advanced And Yet Powerful Rename Bot.
    
âž» Using This Bot You Can Auto Rename Of Your Files.
    
âž» This Bot Also Supports Custom Thumbnail And Custom Caption.
    
âž» Use /tutorial Command To Know How To Use Me.

<b>Bot Is Made By @AshutoshGoswami24</b>

<b><a href='https://github.com/AshutoshGoswami24/Auto-Rename-Bot'>AshutoshGoswami24/Auto-Rename-Bot.git</a></b>
"""
    
    FILE_NAME_TXT = """<b><u>SETUP AUTO RENAME FORMAT</u></b>

Use These Keywords To Setup Custom File Name

âœ“ `[episode]` :- To Replace Episode Number
âœ“ `[quality]` :- To Replace Video Resolution

<b>âž» Example :</b> <code> /autorename Naruto Shippuden S01[episode] [quality][Dual Audio] @AshutoshGoswami24</code>

<b>âž» Your Current Auto Rename Format :</b> <code>{format_template}</code> """
    
    ABOUT_TXT = f"""<b>ðŸ¤– My Name :</b>
<b>ðŸ“ Language :</b> <a href='https://python.org'>Python 3</a>
<b>ðŸ“š Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>ðŸš€ Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>ðŸ§‘â€ðŸ’» Developer :</b> <a href='https://t.me/AshutoshGoswami24'>PandaWep</a>
    
<b>â™»ï¸ Bot Made By :</b> @AshutoshGoswami24"""

    
    THUMBNAIL_TXT = """<b><u>ðŸ–¼ï¸  HOW TO SET THUMBNAIL</u></b>
    
â¦¿ You Can Add Custom Thumbnail Simply By Sending A Photo To Me....
    
â¦¿ /viewthumb - Use This Command To See Your Thumbnail
â¦¿ /delthumb - Use This Command To Delete Your Thumbnail"""

    CAPTION_TXT = """<b><u>ðŸ“Â  HOW TO SET CAPTION</u></b>
    
â¦¿Â /set_caption - Use This Command To Set Your Caption
â¦¿ /see_caption - Use This Command To See Your Caption
â¦¿ /del_caption - Use This Command To Delete Your Caption"""

    PROGRESS_BAR = """<b>\n
â•­â”â”â”â”â°á´˜Ê€á´É¢Ê€á´‡ss Ê™á´€Ê€â±â”âž£
â”£âª¼ ðŸ—ƒï¸ SÉªá´¢á´‡: {1} | {2}
â”£âª¼ â³ï¸ Dá´É´á´‡ : {0}%
â”£âª¼ ðŸš€ Sá´©á´‡á´‡á´…: {3}/s
â”£âª¼ â°ï¸ Eá´›á´€: {4}
â”£âª¼ ðŸ¥º joine Plz: @AshutoshGoswami24
â•°â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”âž£ </b>"""
    
    
    DONATE_TXT = """<b>ðŸ¥² Thanks For Showing Interest In Donation! â¤ï¸</b>
    
If You Like My Bots & Projects, You Can ðŸŽ Donate Me Any Amount From 10 Rs Upto Your Choice.
    
<b>My UPI - PandaWep@ybl</b> """
    
    HELP_TXT = """<b>Hey</b> {}
    
Joine @AshutoshGoswami24 To Help """




