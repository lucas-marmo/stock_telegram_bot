from flask import Flask, render_template, request, url_for
from telegram import Update, ForceReply, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
import yfinance as yf

app = Flask(__name__)

@app.route('/')
async def hello_world():
    bot = Bot(token='COMPLETAR')
    chat = #COMPLETAR
    #hola = await bot.sendMessage(chat_id=chat, text='Hola desde Flask!')
    return render_template("index.html")

@app.route('/precio/<accion>')
async def precio(accion):
    bot = Bot(token='COMPLETAR')
    chat = #COMPLETAR
    data = yf.download(accion, start="2023-07-31", end="2023-08-01")
    valor = str(data['Close'].iloc[-1])
    mensaje = f"El valor actual de {accion} es: {valor}"
    hola = await bot.sendMessage(chat_id=chat, text=mensaje)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)