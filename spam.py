from discord_webhook import DiscordWebhook
import asyncio
from colorama import Fore, Back, Style
print(Fore.GREEN + """
| __      __      ___.   .__                   __       _________                                          |
|/  \    /  \ ____\_ |__ |  |__   ____   ____ |  | __  /   _____/__________    _____   _____   ___________ |
|\   \/\/   // __ \| __ \|  |  \ /  _ \ /  _ \|  |/ /  \_____  \\____ \__  \  /     \ /     \_/ __ \_  __  \|
| \        /\  ___/| \_\ \   Y  (  <_> |  <_> )    <   /        \  |_> > __ \|  Y Y  \  Y Y  \  ___/|  | \/|
|  \__/\  /  \___  >___  /___|  /\____/ \____/|__|_ \ /_______  /   __(____  /__|_|  /__|_|  /\___  >__|   |
|       \/       \/    \/     \/                   \/         \/|__|       \/      \/      \/     \/       |  
       """)
discrdwbhk = input("Webhook Link (if multiple separate by comma):")
cntnt = input("Content to spam:")
loop = input("Do you want to loop Y/N:")
def send():
    webhook = DiscordWebhook(url=discrdwbhk, rate_limit_retry=True, content=cntnt)
    response = webhook.execute()
while True:
    for i in "b":
        send()
send()
