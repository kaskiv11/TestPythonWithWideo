from aiogram import Bot, Dispatcher, executor, types
import logging

logging.basicConfig(level=logging.INFO)

TOKEN = '6049505133:AAFtG_1EHzGJB04pYYxxkdhxbOOiFanG29Q'  # bot API token
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Hello! Type /link for links or /video for a video.')


@dp.message_handler(commands=['link'])
async def link_message(message: types.Message):
    link_list = ["https://www.britishbook.ua/", "https://en.wikipedia.org/wiki/Book",
                 "https://en.wikipedia.org/wiki/Book"]
    link_text = "\n".join(link_list)
    await message.answer(f"Here are some links:\n{link_text}")


@dp.message_handler(commands=['video'])
async def send_video(message: types.Message):
    video_url = 'video/Reading book.mp4'

    caption = "Check out this video!"

    try:
        with open(video_url, 'rb') as video_file:
            await message.answer_video(video=video_file, caption=caption)
    except Exception as e:
        logging.error(f"Error sending video: {e}")
        await message.answer("Failed to send the video. Please try again later!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
