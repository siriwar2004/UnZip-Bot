# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/UnZip-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/UnZip-Bot



from pyrogram import Client
from Unzip.config import Config


app = Client(
    "unzip_bot",
    bot_token=Config.7766243249:AAHdGrwbIQXuiNbq1cYY871jmAa80mDVaSc,
    api_id=Config.25131273
,
    api_hash=Config.6b2715180a62e8c4fbcdde7d8b88787e,
    plugins=dict(root="Unzip")
)


print("🎊 I AM ALIVE 🎊  • Support @NT_BOTS_SUPPORT")
app.run()
