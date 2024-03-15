from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong
from info import ADMINS, LOG_CHANNEL, USERNAME
from database.users_chats_db import db
from database.aks_files import Media, get_files_db_size
from utils import get_size, temp
from Script import script
from datetime import datetime
import psutil
import time

@Client.on_message(filters.new_chat_members & filters.group)
async def save_group(bot, message):
    check = [u.id for u in message.new_chat_members]
    if temp.ME in check:
        if (str(message.chat.id)).startswith("-100") and not await db.get_chat(message.chat.id):
            total=await bot.get_chat_members_count(message.chat.id)
            user = message.from_user.mention if message.from_user else "Dear" 
            group_link = await message.chat.export_invite_link()
            await bot.send_message(LOG_CHANNEL, script.NEW_GROUP_TXT.format(temp.B_LINK, message.chat.title, message.chat.id, message.chat.username, group_link, total, user), disable_web_page_preview=True)  
            await db.add_chat(message.chat.id, message.chat.title)
            btn = [[
                InlineKeyboardButton('🦸 sᴜᴘᴘᴏʀᴛ 🦸', url=USERNAME)
            ]]
            reply_markup=InlineKeyboardMarkup(btn)
            await bot.send_message(
                chat_id=message.chat.id,
                text=f"<b><u>💥 ᴛʜᴀɴᴋ ʏᴏᴜ ꜰᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ɪɴ ɢʀᴏᴜᴘ</u>\n\n❗️ᴅᴏɴ’ᴛ ꜰᴏʀɢᴇᴛ ᴛᴏ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ❗️\n\n⚠️ ᴍᴜꜱᴛ ᴅᴏ ᴀʟʟ ᴛʜᴇꜱᴇ ꜱᴇᴛᴛɪɴɢꜱ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ꜱᴏ ᴛʜᴀᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʟᴏᴏᴋꜱ ᴘᴏᴡᴇʀꜰᴜʟ ᴀɴᴅ ʏᴏᴜ ᴄᴀɴ ᴇᴀʀɴ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏɴᴇʏ 🤑\n\n/set_shortner - ᴛᴏ ꜱᴇᴛ ꜱʜᴏʀᴛᴇɴᴇʀ ғᴏʀ 𝟷ꜱᴛ ᴠᴇʀɪғʏ\n/set_shortner_2 - ᴛᴏ ꜱᴇᴛ ꜱʜᴏʀᴛᴇɴᴇʀ ғᴏʀ 𝟸ɴᴅ ᴠᴇʀɪғʏ\n/set_time - ᴛᴏ ꜱᴇᴛ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴛɪᴍᴇ\n/set_log_channel - ᴛᴏ ꜱᴇᴛ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ғᴏʀ ᴜꜱᴇʀꜱ ᴅᴀᴛᴀ\n/set_tutorial - ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ ʟɪɴᴋ\n/set_caption - ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ғɪʟᴇ ᴄᴀᴘᴛɪᴏɴ\n/set_fsub - ᴛᴏ ꜱᴇᴛ ʏᴏᴜʀ ғᴏʀᴄᴇ ꜱᴜʙꜱᴄʀɪʙᴇ ᴄʜᴀɴɴᴇʟ\n/remove_fsub - ᴛᴏ ʀᴇᴍᴏᴠᴇ ғᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ ɪᴅ\n/details - ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴅᴇᴛᴀɪʟꜱ\n\n😘 𝐼𝑓 𝑦𝑜𝑢 𝑑𝑜 𝑎𝑙𝑙 𝑡ℎ𝑖𝑠 𝑡ℎ𝑒𝑛 𝑦𝑜𝑢𝑟 𝑔𝑟𝑜𝑢𝑝 𝑤𝑖𝑙𝑙 𝑏𝑒 𝑣𝑒𝑟𝑦 𝑐𝑜𝑜𝑙...</b>",
                reply_markup=reply_markup
            )

@Client.on_message(filters.command('leave') & filters.user(ADMINS))
async def leave_a_chat(bot, message):
    r = message.text.split(None)
    if len(message.command) == 1:
        return await message.reply('<b>ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ʟɪᴋᴇ ᴛʜɪꜱ `/leave -100******`</b>')
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "ɴᴏ ʀᴇᴀꜱᴏɴ ᴘʀᴏᴠɪᴅᴇᴅ..."
    try:
        chat = int(chat)
    except:
        chat = chat
    try:
        btn = [[
            InlineKeyboardButton('🦸 ᴏᴡɴᴇʀ 🦸', url=USERNAME)
        ]]
        reply_markup=InlineKeyboardMarkup(btn)
        await bot.send_message(
            chat_id=chat,
            text=f'<b>😞 ʜᴇʟʟᴏ ᴅᴇᴀʀ,\n\nᴍʏ ᴏᴡɴᴇʀ ʜᴀꜱ ᴛᴏʟᴅ ᴍᴇ ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ɢʀᴏᴜᴘ ꜱᴏ ɪ ɢᴏ 😔\n\n🚫 ʀᴇᴀꜱᴏɴ ɪꜱ - <code>{reason}</code>\n\nɪꜰ ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴀᴅᴅ ᴍᴇ ᴀɢᴀɪɴ ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ᴏᴡɴᴇʀ 👇</b>',
            reply_markup=reply_markup,
        )
        await bot.leave_chat(chat)
        await db.delete_chat(chat)
        await message.reply(f"<b>ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ʟᴇꜰᴛ ꜰʀᴏᴍ ɢʀᴏᴜᴘ - `{chat}`</b>")
    except Exception as e:
        await message.reply(f'<b>🚫 ᴇʀʀᴏʀ - `{e}`</b>')

@Client.on_message(filters.command('groups') & filters.user(ADMINS))
async def list_groups(bot, message):
    msg = await message.reply('<b>Searching...</b>')
    chats = await db.get_all_chats()
    total_chats = 0
    out = "Chats saved in the database are:\n\n"
    async for chat in chats:
        out += f"**Title:** {chat['title']}\n**ID:** `{chat['id']}`"
        if chat['chat_status']['is_disabled']:
            out += ' (Disabled Chat)'
        out += '\n\n'
        total_chats += 1
    out += f"Total Chats: {total_chats}\n"
    try:
        await msg.edit_text(out)
    except MessageTooLong:
        with open('chats.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('chats.txt', caption="List of chats")
        await msg.delete()
        os.remove('chats.txt')
        
@Client.on_message(filters.command('stats') & filters.user(ADMINS) & filters.incoming)
async def get_ststs(bot, message):
    users = await db.total_users_count()
    premium = await db.all_premium_users_count()
    groups = await db.total_chat_count()
    size = get_size(await db.get_db_size())
    free = get_size(536870912)
    files = await Media.count_documents()
    db2_size = get_size(await get_files_db_size())
    db2_free = get_size(536870912)
    uptime = time.strftime("%Hh %Mm %Ss", time.gmtime(time.time() - time.time()))
    ram = psutil.virtual_memory().percent
    cpu = psutil.cpu_percent()
    await message.reply_text(script.STATUS_TXT.format(users, premium, groups, size, free, files, db2_size, db2_free, uptime, ram, cpu))
