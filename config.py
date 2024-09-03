import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","AshutoshGoswami24")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
    # -- FORCE_SUB_CHANNELS = ["BotzPW","AshuSupport","AshutoshGoswami24"] -- # 
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', 'AshutoshGoswami24,BotzPW').split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    PORT = int(os.environ.get("PORT", ""))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """<b>ʜᴇʟʟᴏ {} 
    
➻ ᴛʜɪs ɪs ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ʏᴇᴛ ᴘᴏᴡᴇʀғᴜʟ ʀᴇɴᴀᴍᴇ ʙᴏᴛ.
    
➻ ᴜsɪɴɢ ᴛʜɪs ʙᴏᴛ ʏᴏᴜ ᴄᴀɴ ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ ᴏғ ʏᴏᴜʀ ғɪʟᴇs.
    
➻ ᴛʜɪs ʙᴏᴛ ᴀʟsᴏ sᴜᴘᴘᴏʀᴛs ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴀɴᴅ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.
    
➻ ᴜsᴇ /tutorial ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ.</b>

<b>Bot Is Made By @AshutoshGoswami24</b>

<b><a href='https://github.com/AshutoshGoswami24/Auto-Rename-Bot'>AshutoshGoswami24/Auto-Rename-Bot.git</a></b>
"""
    
    FILE_NAME_TXT = """<b><u>SETUP AUTO RENAME FORMAT</u></b>

Use These Keywords To Setup Custom File Name

✓ `[episode]` :- To Replace Episode Number
✓ `[quality]` :- To Replace Video Resolution

<b>➻ Example :</b> <code> /autorename Naruto Shippuden S01[episode] [quality][Dual Audio] @AshutoshGoswami24</code>

<b>➻ Your Current Auto Rename Format :</b> <code>{format_template}</code> """
    
    ABOUT_TXT = f"""<b>🤖 My Name :</b>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>🧑‍💻 Developer :</b> <a href='https://t.me/AshutoshGoswami24'>PandaWep</a>
    
<b>ʙᴏᴛ ɪs ᴏᴡɴᴇᴅ ʙʏ :</b> @AshutoshGoswami24"""

    
    THUMBNAIL_TXT = """<b><u>🖼️  HOW TO SET THUMBNAIL</u></b>
    
<b>⦿ ʏᴏᴜ ᴄᴀɴ ᴀᴅᴅ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ sɪᴍᴘʟʏ ʙʏ sᴇɴᴅɪɴɢ ᴀ ᴘʜᴏᴛᴏ ᴛᴏ ᴍᴇ....
    
⦿ /viewthumb - Use This Command To See Your Thumbnail
⦿ /delthumb - Use This Command To Delete Your Thumbnail</b>"""

    CAPTION_TXT = """<b><u>📝  HOW TO SET CAPTION</u></b>
    
<b>⦿ /set_caption - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ sᴇᴛ ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ
⦿ /see_caption - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ sᴇᴇ ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ
⦿ /del_caption - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ</b>"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
┣⪼ 🥺 joine Plz: @AshutoshGoswami24
╰━━━━━━━━━━━━━━━➣ </b>"""
    
    
    DONATE_TXT = """<b>🥲 ᴛʜᴀɴᴋs ғᴏʀ sʜᴏᴡɪɴɢ ɪɴᴛᴇʀᴇsᴛ ɪɴ ᴅᴏɴᴀᴛɪᴏɴ! ❤️</b>
    
<b>ɪғ ʏᴏᴜ ʟɪᴋᴇ ᴍʏ ʙᴏᴛs & ᴘʀᴏᴊᴇᴄᴛs, ʏᴏᴜ ᴄᴀɴ 🎁 ᴅᴏɴᴀᴛᴇ ᴍᴇ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ғʀᴏᴍ 𝟷𝟶 ʀs ᴜᴘᴛᴏ ʏᴏᴜʀ ᴄʜᴏɪᴄᴇ.</b>
    
<b>ᴍʏ ᴜᴘɪ - PandaWep@ybl</b> """
    
    HELP_TXT = """<b>Hey</b> {}
    
Join @AshutoshGoswami24 To Help """





