

from pyrogram import Client, idle, filters
from pyrogram.types import Message

API_ID = 293267
API_HASH = "e2fdafab7e98be46b74a57dca43"
#SESSION = "BQDJqkIASwhplzoHdEJUJx9Q8U1tVFnNsC_1Gl-YNQ3lsSeFrQjsjPElcNy2XE6twtVOpaVLYoOPdAYZCHuRU7KSrhURKQUbiVaiJmSME-aTHfcqx_30UpLo9mjTQaXb-IL_11bJwK0jweDBL8udG2a_zFci7pS71FpW158j0x1fVh7AOeqW3syOU_dYLHDQ0nNjzMhFel01p7xNbuGPY6oNYkG8wiUOzqfxvtsnUE7eZ-6UH7eLz2MhhRxdso8HmylVdqSd1ApZ3wEzIcjB9vPy2NBI1ddEty0WttB9hzyr1a9ONJcU-uMCWodUvdw8ugbpMp8qYxaNmxBCPl87CjAeqe9RXAAAAAGkd-4rAA"

#SESSION="BQGhN7YAuY8LdLZvtgjaYeexbBPa8GPZtY7KoXGV8_8alavr6t4TBdKdibhKQfDR2wrc3e6l-yKYYCm3_GZq-siCovX9d9hf85vnTYQh9oUinGLr745Li8Vu8mu3lxFFa1jA1W-8CN9-gEGHjvduNKoMlgoFRFBfOETWiJ3v5VjTEWITIFY6y26JTjCqVpdl8FhovZKfttGldms2bmt7hQmE49b6yIk4g0mNBCcBLYlJRjrhGT5Gjul7aiNagy0HJKm2epfJBKCTzmXcJor99cpsbAVt9xuQ6338yTC4yfSxzNyd_2z03jIg5gUkSY0HXLCEmM2nXYj1H2yoUDExqd0a0mlnAAAAAAFfdWJUAA"

SESSION=""

app = Client(
    "my account",
    API_ID,
    API_HASH,
    session_string=SESSION
)

@app.on_message(filters.chat(777000) & filters.text)
async def get_otp(_, message: Message):
    print(f"Message: {message.text}")

async def main():
    await app.start()
    print(f"name: {app.me.first_name} \nphone: {app.me.phone_number}")
    await idle()
    await app.stop()
