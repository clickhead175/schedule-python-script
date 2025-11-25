import os
import requests
import time

# URL for Discord webhook
url = "https://canary.discord.com/api/v9/channels/1324315026768531466/messages"

# Payloads
payloads = [
    {"content": "BPSJ05A5UG claim red packet 🧧🧧🧧🎁🎁 Pepe Last 49 🎁"},
    {"content": "BTC Claim fast 8 people left 🎁 BPSJ05A5UG 🎁"},
    {"content": "BPGCKJ5GOV 😍 10$ last 13 peoples 💗"},
    {"content": "0.001 BTC 💗 😍 only for 216 💌 peoples BPVMGMZJP0"},
    {"content": "137 😍🎖 DOGE Tokens last 19 red packet 💥🧧 BPGCKJ5GOV"},
    {"content": "1.2 SOL 💗 For 121 peoples go claim 🎁🧧BPZHKLPEG9"},
    {"content": "BPSJ05A5UG claim red packet 🧧🧧🧧🎁🎁 Pepe Last 49 🎁"},
    {"content": "Best of luck for TON$ 💵🎉 BPYCHYLWT9"},
    {"content": "0.65 BNB$ 🎟💖 only for 69 peoples claim 🎫 fast BPVMGMZJP0"},
    {"content": "‎0.18 ETH ❣️💌 for 550 peoples go claim BPGCKJ5GOV"},
    {"content": "‎🎖GET some XRP$ 💥🎁 113 🎟 Red packets BPGCKJ5GOV"},
    {"content": "‎10000 NEIRO tokens 428 people can claim 🥳🧧 BPZHKLPEG9"},
    {"content": "‎‎18 USDT$ 🎁 ONLY For 41 peoples go claim fast Red packet 🎉 BPZHKLPEG9"},
    {"content": "‎‎‎738$ BNB BOX CODE 🎟🧧BPSJ05A5UG"},
    {"content": "‎‎‎‎BPYCHYLWT9 🧧🧧🧧🧧🎀🎁 25$"},
    {"content": "203 GUN 🎀 🧧🧧 171 people's can claim 🎟🎖red packet BPYCHYLWT9‎‎‎‎"},
    {"content": "‎‎‎‎red box 🎁 code NEIRO TOKENS 970$ 💌💜 BPYCHYLWT9"},
    {"content": "‎‎‎‎‎Best of luck for TON$ 💵🎉 BPYCHYLWT9"},
    {"content": "‎‎‎‎‎‎BPSJ05A5UG claim red packet 🧧🧧🧧🎁🎁 Pepe Last 49 🎁"},
    {"content": "‎‎‎‎‎‎‎BTC Claim fast 8 people left 🎁 BPSJ05A5UG 🎁"},
    {"content": "‎‎‎‎‎‎‎‎BPGCKJ5GOV 😍 10$ last 13 peoples 💗"},
    {"content": "0.001 BTC 💗 😍 only for 216 💌 peoples BPVMGMZJP0"},
    {"content": "0.65 BNB$ 🎟💖 only for 69 peoples claim 🎫 fast BPVMGMZJP0"},
    {"content": "‎‎‎‎‎‎BPSJ05A5UG claim red packet 🧧🧧🧧🎁🎁 Pepe Last 49 🎁"},
    {"content": "‎10000 NEIRO tokens 428 people can claim 🥳🧧 BPZHKLPEG9"},
    {"content": "‎‎18 USDT$ 🎁 ONLY For 41 peoples go claim fast Red packet 🎉 BPZHKLPEG9"},
    {"content": "‎‎‎738$ BNB BOX CODE 🎟🧧BPSJ05A5UG"},
    {"content": "‎‎‎‎BPYCHYLWT9 🧧🧧🧧🧧🎀🎁 25$"},
    {"content": "203 GUN 🎀 🧧🧧 171 people's can claim 🎟🎖red packet BPYCHYLWT9‎‎‎‎"}
    ]

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')


# Headers for the request
headers = {
    "Authorization": "examplekey=uiuhuihijubiiuncw9eNeDJQP0-w78y8"
}

# Add this to repeatedly post every hour
while True:
    for payload in payloads:
        res = requests.post(url, json=payload, headers=headers)
        print(f"Sent: {payload['content']}")
        time.sleep(30 * 62)  # Sleep for 62 minutes
