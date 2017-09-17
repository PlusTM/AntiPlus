# -*- coding: utf-8 -*-
import telebot
import logging
import json
import os
from telebot import util
import re
from random import randint
import random
import requests as req
import requests
import commands
import urllib2
import urllib
import telebot
import ConfigParser
import redis as r
import redis as redis
session = requests.session()
from telebot import types
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
token = '384180412:AAEuTGiNfdOyzcj-mtKBZshxB2uGX2GRI0s' #Token 
bot = telebot.TeleBot(token)
database = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
sudos = [198794027,264150062] #Sudo IDs
channels = -1001054519880
db = "https://api.telegram.org/bot{}/getMe?".format(token)
res = urllib.urlopen(db)
res_body = res.read()
parsed_json = json.loads(res_body.decode("utf-8"))
botid = parsed_json['result']['id']
botuser = parsed_json['result']['username']
bhash = "blocked:users:{}".format(botuser)

print "Launched>>>"

######################################################################################

def delmessage(token, chat_id, message_id):
	openurl = session.request('get', "https://api.telegram.org/bot{}/deletemessage?chat_id={}&message_id={}".format(token, chat_id, message_id), params=None, files=None, timeout=(3.5, 9999))
	
######################################################################################

#############################
# 			Keys			#
#############################

commadns = types.InlineKeyboardMarkup()
commadns.add(types.InlineKeyboardButton('Ƈσммαηɗѕ', callback_data='command'))
commadns.add(types.InlineKeyboardButton('Mємвєяѕ', callback_data='botmembers'))


commandlist = types.InlineKeyboardMarkup()
commandlist.add(types.InlineKeyboardButton('IƊ', callback_data='getid'), types.InlineKeyboardButton('HєIɗ', callback_data='heid'), types.InlineKeyboardButton('ƤαηєƖ', callback_data='getpanel'))
commandlist.add(types.InlineKeyboardButton('ƑƖтєя', callback_data='getfilter'), types.InlineKeyboardButton('UηƑƖтєя', callback_data='getunfilter'), types.InlineKeyboardButton('ƑιƖтєяLιѕт', callback_data='getfilters'))
commandlist.add(types.InlineKeyboardButton('Sєттιηgѕ', callback_data='getsettings'), types.InlineKeyboardButton('Ƙιcк', callback_data='kicked'), types.InlineKeyboardButton('ƊєƖ', callback_data='delmsg'))
commandlist.add(types.InlineKeyboardButton('SєтOωηєя', callback_data='setowners'), types.InlineKeyboardButton('ƊєƖOωηєя', callback_data='delowners'), types.InlineKeyboardButton('Ƥяσмσтє', callback_data='promote'))
commandlist.add(types.InlineKeyboardButton('Ɗємσтє', callback_data='demote'), types.InlineKeyboardButton('ƜєƖcσмє', callback_data='welcomes'), types.InlineKeyboardButton('Ƭιмє', callback_data='times'))
commandlist.add(types.InlineKeyboardButton('Lσνє', callback_data='love'), types.InlineKeyboardButton('LσƓσ', callback_data='logo'), types.InlineKeyboardButton('Mє', callback_data='me'))
commandlist.add(types.InlineKeyboardButton('ƘιcкMє', callback_data='kickme'), types.InlineKeyboardButton('Ƈяєαтє', callback_data='create'), types.InlineKeyboardButton('Ɛcнσ', callback_data='echo'))
commandlist.add(types.InlineKeyboardButton('Ɓαcк', callback_data='back'))


backs = types.InlineKeyboardMarkup()
backs.add(types.InlineKeyboardButton('Ɓαcк', callback_data='backs'))

back = types.InlineKeyboardMarkup()
back.add(types.InlineKeyboardButton('Ɓαcк', callback_data='back'))
#######################################################################################
def setting(gpslock):
	mediasetting = types.InlineKeyboardMarkup()	
	
	if database.get('text'+str(gpslock)):
		mediasetting.add(types.InlineKeyboardButton('Text', callback_data='untext'), types.InlineKeyboardButton('🔒', callback_data='untext'))
	else:
		mediasetting.add(types.InlineKeyboardButton('Text', callback_data='text'), types.InlineKeyboardButton('🔓', callback_data='text'))

	if database.get('photo'+str(gpslock)):
		mediasetting.add(types.InlineKeyboardButton('Photo', callback_data='unphoto'), types.InlineKeyboardButton('🔒', callback_data='unphoto'))
	else:
		mediasetting.add(types.InlineKeyboardButton('Photo', callback_data='photo'), types.InlineKeyboardButton('🔓', callback_data='photo'))
	
	if database.get('sticker'+str(gpslock)):
		mediasetting.add(types.InlineKeyboardButton('Sticker', callback_data='unsticker'), types.InlineKeyboardButton('🔒', callback_data='unsticker'))
	else:
		mediasetting.add(types.InlineKeyboardButton('Sticker', callback_data='sticker'), types.InlineKeyboardButton('🔓', callback_data='sticker'))

	if database.get('video'+str(gpslock)):
		mediasetting.add(types.InlineKeyboardButton('Video', callback_data='unvideo'), types.InlineKeyboardButton('🔒', callback_data='unvideo'))

	else:
		mediasetting.add(types.InlineKeyboardButton('Video', callback_data='video'), types.InlineKeyboardButton('🔓', callback_data='video'))

	if database.get('music'+str(gpslock)):
		mediasetting.add(types.InlineKeyboardButton('Music', callback_data='unmusic'), types.InlineKeyboardButton('🔒', callback_data='unmusic'))

	else:
		mediasetting.add(types.InlineKeyboardButton('Music', callback_data='music'), types.InlineKeyboardButton('🔓', callback_data='music'))

	if database.get('document'+str(gpslock)):
		mediasetting.add(types.InlineKeyboardButton('File', callback_data='unfile'), types.InlineKeyboardButton('🔒', callback_data='unfile'))
	else:
		mediasetting.add(types.InlineKeyboardButton('File', callback_data='file'), types.InlineKeyboardButton('🔓', callback_data='file'))
		
	#if database.get('locations'+str(gpslock)):
	#	mediasetting.add(types.InlineKeyboardButton('Locations', callback_data='unloc'), types.InlineKeyboardButton('🔒', callback_data='unloc'))
	#else:
	#	mediasetting.add(types.InlineKeyboardButton('Locations', callback_data='loc'), types.InlineKeyboardButton('🔓', callback_data='loc'))
		
	if database.get('spam'+str(gpslock)):
		mediasetting.add(types.InlineKeyboardButton('Spam', callback_data='unspam'), types.InlineKeyboardButton('🔒', callback_data='unspam'))
	else:
		mediasetting.add(types.InlineKeyboardButton('Spam', callback_data='spam'), types.InlineKeyboardButton('🔓', callback_data='spam'))
		
	mediasetting.add(types.InlineKeyboardButton('NextPage', callback_data='next'))
		
	return mediasetting
	
