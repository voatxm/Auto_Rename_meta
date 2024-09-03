from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from helper.database import AshutoshGoswami24
from pyromod.exceptions import ListenerTimeout
from config import Txt, Config


# AUTH_USERS = Config.AUTH_USERS

ON = [
    [InlineKeyboardButton("𝐌𝐞𝐭𝐚𝐝𝐚𝐭𝐚 𝐎𝐧 ✅", callback_data="metadata_1")],
    [InlineKeyboardButton("𝐒𝐞𝐭 𝐂𝐮𝐬𝐭𝐨𝐦 𝐌𝐞𝐭𝐚𝐝𝐚𝐭𝐚", callback_data="cutom_metadata")],
]
OFF = [
    [InlineKeyboardButton("𝐌𝐞𝐭𝐚𝐝𝐚𝐭𝐚 𝐎𝐟𝐟 ❌", callback_data="metadata_0")],
    [InlineKeyboardButton("𝐒𝐞𝐭 𝐂𝐮𝐬𝐭𝐨𝐦 𝐌𝐞𝐭𝐚𝐝𝐚𝐭𝐚", callback_data="cutom_metadata")],
]


@Client.on_message(filters.private & filters.command("metadata"))
async def handle_metadata(bot: Client, message: Message):

    ms = await message.reply_text("**𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭...**", reply_to_message_id=message.id)
    bool_metadata = await AshutoshGoswami24.get_metadata(message.from_user.id)
    user_metadata = await AshutoshGoswami24.get_metadata_code(message.from_user.id)
    await ms.delete()
    if bool_metadata:

        return await message.reply_text(
            f"<b>𝐘𝐨𝐮𝐫 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐌𝐞𝐭𝐚𝐝𝐚𝐭𝐚:</b>\n\n➜ ```{user_metadata}``` ",
            reply_markup=InlineKeyboardMarkup(ON),
        )

    return await message.reply_text(
        f"<b>𝐘𝐨𝐮𝐫 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐌𝐞𝐭𝐚𝐝𝐚𝐭𝐚:</b>\n\n➜ ```{user_metadata}``` ",
        reply_markup=InlineKeyboardMarkup(OFF),
    )


@Client.on_callback_query(filters.regex(".*?(custom_metadata|metadata).*?"))
async def query_metadata(bot: Client, query: CallbackQuery):

    data = query.data

    if data.startswith("metadata_"):
        _bool = data.split("_")[1]
        user_metadata = await AshutoshGoswami24.get_metadata_code(query.from_user.id)

        if bool(eval(_bool)):
            await AshutoshGoswami24.set_metadata(query.from_user.id, bool_meta=False)
            await query.message.edit(
                f"<b>𝐘𝐨𝐮𝐫 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐌𝐞𝐭𝐚𝐝𝐚𝐭𝐚:</b>\n\n➜ ```{user_metadata}``` ",
                reply_markup=InlineKeyboardMarkup(OFF),
            )

        else:
            await AshutoshGoswami24.set_metadata(query.from_user.id, bool_meta=True)
            await query.message.edit(
                f"<b>𝐘𝐨𝐮𝐫 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐌𝐞𝐭𝐚𝐝𝐚𝐭𝐚:</b>\n\n➜ ```{user_metadata}``` ",
                reply_markup=InlineKeyboardMarkup(ON),
            )

    elif data == "cutom_metadata":
        await query.message.delete()
        try:
            try:
                metadata = await bot.ask(
                    text=Txt.SEND_METADATA,
                    chat_id=query.from_user.id,
                    filters=filters.text,
                    timeout=30,
                    disable_web_page_preview=True,
                )
            except ListenerTimeout:
                await query.message.reply_text(
                    "⚠️ 𝐄𝐫𝐫𝐨𝐫!!\n\n𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐭𝐢𝐦𝐞𝐝 𝐨𝐮𝐭.\n𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐛𝐲 𝐮𝐬𝐢𝐧𝐠 /metadata",
                    reply_to_message_id=query.message.id,
                )
                return
            print(metadata.text)
            ms = await query.message.reply_text(
                "**𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭...**", reply_to_message_id=metadata.id
            )
            await AshutoshGoswami24.set_metadata_code(
                query.from_user.id, metadata_code=metadata.text
            )
            await ms.edit("**𝐘𝐨𝐮𝐫 𝐌𝐞𝐭𝐚𝐝𝐭𝐚 𝐂𝐨𝐝𝐞 𝐒𝐞𝐭 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅**")
        except Exception as e:
            print(e)
