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
    {"content": "0.65 BNB$ 🎟💖 only for 69 peoples claim 🎫 fast BPVMGMZJP0"}
]

# Headers for the request
headers = {
    "Authorization": "MTA0MTQzODQ4NTA3ODM0Nzg2Ng.GpW-xJ.teEbOV5cYKFvyhirCRxfYr9-kcw9eNeDJQP0-w"
}

# Add this to repeatedly post every hour
while True:
    for payload in payloads:
        res = requests.post(url, json=payload, headers=headers)
        print(f"Sent: {payload['content']}")
        time.sleep(30 * 62)  # Sleep for 62 minutes
