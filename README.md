# Auto-FilterBot

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/swatv3nub/)


![Python Version](https://img.shields.io/badge/python-3.9-green?style=for-the-badge&logo=appveyor)
![Pyrogram Version](https://img.shields.io/badge/pyrogram-1.2.6-orange?style=for-the-badge&logo=appveyor)
![Database](https://img.shields.io/badge/database-mongo-orange?style=for-the-badge&logo=appveyor)
![Issues](https://img.shields.io/github/issues/swatv3nub/FilterBot?style=for-the-badge&logo=appveyor)
![Forks](https://img.shields.io/github/forks/swatv3nub/FilterBot?style=for-the-badge&logo=appveyor)
![Stars](https://img.shields.io/github/stars/swatv3nub/FilterBot?style=for-the-badge&logo=appveyor)
![LICENSE](https://img.shields.io/github/license/swatv3nub/FilterBot?style=for-the-badge&logo=appveyor)
![Contributors](https://img.shields.io/github/contributors/swatv3nub/FilterBot?style=for-the-badge&logo=appveyor)
![Repository Size](https://img.shields.io/github/repo-size/swatv3nub/FilterBot?style=for-the-badge&logo=appveyor)


Simple Auto Filter Bot Written in Python using the Pyrogram Library

Just Sent Any Text As Query It Will Search For All Connected Chat's Files In Its Mongo DataBase And Reply You With The Message Link As A Button


## Usage

**How To Use Me!**

• Add Me To Any Group
• Add Me To Your Desired Channel

**Promote Me with Full Rights**

Bot Commands (Works Only In Groups) :

    • `/add chat_id` Or `/add @Username`
    To Connect A Group With A Channel (Bot Should Be Admin With Full Previlages In Both Group And Channel)
     
    • `/del chat_id` Or `/del @Username`
    To disconnect A Group With A Channel
    
    • `/delall`
    This Command Will Disconnect All Connected Channel With The Group And Deletes All Its File From DataBase
    
    • `/settings`
    This Command Will Display You A Settings Pannel Instance Which Can Be Used To Twerk Bot's Settings Accordingly

        • `Channel` - Button Will Show You All The Connected Chats With The Group And Will Show Buttons Correspnding To There Order For Furthur Controls
            
        • `Filter Types` - Button Will Show You The 3 Filter Option Available In Bot. Pressing Each Buttons Will Either Enable or Disable Them And This Will Take Into Action As Soon As You Use Them Without The Need Of A Restart

        • `Configure` - Button Will Helps You To Change No. of Pages/ Buttons Per Page/ Total Result. It Also Provides Option To Enable/Disable For Showing Invite Link In Each Results
            
        • `Status` - Button Will Shows The Stats Of Your Channel

## Required Vars

• Your Bot Token From [@BotFather](http://www.telegram.dog/BotFather)

• Your APP ID And API Hash From [Telegram](http://www.my.telegram.org)

• Your User Session String Obtained From [@PyrogramStringBot](http://www.telegram.dog/PyrogramStringBot)

• Mongo DataBase URL Obtained From [MongoDB](http://www.mongodb.com)


## Deploy

### Deploy To Heroku

Heroku Deploy is Simple AF, Just Click the below button, Fill Vars, Click Deploy.

- [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/swatv3nub/FilterBot)

### Local Deploy
- `git clone https://github.com/swatv3nub/FilterBot`
- `cd FilterBot`
- `pip3 install -r requirements.txt`
- Edit The `config.py` as per the instruction given there.
- `python3 -m FilterBot`


## Support   
- Join Our Support Group For Support | Assistance
 
[![Join Support!](https://img.shields.io/badge/support-group-green?style=for-the-badge&logo=appveyor)](https://t.me/HackfreaksSupport)

- Join My Bots Channel For New and Unique Bots

[![Join Channel!](https://img.shields.io/badge/bots-channel-red?style=for-the-badge&logo=appveyor)](https://t.me/ProjectHackfreaks)


Report Bugs, Give Feature Requests There.   
Do Fork And Star The Repository If You Liked It.

## License

- [MIT LICENSE](https://github.com/swatv3nub/FilterBot/blob/Alpha/LICENSE)


## Credits

 - Thanks To Dan for the [Pyrogram Libary](https://github.com/pyrogram/pyrogram)
