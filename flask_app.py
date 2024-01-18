import datetime
from flask import Flask, render_template, request, url_for
from telegram import Update, ForceReply, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
import yfinance as yf

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)

@app.route('/')
async def hello_world():
    bot = Bot(token=app.config['TOKEN'])
    chat = app.config['CHAT_ID']
    #hola = await bot.sendMessage(chat_id=chat, text='Hola desde Flask!')
    return render_template("index.html")

@app.route('/precio/<accion>')
async def precio(accion):
    bot = Bot(token=app.config['TOKEN'])
    chat = app.config['CHAT_ID']
    fecha_inicio = (datetime.datetime.today() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    fecha_fin = datetime.datetime.today().strftime('%Y-%m-%d')
    data = yf.download(accion, start=fecha_inicio, end=fecha_fin)
    valor = str(round(data['Close'].iloc[-1], 2))
    mensaje = f"El valor actual de {accion} es u$s{valor}"
    hola = await bot.sendMessage(chat_id=chat, text=mensaje)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)