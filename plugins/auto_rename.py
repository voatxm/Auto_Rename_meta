from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from helper.database import AshutoshGoswami24

@Client.on_message(filters.private & filters.command("autorename"))
async def auto_rename_command(client, message):
    user_id = message.from_user.id

    # Extract the format from the command
    format_template = message.text.split("/autorename", 1)[1].strip()

    # Save the format template to the database
    await AshutoshGoswami24.set_format_template(user_id, format_template)

    await message.reply_text("**𝐀𝐮𝐭𝐨 𝐑𝐞𝐧𝐚𝐦𝐞 𝐅𝐨𝐫𝐦𝐚𝐭 𝐔𝐩𝐝𝐚𝐭𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲! ✅**")

@Client.on_message(filters.private & filters.command("setmedia"))
async def set_media_command(client, message):
    user_id = message.from_user.id    
    media_type = message.text.split("/setmedia", 1)[1].strip().lower()

    # Save the preferred media type to the database
    await AshutoshGoswami24.set_media_preference(user_id, media_type)

    await message.reply_text(f"**𝐌𝐞𝐝𝐢𝐚 𝐏𝐫𝐞𝐟𝐞𝐫𝐞𝐧𝐜𝐞 𝐒𝐞𝐭 𝐓𝐨 :** {media_type} ✅")






