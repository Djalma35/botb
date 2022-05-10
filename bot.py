import time
import telebot
import os
from id_user import UserID
from instagram import Insta, instafoto
from ip import IP
from gercnpj import GeradorCNPJ
from gercpf import GeradorCPF
from portscan import scan
from placa import PLACA
from cep import CEP
from cnpj import ConCNPJ
from md5 import MD5
from gercns import GeradorCNS
from banks import BANKS
from bin import BIN
from ddd import DDD

tk = "seu Itoken"

bot = telebot.TeleBot(tk, parse_mode="markdown")


@bot.message_handler(commands=['start', 'help', 'comesar', 'acorda'])
def welcome(message):
    bot.reply_to(message, '*Olá, sou um bot feito em Python criado pelo @slayersh')

@bot.message_handler(commands=['id'])
def reply(message):
    bot.reply_to(message, UserID(message))

@bot.message_handler(commands=['insta'])
def Instagram(message):
    bot.reply_to(message, Insta(message))
    bot.send_photo(message.chat.id, instafoto(message))

@bot.message_handler(commands=['ip'])
def ConsultaIP(message):
    bot.reply_to(message, IP(message))

@bot.message_handler(commands=['gercnpj'])
def gerarCNPJ(message):
    bot.reply_to(message, '*Gerando, aguarde...*')
    bot.reply_to(message, GeradorCNPJ(message))

@bot.message_handler(commands=['gercpf'])
def gerarCPF(message):
    bot.reply_to(message, '*Gerando, aguarde...*')
    bot.reply_to(message, GeradorCPF(message))

@bot.message_handler(commands=['scan'])
def scanports(message):
    bot.reply_to(message, '*Aguarde isso pode demorar um pouco*')
    bot.reply_to(message, scan(message))

@bot.message_handler(commands=['placa'])
def placa_consulta(message):
    bot.reply_to(message, PLACA(message))

@bot.message_handler(commands=['cep'])
def ConsultaCEP(message):
    bot.reply_to(message, CEP(message))

@bot.message_handler(commands=['cnpj'])
def ConsultarCNPJ(message):
    bot.reply_to(message, ConCNPJ(message))

@bot.message_handler(commands=['md5'])
def md5Encode(message):
    bot.reply_to(message, MD5(message))

@bot.message_handler(commands=['gercns'])
def gerarCNS(message):
    bot.reply_to(message, '*Gerando, aguarde...*')
    bot.reply_to(message, GeradorCNS(message))

@bot.message_handler(commands=['banks'])
def ConsultarBANCO(message):
    bot.reply_to(message, BANKS(message))

@bot.message_handler(commands=['bin'])
def ConsultaBIN(message):
    bot.reply_to(message, BIN(message))

@bot.message_handler(commands=['ddd'])
def ConsultaDDD(message):
    bot.reply_to(message, DDD(message))

@bot.message_handler(commands=['yt'])
def download(message):
    bot.reply_to(message, '*Baixando, aguarde...*')
    url = message.text[4:]
    video = YouTube(url).streams.get_highest_resolution().download(skip_existing=False)
    file = open(video, 'rb')

    bot.send_video(message.chat.id, file, timeout=1000)
    file.close()
    os.remove(video)


while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        telebot.logger.error(e)
        time.sleep(15)
