from wxpy import *
from wechat_sender import *
from selectCount import *
from getInfo import *
bot = Bot('bot.pkl',console_qr=1)
# bot = Bot(console_qr=1)
my = bot.friends().search('~')[0]
print my

@bot.register(my,except_self=False)
def replyResult(msg):
	# temp = msg.text.decode('gbk')
	# print temp
	if msg.text == '1':
		return statistics()
	elif msg.text == '2':
            return getPipeLineInfo()
        elif msg.text == '3':
            return getPageProcessorInfo()
        else:
            return 'reply 1: getCount(*)\nreply 2: getPipeLineInfo()\nreply 3: getPageProcessorInfo()'
listen(bot)
