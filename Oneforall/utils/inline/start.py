import random
from pyrogram.types import InlineKeyboardButton
from pyrogram.enums import ButtonStyle
import config
from Oneforall import app

# Premium Stickers ki list (Alag-alag buttons ke liye)
STICKERS = [
    6312260233171312151, # Default
    5433824103134530018, # Star
    5431445213233261748, # Fire
    5431718873433095333, # Heart
    5443003051411513631, # Settings/Gear
    5431634752706954211  # Link/Globe
]

def btn(text, style=ButtonStyle.DEFAULT, **kwargs):
    """
    Premium Stickers aur Multi-color support ke saath optimized button function.
    """
    # Har baar ek random premium sticker uthayega
    premium_id = random.choice(STICKERS)
    try:
        return InlineKeyboardButton(
            text=text,
            icon_custom_emoji_id=premium_id,
            style=style,
            **kwargs
        )
    except TypeError:
        # Purane Pyrogram versions ke liye fallback
        return InlineKeyboardButton(text=text, **kwargs)

def start_panel(_):
    buttons = [
        [
            btn(_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true", style=ButtonStyle.SUCCESS),
            btn(_["S_B_2"], url=config.SUPPORT_CHAT, style=ButtonStyle.PRIMARY),
        ],
    ]
    return buttons

def private_panel(_):
    buttons = [
        [
            # Add to Group Button - Success (Green)
            btn(_["S_B_3"], url=f"https://t.me/{app.username}?startgroup=true", style=ButtonStyle.SUCCESS)
        ],
        [
            # Support & Channel - Primary (Blue) & Secondary (Grey)
            btn("ᴇʀᴇɴ ʏᴇᴀɢᴇʀ", url="https://t.me/toxication_infinity", style=ButtonStyle.PRIMARY),
            btn(_["S_B_2"], url=config.SUPPORT_CHAT, style=ButtonStyle.SECONDARY),
        ],
        [
            # Help/Settings - Warning (Yellow/Orange)
            btn(_["S_B_4"], callback_data="settings_back_helper", style=ButtonStyle.WARNING)
        ],
        [
            # Channel - Danger (Red)
            btn(_["S_B_6"], url=config.SUPPORT_CHANNEL, style=ButtonStyle.DANGER),
            btn(_["S_B_5"], url="https://t.me/docker_git_bit", style=ButtonStyle.PRIMARY)
        ],
        [
            # Special Website Button
            btn("「 ⌯ ᴜᴘᴘєʀϻσσɴ ᴛᴜηєꜱ ⌯ 」", url="https://uppermooninfinity.jo3.org/", style=ButtonStyle.SUCCESS)
        ],
    ]
    return buttons
