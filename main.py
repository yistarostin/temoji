import telebot
import time
from tqdm import tqdm

bot = telebot.TeleBot("5064443225:AAEoREVk5gsCLoWS3mBnD7JuKjajDdyD87M")


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(content_types=["dice"])
def send_dice(message: telebot.types.Message):
    luck_count = 0
    TOTAL = 2
    for _ in tqdm(range(TOTAL)):
        got = bot.send_dice(
            message.chat.id, emoji=message.dice.emoji).dice.value
        # print(got)
        if (got - 1) % 21 == 0:  # [1, 22, 43, 64]
            luck_count += 1
        time.sleep(0.1)
    results = f"LUCK_COUNT:\t{luck_count}\nEXPECTED PROBABILITY: \t{4 / 64}\nACTUAL PROBABILTY: \t{luck_count / TOTAL}"
    print(results)
    bot.send_message(message.chat.id, text=(
        "```" + results + "```"), parse_mode="MarkdownV2")
    # exit()


bot.infinity_polling()
