import asyncio
import json
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

# Замініть на ваш реальний токен від @BotFather
BOT_TOKEN = "8803038288:AAEDXA07ph_D04WH4tAcYIGLahb2wp6zj4E"
WEB_APP_URL = "https://davps2gogl-design.github.io/tg-mini-app/"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
  keyboard = InlineKeyboardMarkup(
      inline_keyboard=[
          [
              InlineKeyboardButton(
                  text="🟢 Купити темку «Трафік»",
                  web_app=WebAppInfo(url=WEB_APP_URL),
              )
          ]
      ]
  )
  await message.answer(
      "Вітаю! Натисніть кнопку нижче, щоб відкрити магазин темки:",
      reply_markup=keyboard,
  )


@dp.message(F.web_app_data)
async def handle_web_app_data(message: types.Message):
  data = json.loads(message.web_app_data.data)

  if data.get("item") == "темка_трафік":
    text = (
        "✅ **Ваше замовлення прийнято!**\n\n"
        "📦 **Товар:** Темка «Трафік»\n"
        "💰 **Сума:** 100 грн\n\n"
        "💳 **Реквізити для оплати:**\n"
        "`4149 0000 0000 0000`\n\n"
        "Після оплати надішліть скріншот чека сюди в чат!"
    )
    await message.answer(text, parse_mode="Markdown")


async def main():
  await dp.start_polling(bot)


if __name__ == "__main__":
  asyncio.run(main())
