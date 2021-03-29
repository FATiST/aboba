import vk_api, time, datetime, schedule
from vk_api.longpoll import VkLongPoll, VkEventType

year = '2000' #год рождения (можно изменить)
	
def main():
	try:
		global api
		vk_session = vk_api.VkApi(token='токен') #можно узнать на vkhost.github.io
		api = vk_session.get_api()
	except Exception as er:
		print(er)	
	
def setbdate():
	try:
		d = datetime.datetime.now()
		api.account.saveProfileInfo(bdate=f'{d.day}.{d.month}.{year}')
	except Exception as er:
		print(er)
			
main()
schedule.every().day.at("00:01").do(setbdate) #время, когда дата рождения будет обновляться (можно изменить)

while True:
	schedule.run_pending()
	time.sleep(1)