def setting2(gpslock2):
	mediasetting2 = types.InlineKeyboardMarkup()
	
	if database.get('contact'+str(gpslock2)):
		mediasetting2.add(types.InlineKeyboardButton('Contacts', callback_data='uncontact'), types.InlineKeyboardButton('🔒', callback_data='uncontact'))
	else:
		mediasetting2.add(types.InlineKeyboardButton('Contacts', callback_data='contact'), types.InlineKeyboardButton('🔓', callback_data='contact'))

	if database.get('link'+str(gpslock2)):
		mediasetting2.add(types.InlineKeyboardButton('Links', callback_data='unlink'), types.InlineKeyboardButton('🔒', callback_data='unlink'))
	else:
		mediasetting2.add(types.InlineKeyboardButton('Links', callback_data='link'), types.InlineKeyboardButton('🔓', callback_data='link'))
		
	if database.get('forward'+str(gpslock2)):
		mediasetting2.add(types.InlineKeyboardButton('Forward', callback_data='unforward'), types.InlineKeyboardButton('🔒', callback_data='unforward'))
	else:
		mediasetting2.add(types.InlineKeyboardButton('Forward', callback_data='forward'), types.InlineKeyboardButton('🔓', callback_data='forward'))
		
	if database.get('persian'+str(gpslock2)):
		mediasetting2.add(types.InlineKeyboardButton('Persian', callback_data='unpersian'), types.InlineKeyboardButton('🔒', callback_data='unpersian'))
	else:
		mediasetting2.add(types.InlineKeyboardButton('Persian', callback_data='persian'), types.InlineKeyboardButton('🔓', callback_data='persian'))
		
	if database.get('english'+str(gpslock2)):
		mediasetting2.add(types.InlineKeyboardButton('English', callback_data='unenglish'), types.InlineKeyboardButton('🔒', callback_data='unenglish'))
	else:
		mediasetting2.add(types.InlineKeyboardButton('English', callback_data='english'), types.InlineKeyboardButton('🔓', callback_data='english'))
		
	if database.get('filters'+str(gpslock2)):
		mediasetting2.add(types.InlineKeyboardButton('Filters', callback_data='unfilter'), types.InlineKeyboardButton('🔒', callback_data='unfilter'))
	else:
		mediasetting2.add(types.InlineKeyboardButton('Filters', callback_data='filters'), types.InlineKeyboardButton('🔓', callback_data='filters'))
		
	if database.get('caption'+str(gpslock2)):
		mediasetting2.add(types.InlineKeyboardButton('Caption', callback_data='uncaption'), types.InlineKeyboardButton('🔒', callback_data='uncaption'))
	else:
		mediasetting2.add(types.InlineKeyboardButton('Caption', callback_data='caption'), types.InlineKeyboardButton('🔓', callback_data='caption'))
		
	if database.get('username'+str(gpslock2)):
		mediasetting2.add(types.InlineKeyboardButton('UserName', callback_data='unuser'), types.InlineKeyboardButton('🔒', callback_data='unuser'))
	else:
		mediasetting2.add(types.InlineKeyboardButton('UserName', callback_data='username'), types.InlineKeyboardButton('🔓', callback_data='username'))
		
	if database.get('tag'+str(gpslock2)):
		mediasetting2.add(types.InlineKeyboardButton('Tag', callback_data='untag'), types.InlineKeyboardButton('🔒', callback_data='untag'))
	else:
		mediasetting2.add(types.InlineKeyboardButton('Tag', callback_data='tag'), types.InlineKeyboardButton('🔓', callback_data='tag'))
		
	mediasetting2.add(types.InlineKeyboardButton('Back', callback_data='backpage'))
	
	return mediasetting2

######################################################################################
	
@bot.message_handler(commands=['start'])
def start(message):
	s = bot.get_chat_member(channels, message.chat.id)
	if s.status == "member" or s.status == "creator" or s.status == "administrator":
		id = message.chat.id
		user = message.from_user.username
		database.sadd('startbot',id)
		bot.send_message(message.chat.id, '*AntiPlusBoT Started*\n`You Can See My Commands`', reply_markup=commadns, parse_mode="Markdown")
	else:
		bot.send_message(message.chat.id, "`برای استفاده از ربات باید در کانال ما جوین شوید`\n`ایدی کانال :` @PlusTM", reply_markup=channel, parse_mode="Markdown")


######################################################################################

@bot.message_handler(commands=['help'])
def help(msg):
	bot.send_message(msg.chat.id, '`You Can See My Commands`', reply_markup=commadns, parse_mode="Markdown")

######################################################################################
	
@bot.message_handler(commands=['fwd'])
def fwd(msg):
	try:
		if msg.from_user.id in sudos:
			gpid = "-1001118067690"
			bot.forward_message(gpid, msg.chat.id, msg.reply_to_message.message_id)
	except:
		print("Test")

######################################################################################
			
@bot.message_handler(commands=['rem'])
def adde(msg):
	if msg.from_user.id in sudos:
		if database.sismember("groups", msg.chat.id):
			database.srem("groups", msg.chat.id)
			bot.reply_to(msg, "👥Group > [ {} ] \nRemoved".format(msg.chat.id))
		else:
			bot.reply_to(msg, "👥Group > [ {} ] \nNoT Added".format(msg.chat.id))
	
######################################################################################

