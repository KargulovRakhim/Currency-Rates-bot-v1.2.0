Currency Bot by @Kargulov_Rakhim
---
## What is it?

This bot provides information about currency rates. It's getting it from https://privatbank.ua.

Everything is configurable.

## How to configure?

Configurations available by changing values inside `config.json` file.

Settings:
 - botToken = BotAPI token that can be resolved from @BotFather.
 - currencyApiKey = API Key for privatbank.ua, can be resolved by registration process on the site.
 - currencyRates = array of currency pairs that will be fetched from currate.ru.

## How to run?

 - Install Python 3.0+ version
 - Adopt settings inside `config.json`.
 - In CLI type: python bot.py.
 - After that go to a dialog with bot, and pass '/start' command.
 - And select your interest currency rate;
 - U will get something like:
 ```
 Current currency rates are: 

  USD: 27.650
  EUR: 33,700
  RUR: 0.365

  Data was fetched from https://privatbank.ua
  Dev: https://t.me/Kargulov_Rakhim
 ```

## Info for developers
### Dependencies
 - https://github.com/axios/axios = http client that used to send request to currate.ru.
 - https://github.com/yagop/pyTelegramBotApi = wrapper for Telegram's BotAPI.# currency-Bot-by-Kargulov-from-RETk18-4