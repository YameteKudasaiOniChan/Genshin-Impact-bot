import asyncio, telebot, json, os, genshin, requests, shutil

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

cookies = {"ltuid": 012345678, "ltoken": "abcdefghijklmnop"} # log in to hoyolab account , press f12 / take ltoken and ltuid from storage/cookis 
client = genshin.Client(cookies)


async def info(UID):
    user = await client.get_genshin_user(UID)
    return user.json()


def update(user_id):
    info_file = open(f"data/{user_id}/info.json", "w")
    uid = open(f"data/{user_id}/UID", "r").read()
    data = asyncio.run(info(uid))
    with open(f"data/{user_id}/{user_id}.json", "w") as user_json:
        user_json.write(data)
    user_info = json.loads(data)
    user_info = user_info["info"]
    data = {
"UID": uid,
"Name": f'{user_info["nickname"]}',
"Server": f'{user_info["server"]}'
    }
    json.dump(data, info_file)