@bot.message_handler(commands=['setowner'])
def setowner(msg):
	if msg.from_user.id in sudos:
		if msg.reply_to_message:
			if database.sismember("owners"+str(msg.chat.id), msg.reply_to_message.from_user.id):
				bot.reply_to(msg, "👤ID > [ {} ] Already Added To Owners List".format(msg.reply_to_message.from_user.id))
			else:
				database.sadd("owners"+str(msg.chat.id), msg.reply_to_message.from_user.id)
				bot.reply_to(msg, "👤ID > [ {} ] Added To Owners List".format(msg.reply_to_message.from_user.id))
				
######################################################################################

@bot.message_handler(commands=['time'])
def time(msg):
	reqa = urllib2.Request('http://irapi.ir/time/')
	openera = urllib2.build_opener()
	fa = openera.open(reqa)
	parsed_jsona = json.loads(fa.read())
	ENtime = parsed_jsona['ENtime']
	ENdate = parsed_jsona['ENdate']
	FAdate = parsed_jsona['FAdate']
	timemenu = types.InlineKeyboardMarkup()
	timemenu.add(types.InlineKeyboardButton('🕐Time > {}'.format(ENtime), callback_data='entime'))
	timemenu.add(types.InlineKeyboardButton('📆Date > {}'.format(FAdate), callback_data='fadate'))
	timemenu.add(types.InlineKeyboardButton('📆ENDate > {}'.format(ENdate), callback_data='endate'))
	bot.reply_to(msg, "*Time And Date*".format(), reply_markup=timemenu, parse_mode="Markdown")

######################################################################################

@bot.message_handler(commands=['love'])
def love(msg):
	text1 = msg.text.split()[1]
	text2 = msg.text.split()[2]
	urllib.urlretrieve("http://www.iloveheartstudio.com/-/p.php?t={}%20%EE%BB%AE%20{}&bc=FFCBDB&tc=000000&hc=ff0000&f=c&uc=true&ts=true&ff=PNG&w=500&ps=sq".format(text1,text2), "love.png")
	bot.send_sticker(msg.chat.id, open('love.png'))
	os.remove('love.png')

######################################################################################
	
@bot.message_handler(commands=['me'])
def me(msg):
	if database.sismember("owners"+str(msg.chat.id), msg.from_user.id):
		bot.reply_to(msg, "👤You Are Group Owner".format())
	else:
		if msg.from_user.id in sudos:
			bot.reply_to(msg, "👤You Are My Sudo XD".format())
		else:
			if database.sismember("promote"+str(msg.chat.id), msg.from_user.id):
				bot.reply_to(msg, "👤You Are Group Promote".format())
			else:
				bot.reply_to(msg, "👤You Are Group Member".format())
				
######################################################################################

@bot.message_handler(commands=['panel'])
def panel(msg):
	if msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id) or database.sismember("promote"+str(msg.chat.id), msg.from_user.id):
		stats = database.scard('msg')
		groupss = database.scard('groups')
		members = database.scard('startbot')
		ownersgp = database.scard('owners'+str(msg.chat.id))
		promotes = database.scard('promote'+str(msg.chat.id))
		channel = types.InlineKeyboardMarkup()
		channel.add(types.InlineKeyboardButton('Members > {}'.format(members), callback_data='botmembers'))
		channel.add(types.InlineKeyboardButton('Owners > {}'.format(ownersgp), callback_data='ownerss'))
		channel.add(types.InlineKeyboardButton('Promote > {}'.format(promotes), callback_data='promotess'))
		channel.add(types.InlineKeyboardButton('Groups > {}'.format(groupss), callback_data='gps'))
		channel.add(types.InlineKeyboardButton('🌐Channel🌐', url='https://telegram.me/PlusTM'))
		bot.reply_to(msg, "👥Group Stats >".format(stats,groupss), reply_markup=channel)

######################################################################################

#@bot.message_handler(commands=['resmsgs'])
#def add(msg):
#	if msg.from_user.id in sudos:
#		msgs = msg.message_id
#		database.srem('msgs', msg.chat.id)
#		bot.reply_to(msg, "All Message Reseted NoW".format())

######################################################################################

#@bot.message_handler(commands=['resgps'])
#def add(msg):
#	if msg.from_user.id in sudos:
#		database.srem('groups', msg.chat.id)
#		bot.reply_to(msg, "All Groups Reseted NoW".format())

######################################################################################

@bot.message_handler(commands=['whois'])
def whois(msg):
	try:
		res = "https://api.pwrtelegram.xyz/bot{}/getChat?chat_id={}".format(token,msg.text.split()[1]) #API ghat mibashad:|
		opener = urllib2.build_opener()
		f = opener.open(res)                                                                    
		parsed_json = json.loads(f.read())                                                      
		id = parsed_json["result"]["id"]
		username = parsed_json["result"]["username"]
		frist = parsed_json["result"]["first_name"]
		bot.reply_to(msg, "Name > [{}]\nID > [{}]\nUser > [@{}]".format(frist,id,username))
	except:
		bot.reply_to(msg, "Error!\nThis ID For Group But This CMD For Users Or /whois UserName/ID")
	
######################################################################################

@bot.message_handler(commands=['gpinfo'])
def gpinfo(msg):
	try:
		res = "https://api.pwrtelegram.xyz/bot{}/getChat?chat_id={}".format(token,msg.chat.id) #API ghat mibashad:|
		opener = urllib2.build_opener()
		f = opener.open(res)                                                                    
		parsed_json = json.loads(f.read())                                                      
		id = parsed_json["result"]["id"]
		title = parsed_json["result"]["title"]
		about = parsed_json["result"]["about"]
		gpusers = parsed_json["result"]["participants_count"]
		bot.reply_to(msg, "GroupInfo >\nName > [{}]\nID > [{}]\nMembers > [{}]\nAbout >\n[{}]".format(title,id,gpusers,about))
	except:
		bot.reply_to(msg, "Error!")
		
######################################################################################

@bot.message_handler(commands=['logo'])
def logo(msg):
	try:
		text1 = msg.text.split()[1]
		text2 = msg.text.split()[2]
		bot.reply_to(msg, "Please Wait...")
		res1 = "http://logo.irapi.ir/create/{}/{}".format(text1,text2) #API ghat mibashad:|
		opener = urllib2.build_opener()
		f = opener.open(res1)
		parsed_json = json.loads(f.read())
		logos = parsed_json["url"]
		urllib.urlretrieve("http://{}".format(logos), "logo.png")
		bot.send_sticker(msg.chat.id, open('logo.png'))
		bot.send_photo(msg.chat.id, open('logo.png'), caption="Your LoGo\n@PlusTM")
		os.remove('logo.png')
	except:
		bot.reply_to(msg, "Error!\nYou Can Send 100 To 144")
	
