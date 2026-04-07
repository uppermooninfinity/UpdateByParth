import random
from pyrogram.types import InlineKeyboardButton
from pyrogram.enums import ButtonStyle
import config
from Oneforall import app

# Premium Stickers
STICKERS = [6312260233171312151, 5433824103134530018, 5431445213233261748]

def btn(text, style=ButtonStyle.DEFAULT, **kwargs):
    premium_id = random.choice(STICKERS)
    return InlineKeyboardButton(
        text=text,
        icon_custom_emoji_id=premium_id,
        style=style,
        **kwargs
    )

def private_panel(_):
    buttons = [
        [btn(_["S_B_3"], url=f"https://t.me/{app.username}?startgroup=true", style=ButtonStyle.SUCCESS)], # Green
        [
            btn("ᴇʀᴇɴ ʏᴇᴀɢᴇʀ", url="https://t.me/toxication_infinity", style=ButtonStyle.PRIMARY), # Blue
            btn(_["S_B_2"], url=config.SUPPORT_CHAT, style=ButtonStyle.PRIMARY), 
        ],
        [btn(_["S_B_4"], callback_data="settings_back_helper", style=ButtonStyle.WARNING)], # Orange
        [
            btn(_["S_B_6"], url=config.SUPPORT_CHANNEL, style=ButtonStyle.DANGER), # Red
            btn(_["S_B_5"], url="https://t.me/docker_git_bit", style=ButtonStyle.PRIMARY)
        ],
    ]
    return buttons
