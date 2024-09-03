import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserNotParticipant
from config import Config

FORCE_SUB_CHANNELS = Config.FORCE_SUB_CHANNELS


async def not_subscribed(_, __, message):
    for channel in FORCE_SUB_CHANNELS:
        try:
            user = await message._client.get_chat_member(channel, message.from_user.id)
            if user.status in {"kicked", "left"}:
                return True
        except UserNotParticipant:
            return True
    return False


@Client.on_message(filters.private & filters.create(not_subscribed))
async def forces_sub(client, message):
    not_joined_channels = []
    for channel in FORCE_SUB_CHANNELS:
        try:
            user = await client.get_chat_member(channel, message.from_user.id)
            if user.status in {"kicked", "left"}:
                not_joined_channels.append(channel)
        except UserNotParticipant:
            not_joined_channels.append(channel)

    buttons = [
        [
            InlineKeyboardButton(
                text=f"📢 𝐉𝐨𝐢𝐧 {channel.capitalize()} 📢", url=f"https://t.me/{channel}"
            )
        ]
        for channel in not_joined_channels
    ]
    buttons.append(
        [
            InlineKeyboardButton(
                text="✅ 𝐈 𝐀𝐦 𝐉𝐨𝐢𝐧𝐞𝐝 ✅", callback_data="check_subscription"
            )
        ]
    )

    text = "**𝐒𝐨𝐫𝐫𝐲, 𝐲𝐨𝐮'𝐫𝐞 𝐧𝐨𝐭 𝐣𝐨𝐢𝐧𝐞𝐝 𝐭𝐨 𝐚𝐥𝐥 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝 𝐜𝐡𝐚𝐧𝐧𝐞𝐥𝐬 😐. 𝐏𝐥𝐞𝐚𝐬𝐞 𝐣𝐨𝐢𝐧 𝐭𝐡𝐞 𝐮𝐩𝐝𝐚𝐭𝐞 𝐜𝐡𝐚𝐧𝐧𝐞𝐥𝐬 𝐭𝐨 𝐜𝐨𝐧𝐭𝐢𝐧𝐮𝐞**"
    await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))


@Client.on_callback_query(filters.regex("check_subscription"))
async def check_subscription(client, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    not_joined_channels = []

    for channel in FORCE_SUB_CHANNELS:
        try:
            user = await client.get_chat_member(channel, user_id)
            if user.status in {"kicked", "left"}:
                not_joined_channels.append(channel)
        except UserNotParticipant:
            not_joined_channels.append(channel)

    if not not_joined_channels:
        await callback_query.message.edit_text(
            "**𝐘𝐨𝐮 𝐡𝐚𝐯𝐞 𝐣𝐨𝐢𝐧𝐞𝐝 𝐚𝐥𝐥 𝐭𝐡𝐞 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝 𝐜𝐡𝐚𝐧𝐧𝐞𝐥𝐬. 𝐓𝐡𝐚𝐧𝐤 𝐲𝐨𝐮! 😊 /start 𝐧𝐨𝐰**"
        )
    else:
        buttons = [
            [
                InlineKeyboardButton(
                    text=f"📢 𝐉𝐨𝐢𝐧 {channel.capitalize()} 📢",
                    url=f"https://t.me/{channel}",
                )
            ]
            for channel in not_joined_channels
        ]
        buttons.append(
            [
                InlineKeyboardButton(
                    text="✅ 𝐈 𝐀𝐦 𝐉𝐨𝐢𝐧𝐞𝐝", callback_data="check_subscription"
                )
            ]
        )

        text = "**𝐘𝐨𝐮 𝐡𝐚𝐯𝐞𝐧'𝐭 𝐣𝐨𝐢𝐧𝐞𝐝 𝐚𝐥𝐥 𝐭𝐡𝐞 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝 𝐜𝐡𝐚𝐧𝐧𝐞𝐥𝐬. 𝐏𝐥𝐞𝐚𝐬𝐞 𝐣𝐨𝐢𝐧 𝐭𝐡𝐞𝐦 𝐭𝐨 𝐜𝐨𝐧𝐭𝐢𝐧𝐮𝐞. **"
        await callback_query.message.edit_text(
            text=text, reply_markup=InlineKeyboardMarkup(buttons)
        )