######################################################################################

@bot.message_handler(commands=['tarikh'])
def tarikh(msg):
	try:
		text1 = msg.text.split()[1]
		res1 = "https://api.feelthecode.xyz/convertdate/?date={}".format(text1)
		opener = urllib2.build_opener()
		f = opener.open(res1)
		parsed_json = json.loads(f.read())
		tarikh = parsed_json["jalali_date"]
		bot.reply_to(msg, "{}".format(tarikh))
	except:
		print("Error!")
	
######################################################################################

@bot.message_handler(commands=['date'])
def date(msg):
	try:
		urllib.urlretrieve("https://api.feelthecode.xyz/sticker/date/".format(), "date.png")
		bot.send_sticker(msg.chat.id, open('date.png'))
		os.remove('date.png')
	except:
		print("Error!")
	
######################################################################################

@bot.message_handler(commands=['insta'])
def instagram(msg):
	try:
		text1 = msg.text.split()[1]
		res1 = "https://instagram.com/{}/?__a=1".format(text1)
		opener = urllib2.build_opener()
		f = opener.open(res1)
		parsed_json = json.loads(f.read())
		bio = (parsed_json["user"]["biography"] or '*****')
		followers = parsed_json["user"]["followed_by"]["count"]
		following = (parsed_json["user"]["follows"]["count"] or '*****')
		name = (parsed_json["user"]["full_name"] or '*****')
		id = (parsed_json["user"]["id"] or '*****')
		is_private = parsed_json["user"]["is_private"]
		pic_url = parsed_json["user"]["profile_pic_url_hd"]
		username = (parsed_json["user"]["username"] or '*****')
		fb = (parsed_json["user"]["connected_fb_page"] or '*****')
		urllib.urlretrieve("{}".format(pic_url), "pic.png")
		bot.send_photo(msg.chat.id, open('pic.png'), caption="Biografi > {}\nFollowers > {}\nFollowing > {}\nName > {}\nID > {}\nUserName > {}\nFaceBooK > {}".format(bio, followers, following, name, id, username, fb))
		os.remove('pic.png')
	except:
		print("Error!")

######################################################################################

@bot.message_handler(commands=['down'])
def instagramdown(msg):
	try:
		text1 = msg.text.split()[1]
		res1 = "http://api.mosydev.ir/instagram/?url={}".format(text1) #API ghat mibashad:|
		opener = urllib2.build_opener()
		f = opener.open(res1)
		parsed_json = json.loads(f.read())
		url = parsed_json["url"]
		urllib.urlretrieve("{}".format(url), "insta.png")
		bot.send_photo(msg.chat.id, open('insta.png'), caption="Channel > [@PlusTM]")
		os.remove('insta.png')
	except:
		print("Error!")

######################################################################################

@bot.message_handler(commands=['voice'])
def voice(msg):
	try:
		text1 = msg.text.split()[1]
		url="http://irapi.ir/farsireader/?text={}".format(text1) #API ghat mibashad:|
		bot.send_voice(msg.chat.id,url,caption="Voice > [{}]".format(text1))
	except:
		print("Error!")
		
######################################################################################

@bot.message_handler(commands=['promote'])
def promote(msg):
	if msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id):
		if msg.reply_to_message:
			if database.sismember("promote"+str(msg.chat.id), msg.reply_to_message.from_user.id):
				bot.reply_to(msg, "👤ID > [ {} ] Already Added To Promote List".format(msg.reply_to_message.from_user.id))
			else:
				database.sadd("promote"+str(msg.chat.id), msg.reply_to_message.from_user.id)
				bot.reply_to(msg, "👤ID > [ {} ] Added To Promote List".format(msg.reply_to_message.from_user.id))
				
######################################################################################

@bot.message_handler(commands=['delowner'])
def delowner(msg):
	if msg.from_user.id in sudos:
		if msg.reply_to_message:
			database.srem("owners"+str(msg.chat.id), msg.reply_to_message.from_user.id)
			bot.reply_to(msg, "👤ID > [ {} ] Removed The Owner List".format(msg.reply_to_message.from_user.id))

######################################################################################

@bot.message_handler(commands=['demote'])
def demote(msg):
	if msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id):
		if msg.reply_to_message:
			database.srem("promote"+str(msg.chat.id), msg.reply_to_message.from_user.id)
			bot.reply_to(msg, "👤ID > [ {} ] Removed The Promote List".format(msg.reply_to_message.from_user.id))

######################################################################################

@bot.message_handler(commands=['id'])
def id(msg):
	if msg.from_user.id:
		id = msg.chat.id
		ids = msg.from_user.id
		ax = bot.get_user_profile_photos(ids)
		number = ax.total_count
		file = ax.photos[0][2].file_id
		text = "👤UserID > [ {} ]\n👥GroupID > [ {} ]".format(msg.from_user.id,id)
		bot.send_photo(msg.chat.id, file, caption='{}'.format(text))
		#bot.reply_to(msg, "👤UserID > [ {} ]\n👥GroupID > [ {} ]".format(msg.from_user.id,id))

######################################################################################

@bot.message_handler(commands=['creator'])
def creator(msg):
	bot.reply_to(msg, "AntiPlus\nنوشته شده توسط :\n@HajiNitro\n@PlusTM\nآدرس سورس ربات :\nhttps://github.com/PlusTM/AntiPlus\nستاره یادتون نره :)".format())

######################################################################################

@bot.message_handler(commands=['heid'])
def heid(msg):
	if msg.from_user.id:
		try:
			id = msg.chat.id
			bot.reply_to(msg, "👤UserID > [ {} ]".format(msg.reply_to_message.from_user.id,id))
		except:
			bot.reply_to(msg, "Just By Reply To User Message :)".format())

######################################################################################

