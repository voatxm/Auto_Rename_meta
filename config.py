import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "9ea49405d5a93e784114c469f5ce4bbd")
    API_HASH  = os.environ.get("API_HASH", "26634100")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7504372339:AAGEAyLI5le3GIj0QnlJa3EJERj_Vl0Shgk") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","Yugen")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://zoey611870:5ErfLUWPKH44hkqK@cluster0.7doyqob.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://telegra.ph/file/8fe5276a43438e5390909.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1302933634').split()]
    # -- FORCE_SUB_CHANNELS = ["BotzPW","AshuSupport","AshutoshGoswami24"] -- # 
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', 'Yugen_Bots').split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002123409511"))
    PORT = int(os.environ.get("PORT", "8080"))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """𝐇𝐞𝐲, {mention} 
    
➻ 𝐓𝐡𝐢𝐬 𝐈𝐬 𝐀𝐧 𝐀𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐀𝐧𝐝 𝐘𝐞𝐭 𝐏𝐨𝐰𝐞𝐫𝐟𝐮𝐥 𝐑𝐞𝐧𝐚𝐦𝐞 𝐁𝐨𝐭.
    
➻ 𝐔𝐬𝐢𝐧𝐠 𝐓𝐡𝐢𝐬 𝐁𝐨𝐭 𝐘𝐨𝐮 𝐂𝐚𝐧 𝐀𝐮𝐭𝐨 𝐑𝐞𝐧𝐚𝐦𝐞 𝐎𝐟 𝐘𝐨𝐮𝐫 𝐅𝐢𝐥𝐞𝐬.
    
➻ 𝐓𝐡𝐢𝐬 𝐁𝐨𝐭 𝐀𝐥𝐬𝐨 𝐒𝐮𝐩𝐩𝐨𝐫𝐭𝐬 𝐂𝐮𝐬𝐭𝐨𝐦 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐀𝐧𝐝 𝐂𝐮𝐬𝐭𝐨𝐦 𝐂𝐚𝐩𝐭𝐢𝐨𝐧.
    
➻ 𝐔𝐬𝐞 /𝐭𝐮𝐭𝐨𝐫𝐢𝐚𝐥 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐓𝐨 𝐊𝐧𝐨𝐰 𝐇𝐨𝐰 𝐓𝐨 𝐔𝐬𝐞 𝐌𝐞.

"""
    
    FILE_NAME_TXT = """<b><u>𝐒𝐄𝐓𝐔𝐏 𝐀𝐔𝐓𝐎 𝐑𝐄𝐍𝐀𝐌𝐄 𝐅𝐎𝐑𝐌𝐀𝐓</u></b>

𝐔𝐬𝐞 𝐓𝐡𝐞𝐬𝐞 𝐊𝐞𝐲𝐰𝐨𝐫𝐝𝐬 𝐓𝐨 𝐒𝐞𝐭𝐮𝐩 𝐂𝐮𝐬𝐭𝐨𝐦 𝐅𝐢𝐥𝐞 𝐍𝐚𝐦𝐞

✓ `{episode}` :- 𝐓𝐨 𝐑𝐞𝐩𝐥𝐚𝐜𝐞 𝐄𝐩𝐢𝐬𝐨𝐝𝐞 𝐍𝐮𝐦𝐛𝐞𝐫
✓ `{quality}` :- 𝐓𝐨 𝐑𝐞𝐩𝐥𝐚𝐜𝐞 𝐕𝐢𝐝𝐞𝐨 𝐑𝐞𝐬𝐨𝐥𝐮𝐭𝐢𝐨𝐧

<b>➻ 𝐄𝐱𝐚𝐦𝐩𝐥𝐞 :</b> <code> /autorename Naruto Shippuden S01EP{episode} {quality}[Dual Audio] @PARADOX_EMPEROR</code>

<b>➻ 𝐘𝐨𝐮𝐫 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐀𝐮𝐭𝐨 𝐑𝐞𝐧𝐚𝐦𝐞 𝐅𝐨𝐫𝐦𝐚𝐭 :</b> <code>{format_template}</code> """
    
    ABOUT_TXT = f"""<b>🤖 My Name : </b>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
    
"""

    
    THUMBNAIL_TXT = """<b><u>𝐇𝐎𝐖 𝐓𝐎 𝐒𝐄𝐓 𝐓𝐇𝐔𝐌𝐁𝐍𝐀𝐈𝐋</u></b>
    
⦿ 𝐘𝐨𝐮 𝐂𝐚𝐧 𝐀𝐝𝐝 𝐂𝐮𝐬𝐭𝐨𝐦 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐒𝐢𝐦𝐩𝐥𝐲 𝐁𝐲 𝐒𝐞𝐧𝐝𝐢𝐧𝐠 𝐀 𝐏𝐡𝐨𝐭𝐨 𝐓𝐨 𝐌𝐞....
    
⦿ /viewthumb - 𝐔𝐬𝐞 𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐓𝐨 𝐒𝐞𝐞 𝐘𝐨𝐮𝐫 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥
⦿ /delthumb - 𝐔𝐬𝐞 𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐓𝐨 𝐃𝐞𝐥𝐞𝐭𝐞 𝐘𝐨𝐮𝐫 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥"""
    CAPTION_TXT = """<b><u>𝐇𝐎𝐖 𝐓𝐎 𝐒𝐄𝐓 𝐂𝐀𝐏𝐓𝐈𝐎𝐍</u></b>
    
⦿ /set_caption- 𝐔𝐬𝐞 𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐓𝐨 𝐒𝐞𝐭 𝐘𝐨𝐮𝐫 𝐂𝐚𝐩𝐭𝐢𝐨𝐧
⦿ /see_caption - 𝐔𝐬𝐞 𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐓𝐨 𝐒𝐞𝐞 𝐘𝐨𝐮𝐫 𝐂𝐚𝐩𝐭𝐢𝐨𝐧
⦿ /del_caption - 𝐔𝐬𝐞 𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐓𝐨 𝐃𝐞𝐥𝐞𝐭𝐞 𝐘𝐨𝐮𝐫 𝐂𝐚𝐩𝐭𝐢𝐨𝐧"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""
    
    
    DONATE_TXT = """<b>🥲 𝐓𝐡𝐚𝐧𝐤𝐬 𝐅𝐨𝐫 𝐒𝐡𝐨𝐰𝐢𝐧𝐠 𝐈𝐧𝐭𝐞𝐫𝐞𝐬𝐭 𝐈𝐧 𝐃𝐨𝐧𝐚𝐭𝐢𝐨𝐧! ❤️</b>
    
𝐈𝐟 𝐘𝐨𝐮 𝐋𝐢𝐤𝐞 𝐌𝐲 𝐁𝐨𝐭𝐬 & 𝐏𝐫𝐨𝐣𝐞𝐜𝐭𝐬, 𝐘𝐨𝐮 𝐂𝐚𝐧 🎁 𝐃𝐨𝐧𝐚𝐭𝐞 𝐌𝐞 𝐀𝐧𝐲 𝐀𝐦𝐨𝐮𝐧𝐭 𝐔𝐩𝐭𝐨 𝐘𝐨𝐮𝐫 𝐂𝐡𝐨𝐢𝐜𝐞.
    
<b>𝐌𝐲 𝐔𝐏𝐈 - `yugenbots@upi`</b> """
    
    HELP_TXT = """<b>𝐇𝐞𝐲</b> {mention}
    
𝐉𝐨𝐢𝐧 @Yugen_Bots_Support 𝐅𝐨𝐫 𝐇𝐞𝐥𝐩 """





