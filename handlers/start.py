from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
I am 𝑻𝒆𝒔𝒍𝒂 𝑴𝒖𝒔𝒊𝒄𝑩𝒐𝒕 :- VC Music Player, an open-source bot that lets you play music in your Telegram groups.
For source code Join our support group @TeslaRobo_Chat.
/help to know my commands.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support 🆘", url="https://t.me/TeslaRobo_Chat"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🤴 Owner", url="https://t.me/Warning_MadBoy_is_Back"
                    ),
                    InlineKeyboardButton(
                        "⚜️ DEV", url="https://t.me/ItS_PRaNAv_Xd"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Add To Your Group 🎵", url="https://t.me/TeslaMusicRoBot?startgroup=true"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