@bot.message_handler(commands=['kick'])
def kick(msg):
	if msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id) or database.sismember("promote"+str(msg.chat.id), msg.from_user.id):
		try:
			id = msg.chat.id
			bot.kick_chat_member(msg.chat.id, msg.reply_to_message.from_user.id)
			bot.reply_to(msg, "User [{}] Kicked!".format(msg.reply_to_message.from_user.id))
		except:
			bot.reply_to(msg, "Just By Reply To User Message :)".format())

######################################################################################

@bot.message_handler(commands=['kickme'])
def kickme(msg):
	if msg.from_user.id:
		try:
			id = msg.chat.id
			#bot.reply_to(msg, "User [{}] Kicked! By Self".format(msg.from_user.id))
			bot.kick_chat_member(msg.chat.id, msg.from_user.id)
		except:
			bot.reply_to(msg, "I Can NoT Kick You:|".format())

######################################################################################

@bot.message_handler(commands=['setwlc'])
def setwlc(msg):
	ids = msg.chat.id
	database.delete("gpwlc","{}".format(ids))
	owners = database.sismember('owners'+str(ids), '{}'.format(msg.from_user.id))
	if str(owners) == 'True':
		database.hset("gpwlc","{}".format(ids),msg.text.replace('/setwlc ',''))
		bot.reply_to(msg, "👥Group Welcome Seted!".format())

######################################################################################
			
@bot.message_handler(commands=['del'])
def delete(msg):
	if msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id) or database.sismember("promote"+str(msg.chat.id), msg.from_user.id):
		if msg.reply_to_message:
			delmessage(token, msg.chat.id, msg.reply_to_message.message_id)
			delmessage(token, msg.chat.id, msg.message_id)
	
######################################################################################

@bot.message_handler(content_types=['new_chat_member'])
def welcome(msg):
	id = msg.from_user.id
	channels = types.InlineKeyboardMarkup()
	channels.add(types.InlineKeyboardButton('🌐Channel🌐', url='https://telegram.me/PlusTM'))
	text = database.hget("gpwlc","{}".format(msg.chat.id))
	bot.reply_to(msg, "{}".format(text), reply_markup=channels)
		
######################################################################################
	
@bot.message_handler(content_types=['left_chat_member'])
def welcome(msg):
	id = msg.from_user.id
	channels = types.InlineKeyboardMarkup()
	channels.add(types.InlineKeyboardButton('🌐Channel🌐', url='https://telegram.me/PlusTM'))
	bot.reply_to(msg, "User [{}] Bye Bye:)".format(id), reply_markup=channels)
		
######################################################################################
	
@bot.message_handler(commands=['settings'])
def locks(msg):
	if database.sismember("groups", msg.chat.id):
		if msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id) or database.sismember("promote"+str(msg.chat.id), msg.from_user.id):
			try:
				if database.get(msg.from_user.id):
					bot.reply_to(msg, "Please Wait For {} Sec".format(database.ttl(msg.from_user.id)))
				else:
					bot.send_message(msg.chat.id, "👥Group Settings >".format(), reply_markup=setting(msg.chat.id))
			except:
				#bot.send_message(msg.chat.id, "👥Group Settings :".format(database), reply_markup=setting(msg.chat.id))
				database.setex(msg.from_user.id, 60, True)
				
######################################################################################

@bot.message_handler(commands=['create'])
def create(msg):
	if msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id) or database.sismember("promote"+str(msg.chat.id), msg.from_user.id):
		try:
			if msg.from_user.id:
				text2 = msg.text.split()[2]
				text3 = msg.text.split()[3]
				text1 = msg.text.split()[1]
				st = url='{}'.format(text3)
				create = types.InlineKeyboardMarkup()
				create.add(types.InlineKeyboardButton('{}'.format(text2), st))
				bot.reply_to(msg, "{}".format(text1), reply_markup=create)
			else:
				bot.reply_to(msg, "_|_".format())
		except:
			bot.reply_to(msg, "Error!".format())

@bot.message_handler(commands=['echo'])
def echo(msg):
    if msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id) or database.sismember("promote"+str(msg.chat.id), msg.from_user.id):
		try:
			if database.get(msg.from_user.id):
				text = msg.text.replace('/echo ','')
				bot.reply_to(msg, "Please Wait For {} Sec".format(database.ttl(msg.from_user.id)))
				#bot.kick_chat_member(msg.chat.id, msg.from_user.id)
			else:
				bot.reply_to(msg, "{}".format(text,database))
		except:
			text = msg.text.replace('/echo ','')
			bot.reply_to(msg, "{}".format(text,database))
			database.setex(msg.from_user.id, 60, True)

######################################################################################	

@bot.message_handler(commands=['filter'])
def filter(msg):
    if msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id):
		text = msg.text.replace('/filter ','')
		filters = database.sadd("filters", text)
		bot.reply_to(msg, "{} Added To Filter List".format(text))
		
######################################################################################

@bot.message_handler(commands=['unfilter'])
def unfilter(msg):
    if msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id):
		try:
			text = msg.text.replace('/unfilter ','')
			filters = database.srem("filters", text)
			bot.reply_to(msg, "{} Removed!".format(text))
		except:
			bot.reply_to(msg, "{} NoT Filter".format(text))
		
######################################################################################	

@bot.message_handler(commands=['filterlist'])
def filterlist(msg):
	if msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id) or database.sismember("promote"+str(msg.chat.id), msg.from_user.id):
		try:
			i = 0
			for id in database.smembers("filters"):
				message = "{} - {}".format(i,id)
				i = i + 1
			bot.reply_to(msg, "Filter List >\n{}".format(message))
		except:
			bot.reply_to(msg, "Filter List Is Empty".format())

