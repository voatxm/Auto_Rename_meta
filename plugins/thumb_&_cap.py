from pyrogram import Client, filters
from helper.database import AshutoshGoswami24


@Client.on_message(filters.private & filters.command("set_caption"))
async def add_caption(client, message):
    if len(message.command) == 1:
        return await message.reply_text(
            "**𝐆𝐢𝐯𝐞 𝐓𝐡𝐞 𝐂𝐚𝐩𝐭𝐢𝐨𝐧\n\n𝐄𝐱𝐚𝐦𝐩𝐥𝐞 :- ```/set_caption 📕𝐍𝐚𝐦𝐞 ➠ : {filename} \n\n🔗 𝐒𝐢𝐳𝐞 ➠ : {filesize} \n\n⏰ 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧 ➠ : {duration}```**"
        )
    caption = message.text.split(" ", 1)[1]
    await AshutoshGoswami24.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("**𝐘𝐨𝐮𝐫 𝐂𝐚𝐩𝐭𝐢𝐨𝐧 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐀𝐝𝐝𝐞𝐝 ✅**")


@Client.on_message(filters.private & filters.command("del_caption"))
async def delete_caption(client, message):
    caption = await AshutoshGoswami24.get_caption(message.from_user.id)
    if not caption:
        return await message.reply_text("**You Don't Have Any Caption ❌**")
    await AshutoshGoswami24.set_caption(message.from_user.id, caption=None)
    await message.reply_text("**𝐘𝐨𝐮𝐫 𝐂𝐚𝐩𝐭𝐢𝐨𝐧 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐃𝐞𝐥𝐞𝐭𝐞𝐝 🗑️**")


@Client.on_message(filters.private & filters.command(["see_caption", "view_caption"]))
async def see_caption(client, message):
    caption = await AshutoshGoswami24.get_caption(message.from_user.id)
    if caption:
        await message.reply_text(f"**𝐘𝐨𝐮𝐫 𝐂𝐚𝐩𝐭𝐢𝐨𝐧 :**\n\n```{caption}```")
    else:
        await message.reply_text("**𝐘𝐨𝐮 𝐃𝐨𝐧'𝐭 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐂𝐚𝐩𝐭𝐢𝐨𝐧 ❌**")


@Client.on_message(filters.private & filters.command(["view_thumb", "viewthumb"]))
async def viewthumb(client, message):
    thumb = await AshutoshGoswami24.get_thumbnail(message.from_user.id)
    if thumb:
        await client.send_photo(chat_id=message.chat.id, photo=thumb)
    else:
        await message.reply_text("**𝐘𝐨𝐮 𝐃𝐨𝐧'𝐭 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 ❌**")


@Client.on_message(filters.private & filters.command(["del_thumb", "delthumb"]))
async def removethumb(client, message):
    await AshutoshGoswami24.set_thumbnail(message.from_user.id, file_id=None)
    await message.reply_text("**𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐃𝐞𝐥𝐞𝐭𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 🗑️**")


@Client.on_message(filters.private & filters.photo)
async def addthumbs(client, message):
    mkn = await message.reply_text("𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭 ...")
    await AshutoshGoswami24.set_thumbnail(
        message.from_user.id, file_id=message.photo.file_id
    )
    await mkn.edit("**𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐒𝐚𝐯𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅️**")
