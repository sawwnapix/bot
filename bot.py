from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

TOKEN = "8063443001:AAGfcxOJ66bNKzOQtWAbcEU3qt5K1sIjDXA"  # Твой токен

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Главное меню (кнопки внизу)
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.row(
    KeyboardButton("About Me🚀"), KeyboardButton("Donate💵")
).row(
    KeyboardButton("My Account 🏆"), KeyboardButton("My Modules🔮")
)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.answer("Привет! Выбери нужный раздел:", reply_markup=main_menu)

# Обработчик нажатия на About Me🚀
@dp.message_handler(lambda message: message.text == "About Me🚀")
async def about_me(message: types.Message):
    text = """📝 **Name:** Yegor  
😀 **Birthday:** 05.02  
📆 **Age:** 12 years  
😀 **From:** Ukraine  

🗣 **Languages:**  
  - 🇷🇺 Russian: Native Speaker  
  - 🇺🇦 Ukrainian: C1  
  - 🇮🇹 Italian: B2  
  - 🇬🇧 English: B1  
  - 🇫🇷 French: A1  

🏆 **Hobbies:**  
  - 🖼 Drawing  
  - 🎮 Playing video games  
  - ⌨️ Learning Python  
  - 🎧 Listening to music  

⛓️ [**Referral links: click here**](https://t.me)  
🔕 [**If you have spam ban: click here**](https://t.me)  

💫 The userbot I use - **Heroku 🪐**"""
    await message.answer_photo("https://0x0.st/s/LzSAEoh6JqKuRhSQFc0Nmw/8KXu.jpg", caption=text, parse_mode="Markdown")

# Обработчик нажатия на Donate💵
@dp.message_handler(lambda message: message.text == "Donate💵")
async def donate(message: types.Message):
    text = "Привет! Тут ты можешь поддержать меня 💵"
    buttons = InlineKeyboardMarkup(row_width=1)
    buttons.add(
        InlineKeyboardButton("Crypto Bot⚡", url="http://t.me/send?start=IVGoorKHazNg"),
        InlineKeyboardButton("Crypto Testnet🔮", url="http://t.me/CryptoTestnetBot?start=IVg3HKXvOzhK"),
        InlineKeyboardButton("xRocket 🚀 (Only USDT)", url="https://t.me/xrocket?start=inv_eMkKSHKf5FwmKcM")
    )
    await message.answer_photo("https://0x0.st/s/sdHpMNoENecyuJoiHZ2f4w/8XC2.jpg", caption=text, reply_markup=buttons)

# Обработчик нажатия на My Account 🏆
@dp.message_handler(lambda message: message.text == "My Account 🏆")
async def my_account(message: types.Message):
    text = "Мой аккаунт: @zerixgod @neprivet\nМогу помочь вам с вопросом, если разбираюсь в сфере, связанной с вашим вопросом."
    await message.answer_photo("https://0x0.st/s/493FO1NdH2OJlGL4PoIdng/8K8q.jpg", caption=text)

# Обработчик нажатия на My Modules 🔮
@dp.message_handler(lambda message: message.text == "My Modules🔮")
async def my_modules(message: types.Message):
    text = "🚀Мой канал с модулями для Юзербота Hikka: @angellmodules"
    await message.answer_photo("https://0x0.st/s/Wnvcaj71mPP0rwb_A7_KMQ/8K8a.jpg", caption=text)

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