######################################################################################
		
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	print call
	if database.sismember("groups", call.message.chat.id):
		if call.from_user.id in sudos or database.sismember("owners"+str(call.message.chat.id), call.from_user.id):
			gplink = call.message.chat.id
			if call.data.startswith("untext"):
				database.delete('text'+str(gplink)) 
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Text has been UnLocked")

			if call.data.startswith("text"):
				database.set('text'+str(gplink), True)
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Text has been Locked !") 

			if call.data.startswith("unphoto"):
				database.delete('photo'+str(gplink))
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Photo has been UnLocked !") 

			if call.data.startswith("photo"):
				database.set('photo'+str(gplink), True)
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Photo has been Locked ") 
				
			if call.data.startswith("unsticker"):
				database.delete('sticker'+str(gplink))
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Sticker has been UnLocked !") 

			if call.data.startswith("sticker"):
				database.set('sticker'+str(gplink),True)
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Sticker has been Locked !") 	
				
			if call.data.startswith("unvideo"):
				database.delete('video'+str(gplink))
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Video has been UnLocked !") 

			if call.data.startswith("video"):
				database.set('video'+str(gplink), True)
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Video has been Locked !") 


			if call.data.startswith("unmusic"):
				database.delete('music'+str(gplink))
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting(gplink)) 
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Music has been UnLocked !") 

			if call.data.startswith("music"):
				database.set('music'+str(gplink),True)
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Music has been Locked !") 

			if call.data.startswith("unfile"):
				database.delete('document'+str(gplink))
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="File has been UnLocked !") 

			if call.data.startswith("file"):
				database.set('document'+str(gplink),True)
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="File has been Locked !") 

			#if call.data.startswith("unloc"):
			#	database.delete('Locations'+str(gplink))
			#	bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting(gplink))
			#	bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Locations has been UnLocked") 

			#if call.data.startswith("loc"):
			#	database.set('Locations'+str(gplink),True)
			#	bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting(gplink))
			#	bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Locations has been Locked !")  
					
			if call.data.startswith("uncontact"):
				database.delete('contact'+str(gplink))
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting2(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Contacts has been UnLocked !")
		 
			if call.data.startswith("contact"):
				database.set('contact'+str(gplink),True) 
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting2(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Contacts has been Locked !")

			if call.data.startswith("unlink"):
				database.delete('link'+str(gplink)) 
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting2(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Link has been UnLocked")

			if call.data.startswith("link"):
				database.set('link'+str(gplink), True)
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting2(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Link has been Locked !") 
				
			if call.data.startswith("unforward"):
				database.delete('forward'+str(gplink)) 
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting2(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Forward has been UnLocked")

			if call.data.startswith("forward"):
				database.set('forward'+str(gplink), True)
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting2(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Forward has been Locked !") 
				
			if call.data.startswith("unpersian"):
				database.delete('persian'+str(gplink)) 
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting2(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Persian has been UnLocked")

			if call.data.startswith("persian"):
				database.set('persian'+str(gplink), True)
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting2(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Persian has been Locked !") 
				
			if call.data.startswith("unenglish"):
				database.delete('english'+str(gplink)) 
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting2(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="English has been UnLocked")

			if call.data.startswith("english"):
				database.set('english'+str(gplink), True)
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting2(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="English has been Locked !") 
				
			if call.data.startswith("unfilter"):
				database.delete('filters'+str(gplink)) 
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting2(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Filter has been UnLocked")

			if call.data.startswith("filters"):
				database.set('filters'+str(gplink), True)
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting2(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Filter has been Locked !") 
				
			if call.data.startswith("uncaption"):
				database.delete('caption'+str(gplink)) 
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting2(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Caption has been UnLocked")

			if call.data.startswith("caption"):
				database.set('caption'+str(gplink), True)
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting2(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Caption has been Locked !") 
				
			if call.data.startswith("unuser"):
				database.delete('username'+str(gplink)) 
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting2(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="UserName has been UnLocked")

			if call.data.startswith("username"):
				database.set('username'+str(gplink), True)
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting2(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="UserName has been Locked !") 
				
			if call.data.startswith("untag"):
				database.delete('tag'+str(gplink)) 
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting2(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Tag has been UnLocked")

			if call.data.startswith("tag"):
				database.set('tag'+str(gplink), True)
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting2(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Tag has been Locked !") 
				
			if call.data.startswith("unspam"):
				database.delete('spam'+str(gplink)) 
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Spam has been UnLocked")

			if call.data.startswith("spam"):
				database.set('spam'+str(gplink), True)
				bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=setting(gplink))
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Spam has been Locked !") 
				
			if call.data == "msgss":
				bot.answer_callback_query(callback_query_id=call.id,text="All Msgs")
				
			if call.data == "gps":
				bot.answer_callback_query(callback_query_id=call.id,text="All Groups")
				
			if call.data == "ownerss":
				bot.answer_callback_query(callback_query_id=call.id,text="All Group Owners")
				
			if call.data == "promotess":
				bot.answer_callback_query(callback_query_id=call.id,text="All Group Promote")
				
			if call.data == "next":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='👥Group Settings >', reply_markup=setting2(gplink))
				
			if call.data == "backpage":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='👥Group Settings >', reply_markup=setting(gplink))

			if call.data == "endate":
				bot.answer_callback_query(callback_query_id=call.id,text="📆ENDate📆")
				
			if call.data == "fadate":
				bot.answer_callback_query(callback_query_id=call.id,text="📆Date📆")
				
			if call.data == "entime":
				bot.answer_callback_query(callback_query_id=call.id,text="🕐Time🕐")
				
			if call.data == "command":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ƈσммαηɗѕ Lιѕт >", reply_markup=commandlist, parse_mode="Markdown")
				bot.answer_callback_query(callback_query_id=call.id,text="Commands List")
				
			if call.data == "getid":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Ɠєт Ƴσυя IƊ Aηɗ ƤяσfιƖє Aηɗ ƓяσυρIƊ*\n`[/]id`", reply_markup=backs, parse_mode="Markdown")
				bot.answer_callback_query(callback_query_id=call.id,text="Help ID")
				
			if call.data == "heid":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Ɠєт Uѕєя IƊ Ɓу RєρƖу*\n`[/]heid`", reply_markup=backs, parse_mode="Markdown")
				bot.answer_callback_query(callback_query_id=call.id,text="Help HeID")
				
			if call.data == "getpanel":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Ɠєт ƁσƬ Iηfσ(Ɠяσυρѕ/Oωηєяѕ/Ƥяσмσтѕ...)*\n`[/]panel`", reply_markup=backs, parse_mode="Markdown")
				bot.answer_callback_query(callback_query_id=call.id,text="Help Panel")
				
			if call.data == "getfilter":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*ƑιƖтєя Ƴσυя Ɯσяɗ Ƒσя ƊєƖєтє*\n`[/]filter [Text]`", reply_markup=backs, parse_mode="Markdown")
				bot.answer_callback_query(callback_query_id=call.id,text="Help Filter")
				
			if call.data == "getunfilter":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*UηƑιƖтєя Ƴσυ Ɯσяɗ*\n[/]`unfilter [Text]`", reply_markup=backs, parse_mode="Markdown")
				bot.answer_callback_query(callback_query_id=call.id,text="Help UnFilter")
				
			if call.data == "getfilters":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Sнσω ƑιƖтєяLιѕт*\n`[/]filterlist`", reply_markup=backs, parse_mode="Markdown")
				bot.answer_callback_query(callback_query_id=call.id,text="Help FilterList")
				
			if call.data == "getsettings":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Sнσω Ɠяσυρ Sєттιηgѕ*\n`[/]settings`", reply_markup=backs, parse_mode="Markdown")
				bot.answer_callback_query(callback_query_id=call.id,text="Help Settings")
				
			if call.data == "kicked":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Ƙιcк Uѕєя Ƒяσм Ɠяσυρ Ɓу RєρƖу*\n`[/]kick`", reply_markup=backs, parse_mode="Markdown")
				bot.answer_callback_query(callback_query_id=call.id,text="Help Kick")
				
			if call.data == "delmsg":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*ƊєƖєтє Mєѕѕαgє Ɓу RєρƖу*\n`[/]del`", reply_markup=backs, parse_mode="Markdown")
				bot.answer_callback_query(callback_query_id=call.id,text="Help Delete Message")
				
			if call.data == "setowners":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Sєт Ɠяσυρ Oωηєя Ɓу RєρƖу*\n`[/]setowner`", reply_markup=backs, parse_mode="Markdown")
				bot.answer_callback_query(callback_query_id=call.id,text="Help SetOwner")
				
			if call.data == "delowners":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*ƊєƖ Ɠяσυρ Oωηєя Ɓу RєρƖу*\n`[/]delowner`", reply_markup=backs, parse_mode="Markdown")
				bot.answer_callback_query(callback_query_id=call.id,text="Help DelOwner")
				
			if call.data == "promotes":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Sєт Ɠяσυρ Ƥяσмσтє Ɓу RєρƖу*\n`[/]promote`", reply_markup=backs, parse_mode="Markdown")
				bot.answer_callback_query(callback_query_id=call.id,text="Help Promote")
				
			if call.data == "demote":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*ƊєƖ Ɠяσυρ Ƥяσмσтє Ɓу RєρƖу*\n`[/]demote`", reply_markup=backs, parse_mode="Markdown")
				bot.answer_callback_query(callback_query_id=call.id,text="Help Demote")
				
			if call.data == "welcomes":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Sєт Ɠяσυρ ƜєƖcσмє*\n`[/]setwlc`", reply_markup=backs, parse_mode="Markdown")
				bot.answer_callback_query(callback_query_id=call.id,text="Help Welcome")
				
			if call.data == "times":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Ɠєт Iяαη Ƭιмє Aηɗ Ɗαтє*\n`[/]time`", reply_markup=backs, parse_mode="Markdown")
				bot.answer_callback_query(callback_query_id=call.id,text="Help Time")
				
			if call.data == "love":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Ƈяєαтє Lσνє Sтιcкєя*\n`[/]love [Text] [Text]`", reply_markup=backs, parse_mode="Markdown")
				bot.answer_callback_query(callback_query_id=call.id,text="Help Love")
				
			if call.data == "logo":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Ƈяєαтє Ƴσυя LσƓσ*\n`[/]logo [Number(100-144)] [Text]`", reply_markup=backs, parse_mode="Markdown")
				bot.answer_callback_query(callback_query_id=call.id,text="Help LoGo")
				
			if call.data == "me":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Ɠєт Ƴσυя Rαηк Ƭσ Ɠяσυρ*\n`[/]me`", reply_markup=backs, parse_mode="Markdown")
				bot.answer_callback_query(callback_query_id=call.id,text="Help Me")
				
			if call.data == "create":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Ƈяєαтє Ƙєувσαяɗ IηƖιηє*\n`[/]create [Text] [Text] [Url]`", reply_markup=backs, parse_mode="Markdown")
				bot.answer_callback_query(callback_query_id=call.id,text="Help Create Keyboard")
				
			if call.data == "kickme":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Ƙιcк Uѕєя Ɓу SєƖf*\n`[/]kickme`", reply_markup=backs, parse_mode="Markdown")
				bot.answer_callback_query(callback_query_id=call.id,text="Help KickMe")
				
			if call.data == "echo":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Ɛcнσ Ƴσυя Ƭєxт*\n`[/]echo [Text]`", reply_markup=backs, parse_mode="Markdown")
				bot.answer_callback_query(callback_query_id=call.id,text="Help Echo")
				
			if call.data == "backs":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ƈσммαηɗѕ Lιѕт >", reply_markup=commandlist, parse_mode="Markdown")
				bot.answer_callback_query(callback_query_id=call.id,text="Back To Commands List")
				
			if call.data == "back":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ɓαcк Ƭσ Ɓσт Mєηυ", reply_markup=commadns, parse_mode="Markdown")
				bot.answer_callback_query(callback_query_id=call.id,text="Back To Menu")
				
			if call.data == "botmembers":
				members = database.scard('startbot')
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Ɓσт Mємвєяѕ >* `[{}]`".format(members), reply_markup=back, parse_mode="Markdown")
				bot.answer_callback_query(callback_query_id=call.id,text="Bot Members")
				
				
######################################################################################

@bot.message_handler(commands=['add'])
def adde(msg):
	if msg.from_user.id in sudos:
		if database.sismember("groups", msg.chat.id):
			bot.reply_to(msg, "👥Group > [ {} ] \n🎗Already Added To Gp List".format(msg.chat.id))
		else:
			database.sadd("groups", msg.chat.id)
			bot.reply_to(msg, "👥Group > [ {} ] \n🎗Added To Gp List".format(msg.chat.id))

######################################################################################

@bot.message_handler(content_types=['text', 'caption', 'username', 'tag', 'persian', 'english', 'filters', 'forward', 'link', 'sticker', 'locations', 'contact', 'document', 'audio', 'video', 'photo'])
def delete(msg):
	print msg
	
	id = msg.chat.id
	flood_max = 5 #You Can Change This Number
	flood_time = 1 #You Can Change This Number
	post_count = database.get("FloodCount"+str(id)+":"+str(msg.from_user.id))
	database.setex("FloodCount{}:{}".format(id,msg.from_user.id),flood_time,int(flood_max) + 1)
	
	if not msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id) or database.sismember("promote"+str(msg.chat.id), msg.from_user.id):
		if database.get("spam"+str(msg.chat.id)):
			if post_count > flood_max:
				bot.delete_message(msg.chat.id, msg.message_id)
				bot.kick_chat_member(msg.chat.id, msg.from_user.id)
				text = msg.text
				if len(text) >= 300:
					bot.delete_message(msg.chat.id, msg.message_id)
	
	if not msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id) or database.sismember("promote"+str(msg.chat.id), msg.from_user.id):
		if msg.sticker and database.get("sticker"+str(msg.chat.id)):
			delmessage(token, msg.chat.id, msg.message_id)
	
	if not msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id) or database.sismember("promote"+str(msg.chat.id), msg.from_user.id):
		if msg.location and database.get("location"+str(msg.chat.id)):
			delmessage(token, msg.chat.id, msg.message_id)
	
	if not msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id) or database.sismember("promote"+str(msg.chat.id), msg.from_user.id):
		if msg.text and database.get("text"+str(msg.chat.id)):
			delmessage(token, msg.chat.id, msg.message_id)

	if not msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id) or database.sismember("promote"+str(msg.chat.id), msg.from_user.id):
		if msg.contact and database.get("contact"+str(msg.chat.id)):
			delmessage(token, msg.chat.id, msg.message_id)
		
	if not msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id) or database.sismember("promote"+str(msg.chat.id), msg.from_user.id):
		if msg.document and database.get("document"+str(msg.chat.id)):
			delmessage(token, msg.chat.id, msg.message_id)
		
	if not msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id) or database.sismember("promote"+str(msg.chat.id), msg.from_user.id):
		if msg.audio and database.get("music"+str(msg.chat.id)):
			delmessage(token, msg.chat.id, msg.message_id)

	if not msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id) or database.sismember("promote"+str(msg.chat.id), msg.from_user.id):
		if msg.video and database.get("video"+str(msg.chat.id)):
			delmessage(token, msg.chat.id, msg.message_id)

	if not msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id) or database.sismember("promote"+str(msg.chat.id), msg.from_user.id):
		if msg.photo and database.get("photo"+str(msg.chat.id)):
			delmessage(token, msg.chat.id, msg.message_id)
		
	if not msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id) or database.sismember("promote"+str(msg.chat.id), msg.from_user.id):
		if msg.location and database.get("locations"+str(msg.chat.id)):
			delmessage(token, msg.chat.id, msg.message_id)
		
	if not msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id) or database.sismember("promote"+str(msg.chat.id), msg.from_user.id):
		if msg.caption and database.get("caption"+str(msg.chat.id)):
			delmessage(token, msg.chat.id, msg.message_id)
		
	if not msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id) or database.sismember("promote"+str(msg.chat.id), msg.from_user.id):
		if msg.forward_from and database.get("forward"+str(msg.chat.id)):
			delmessage(token, msg.chat.id, msg.message_id)
		
	if not msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id) or database.sismember("promote"+str(msg.chat.id), msg.from_user.id):
		if database.get("link"+str(msg.chat.id)):
			if re.match("https://telegram.me/(.*)", msg.text) or re.match("https://t.me/(.*)", msg.text) or re.match("telegram.me/(.*)", msg.text) or re.match("t.me/(.*)", msg.text):
				delmessage(token, msg.chat.id, msg.message_id)
			
	if not msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id) or database.sismember("promote"+str(msg.chat.id), msg.from_user.id):
		if database.get("persian"+str(msg.chat.id)):
			cps = (msg.photo or msg.caption or msg.text)
			if re.match("(ض|ص|ث|ق|ف|غ|ع|ه|خ|ح|ج|چ|پ|ش|س|ی|ب|ل|ا|ت|ن|مپک|گ|ظ|ط|ز|ژ|ر|ذ|د|ئ|ئ|و|)", msg.text):
				delmessage(token, msg.chat.id, msg.message_id)
			
	if not msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id) or database.sismember("promote"+str(msg.chat.id), msg.from_user.id):
		if database.get("english"+str(msg.chat.id)):
			cps = (msg.photo or msg.caption or msg.text)
			if re.match("(q|w|e|r|t|y|u|i|o|p|a|s|d|f|g|h|j|k|l|z|x|c|v|b|n|m|Q|W|E|R|T|Y|U|I|O|P|A|S|D|F|G|H|J|K|L|Z|X|C|V|B|N|M)", msg.text):
				delmessage(token, msg.chat.id, msg.message_id)
			
	if not msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id) or database.sismember("promote"+str(msg.chat.id), msg.from_user.id):
		if database.get("tag"+str(msg.chat.id)):
			if re.match("#(.*)", msg.text) or re.match("(.*)#", msg.text):
				delmessage(token, msg.chat.id, msg.message_id)
			
	if not msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id) or database.sismember("promote"+str(msg.chat.id), msg.from_user.id):
		if database.get("username"+str(msg.chat.id)):
			if re.match("@(.*)", msg.text) or re.match("(.*)@", msg.text):
				delmessage(token, msg.chat.id, msg.message_id)
			
	if not msg.from_user.id in sudos or database.sismember("owners"+str(msg.chat.id), msg.from_user.id) or database.sismember("promote"+str(msg.chat.id), msg.from_user.id):
		if msg.text in database.smembers("filters"):
			delmessage(token, msg.chat.id, msg.message_id)
		
		
######################################################################################
		
#@bot.message_handler(content_types=["text"])
#def msgs(msg):
 # msgs = msg.message_id
#  database.sadd('msg', msgs)

######################################################################################
# BoT Writed By Mr.Nitro(@HajiNitro) & @PlusTM
# Thanks To : 1 : @AlphaCyber 2 : @MosyDev 

#  Version > (FINAL)  #
bot.polling(True)
