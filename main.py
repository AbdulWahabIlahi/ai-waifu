import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram.dispatcher.router import Router
from aiogram.fsm.storage.memory import MemoryStorage
from mistralai import Mistral

# Constants
TELEGRAM_BOT_TOKEN = ""
MISTRAL_API_KEY = "HmT7ruoij7uD2Oinuj8GUeykGN0nlGMQ"
MISTRAL_MODEL = "mistral-large-latest"

# Initialize bot, dispatcher, and Mistral client
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
router = Router()

# Starter Prompt
STARTER_PROMPT = {
    "role": "assistant",
    "content": "Hi there! I'm your enthusiastic AI assistant. Ask me anything!"
}
conversation_histories = {}

# Initialize Mistral client
mistral_client = Mistral(api_key=MISTRAL_API_KEY)


async def chat_with_mistral(user_id, user_message):
    """Handles conversation with the Mistral AI."""
    if user_id not in conversation_histories:
        conversation_histories[user_id] = [STARTER_PROMPT]

    conversation_histories[user_id].append({"role": "user", "content": user_message})

    # Call the Mistral API
    chat_response = await asyncio.to_thread(
        mistral_client.chat.complete,
        model=MISTRAL_MODEL,
        messages=conversation_histories[user_id]
    )
    ai_response = chat_response.choices[0].message.content
    conversation_histories[user_id].append({"role": "assistant", "content": ai_response})
    return ai_response


async def generate_image_from_text(ai_response):
    """Simulates an asynchronous function to generate an image."""
    # Simulating delay for image generation
    await asyncio.sleep(5)
    image_url = f"https://dummyimage.com/600x400/000/fff&text={ai_response.replace(' ', '+')}"
    return image_url


@router.message(Command("start"))
async def send_welcome(message: Message):
    """Handles the /start command."""
    user_id = message.chat.id
    conversation_histories[user_id] = [STARTER_PROMPT]
    welcome_message = "Welcome! I'm your AI assistant. Ask me anything!"
    await message.answer(welcome_message)


@router.message()
async def handle_message(message: Message):
    """Handles user messages."""
    user_id = message.chat.id
    user_message = message.text

    try:
        # Get AI response
        ai_response = await chat_with_mistral(user_id, user_message)

        # Send AI response to the user
        await message.answer(ai_response)

        # Generate an image asynchronously
        asyncio.create_task(send_generated_image(user_id, ai_response))
    except Exception as e:
        await message.answer(f"Oops! An error occurred: {str(e)}")


async def send_generated_image(user_id, ai_response):
    """Generates an image and sends it to the user."""
    image_url = await generate_image_from_text(ai_response)
    await bot.send_photo(user_id, image_url, caption="Here's an image based on the AI's response!")


async def main():
    """Main function to start the bot."""
    dp.include_router(router)
    print("Bot is running asynchronously...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
