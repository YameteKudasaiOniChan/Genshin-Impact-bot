import asyncio, telebot, json, os, genshin, requests, shutil
from scripts import update

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

cookies = {"ltuid": 012345678, "ltoken": "abcdefghijklmnop"} # log in to hoyolab account , press f12 / take ltoken and ltuid from storage/cookis 
Bot_token = "" #telegram bot token can take it from @botfather

client = genshin.Client(cookies)
bot = telebot.TeleBot(Bot_token)

try:
    os.mkdir("data")
except:
    pass
# game
def get_uid(user_id):
    file = open(f"data/{user_id}/info.json",'r')
    data = json.loads(file.read())
    return data["UID"]

# bot
## /start
@bot.message_handler(commands=['start'])
def starter(message):
    bot.reply_to(message, f"Hello welcome to bot\nOwner: @Yamete_Kudasai_Oni_Chan\nDeveloper: @Yamete_Kudasai_Oni_Chan")

## /set_uid
@bot.message_handler(commands=['set_uid'])
def set_uid(message):
    try:
        try:
            os.mkdir(f"data/{message.from_user.id}")
        except:
            pass

        uid = message.text.split()
        uid = uid[1]
        print(uid)
        with open(f"data/{message.from_user.id}/UID","w") as file:
            file.write(uid)
            file.close()
        update(message.from_user.id)
        bot.reply_to(message, "UID successfully set")
    except:
        bot.reply_to(message, "Invalid UID\nPlease send the uid as:\n/set_uid 123456789")
## /me
@bot.message_handler(commands=['me'])
def me(message):
    try:
        update(message.from_user.id)
        with open(f"data/{message.from_user.id}/info.json",'r') as file:
            json_object = json.load(file)
        msg = f"""
Server  :  {json_object["Server"]}
Name  :  {json_object["Name"]}
ID  :  {json_object["UID"]}
"""
        bot.reply_to(message,msg)
    except:
        bot.reply_to(message, "No information was found about you \n :(")
## /Top_characters
@bot.message_handler(commands=['me'])
def Top_characters(message):
    try:
        os.mkdir(f"data/{message.from_user.id}/TopChar")

    except:
        bot.reply_to(message, "can't get characters")


bot.infinity_polling()