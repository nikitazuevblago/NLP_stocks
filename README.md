# WARNING - IN RUSSIA THE PROJECT DOESN'T WORK BECAUSE CHATGPT API CAN'T BE ACCESSED VIA API WITHOUT PROXY AND TG BOT CAN'T BE RUNED WITH PROXY, SOON BUG WILL BE FIXED

# NLP_stocks

  Code stuff
1. Download libraries in requirements.txt by   ->    pip install -r requirements.txt
2. Create secret_key.py and locate it in the root of repository, there should be:
      api_key = 'chatGPT api key'
      api_key_finance = 'https://eodhd.com/login - api here'
      bot_token = "tg bot token"
   P.s. Instruction how to get your tg bot token -> https://helpdesk.bitrix24.com/open/17622486/#:~:text=If%20you%20already%20have%20a,get%20a%20new%20access%20token.
4. Run main.py
   1*. If you're in Russia then chatGPT api may not work without proxy, we would reccomend to download outline proxy app -> https://getoutline.org/get-started/#step-3
   you can find some ss keys here -> @OutlineVpnOfficial
5. Go to your tg bot

  Bot stuff
1. /set_balance 10000000
2. /request YOURDESIREDCOMPANYTICKER
