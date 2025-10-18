import telebot
import schedule
import time
from datetime import datetime

# Telegram sozlamalari
TOKEN = "8194820377:AAFLYln2J3MEbK2vgGcpMV3u3T6Bg7uayFA"  # BotFather'dan olingan token
CHAT_ID = "2035595180"  # O'zingizning Telegram ID'ingiz

bot = telebot.TeleBot(TOKEN)

# --- FANNING MA'LUMOTLARI ---
darslar = [
    # 1-FAN
    {"hafta": 1, "fan": "Ilmiy tadqiqot usullari va eksperimentni rejalashtirish", 
     "mavzu": "Ilmiy tadqiqot tushunchasi va maqsadi"},
    {"hafta": 2, "fan": "Ilmiy tadqiqot usullari va eksperimentni rejalashtirish", 
     "mavzu": "Ilmiy muammo, gipoteza va maqsad qo‘yish"},
    {"hafta": 3, "fan": "Ilmiy tadqiqot usullari va eksperimentni rejalashtirish", 
     "mavzu": "Tadqiqot metodlari: kuzatish, tajriba, tahlil"},
    # 2-FAN
    {"hafta": 4, "fan": "Ilmiy-tadqiqot metodologiyasi", 
     "mavzu": "Ilmiy metodologiya tushunchasi"},
    {"hafta": 5, "fan": "Ilmiy-tadqiqot metodologiyasi", 
     "mavzu": "Ilmiy izlanish bosqichlari"},
    {"hafta": 6, "fan": "Ilmiy-tadqiqot metodologiyasi", 
     "mavzu": "Ilmiy muammo va gipoteza"},
    # 3-FAN
    {"hafta": 7, "fan": "Patentshunoslik, litsenziyalash va sertifikatlash", 
     "mavzu": "Intellektual mulk tushunchasi"},
    {"hafta": 8, "fan": "Patentshunoslik, litsenziyalash va sertifikatlash", 
     "mavzu": "Patent huquqi asoslari"},
    {"hafta": 9, "fan": "Patentshunoslik, litsenziyalash va sertifikatlash", 
     "mavzu": "Patent olish tartibi"},
    # 4-FAN
    {"hafta": 10, "fan": "Qishloq xo‘jaligi mashinalari nazariyasi va hisobi", 
     "mavzu": "Mashina nazariyasiga kirish"},
    {"hafta": 11, "fan": "Qishloq xo‘jaligi mashinalari nazariyasi va hisobi", 
     "mavzu": "Mexanik tizimlarning turlari"},
    {"hafta": 12, "fan": "Qishloq xo‘jaligi mashinalari nazariyasi va hisobi", 
     "mavzu": "Harakat uzatish mexanizmlari"}
]

# --- HAR KUNI YUBORILADIGAN XABAR ---
def send_dars():
    hafta = datetime.now().isocalendar()[1] % 12  # hozirgi hafta
    dars = darslar[hafta - 1] if hafta <= len(darslar) else darslar[-1]

    message = (
        f"📅 {datetime.now().strftime('%d-%m-%Y')}\n"
        f"🕔 05:30 — Ertalabki dars\n\n"
        f"📘 *Fan:* {dars['fan']}\n"
        f"🎓 *Mavzu:* {dars['mavzu']}\n\n"
        "🧩 Bugungi topshiriq:\n"
        "- Konspekt yozing\n"
        "- 3 ta asosiy savol tayyorlang\n"
        "- O‘rganilgan materialdan 1 amaliy misol keltiring\n\n"
        "💡 Esda tuting: Har kuni kichik o‘qish — katta natija sari qadam!"
    )

    bot.send_message(2035595180, message, parse_mode="Markdown")

# Har kuni 05:30 da dars yuborish
schedule.every().day.at("21:46").do(send_dars)

bot.send_message(2035595180, "✅ Darslik Magistr bot ishga tushdi! Har kuni 18:00 da yangi mavzu yuboriladi.")

while True:
    schedule.run_pending()
    time.sleep(30)
