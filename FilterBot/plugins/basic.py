from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from FilterBot import Translation
from .filterbot import app

@app.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Dev', url='https://t.me/MaskedVirus'),
        InlineKeyboardButton('Project', url ='https://t.me/ProjectHackfreaks')
    ],[
        InlineKeyboardButton('Help', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(message.from_user.mention),
        reply_markup=reply_markup,
        parse_mode="markdown",
        reply_to_message_id=update.message_id
    )

@app.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home', callback_data='start'),
        InlineKeyboardButton('About', callback_data='about')
    ],[
        InlineKeyboardButton('Close', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="markdown",
        reply_to_message_id=update.message_id
    )

@app.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home', callback_data='start'),
        InlineKeyboardButton('Close', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="markdown",
        reply_to_message_id=update.message_id
    )
    
