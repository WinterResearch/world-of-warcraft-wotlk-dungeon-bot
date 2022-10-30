from time import sleep, perf_counter
from threading import Thread
import pyautogui as p
import keyboard 


targetz = False
low_mana = False
low_health = False
mobs_killed = 0
combat_status = False
stop_bot = False
aura = None
def pause_bot():
	print('PRESS F7 TO PAUSE THE BOT')
	if keyboard.is_pressed('f7'):
		print('YOU PRESSED F7 -- PAUSING BOT')
		stop_bot = True
		while keyboard.is_pressed('f8') is False:
			print('PRESS F8 TO START BOT')
			sleep(5)
		stop_bot = False
		print('BOT BACK ON')



def enemy_low():
	global stop_bot
	if stop_bot is True:
		print('ENEMY_LOW THREAD TO SLEEP, global stop_bot TRUE')
		sleep(100)
	low_hp = p.locateCenterOnScreen('enemy_low.png',confidence=.8,region=(6,567,56,59), grayscale=True)
	if low_hp:
		print('ENEMY LOW, PRESSING HAMMER OF WRATH')
		hammer_wrath()
	else:
		print('FALSE ENEMY NOT LOW_HEALTH')

def health_check():
	global low_health
	global stop_bot
	if stop_bot is True:
		print('HEALTH_CHECK THREAD TO SLEEP, global stop_bot TRUE')
		sleep(100)
	low = p.locateOnScreen('low_health.png',confidence=.7, region=(2465,346,56,53), grayscale=True)
	if low:
		low_health = True
		print('LOW_HEALTH')
	else:
		low_health = False
		print('NOT LOW HP')
		

def hammer_wrath():
	wrath = p.locateCenterOnScreen('hammer_wrath.png',region=(1167,1377,50,48),grayscale=True)
	if wrath:
		p.press('f')
		print('HAMMER OF WRATH')
		#sleep(.5)

def in_combat():
	global combat_status
	global stop_bot
	global targetz
	if stop_bot is True:
		print('IN_COMBAT THREAD TO SLEEP, global stop_bot TRUE')
		sleep(100)
	in_combat = p.locateCenterOnScreen('in_combat.png',confidence=.7,region=(2339,1293,60,60),grayscale=True)
	if in_combat:
		combat_status = True
		print('IN_COMBAT TRUE')
		if dungeon_target() is True:
			attack()
		if dungeon_target() is False:
			p.hotkey('alt','5') #run to ally
			p.press('tab')
	else:
		combat_status = False
		clear_loot()

def mana_check():
	global low_mana
	global stop_bot
	if stop_bot is True:
		print('MANA_CHECK THREAD TO SLEEP, global stop_bot TRUE')
		sleep(100)
	mana_check = p.locateCenterOnScreen('low_mana.png',confidence=.9,region=(2392,303,48,52),grayscale=True)
	if mana_check:
		low_mana = True
		print('LOW MANA')
	else:
		low_mana = False

def attack():
	# paladin rotation, can be modified for another class
	seal_not_on()
	p.press('2')
	p.hotkey('shift','5')
	p.hotkey('shift','4')
	p.press('r')
	p.press('4')
	#p.press('g')
	p.press('t')
	p.hotkey('shift','g')
	
	#art_of_war()
	p.hotkey('ctrl','6') # run to target

def target():
	global targetz
	global stop_bot
	if stop_bot is True:
		print('TARGET THREAD TO SLEEP, global stop_bot TRUE (F8 KEY)')
		sleep(100)
	target_true = p.locateOnScreen('enemy_target.png',grayscale=True,confidence=.9,region=(2269,90,34,34))
	if target_true:
		print('TARGET TRUE')
		targetz = True
		return True
	else:
		print('NO TARGET')
		targetz = False
		return False


def seal_not_on():
	seal = p.locateCenterOnScreen('seal_on_paladin.png',confidence=.7,region=(2270,4,29,33),grayscale=True)
	if seal:
		pass
	else:
		print('USING SEAL')
		p.hotkey('shift','2')

def find_image_location():
	#pyautogui.press('capslock') #W/E NEED TO DO TO TRIGGER WA
	b = p.locateOnScreen('dungeon_target.png',confidence=.9)
	print(b)

def follow_ally():
	global combat_status

	if combat_status is False:
		print('COMBAT STATUS IS FALSE FOLLOWING')
		p.hotkey('alt','5') # / follow macro keybind
		sleep(5)


def turn(direction,direction2=None):
	if direction == 180:
		p.keyDown('left')
		sleep(.91)
		p.keyUp('left')
	if direction == 90 and direction2 == 'left':
		p.keyDown('left')
		sleep(.5)
		p.keyUp('left')
	if direction == 45 and direction2 == 'left':
		p.keyDown('left')
		sleep(.25)
		p.keyUp('left')
	if direction == 90 and direction2 == 'right':
		p.keyDown('right')
		sleep(.46)
		p.keyUp('right')
	if direction == 45 and direction2 == 'right':
		p.keyDown('right')
		sleep(.46)
		p.keyUp('right')
	if direction == 15 and direction2 == 'left':
		p.keyDown('left')
		sleep(.23)
		p.keyUp('left')
	if direction == 15 and direction2 == 'right':
		p.keyDown('right')
		sleep(.23)
		p.keyUp('right')
	if direction == 7 and direction2 == 'right':
		p.keyDown('right')
		sleep(.11)
		p.keyUp('right')
	if direction == 7 and direction2 == 'left':
		p.keyDown('left')
		sleep(.11)
		p.keyUp('left')


def art_of_war():
	global low_health
	global combat_status
	aow = p.locateCenterOnScreen('art_of_war.png',confidence=.7,region=(2490,32,100,100),grayscale=True)
	print(aow)
	print(aow)
	print(aow)
	print(aow)

	print('ART OF WAR BUFF')
	print(combat_status)
	print('COMBAT STATUS ABOVE')
	if aow != None:
		if low_health is True:
			p.hotkey('ctrl','4')
		else:
			if combat_status is True:
				print('HEALING AOW')
				p.press('t')


def check_alive():
	alive = p.locateCenterOnScreen('alive.png',confidence=.7,grayscale=True)
	if alive != None:
		print('ALIVE')
		return True
	else:
		return False


def press_key(key,hold_time):

		p.keyDown(key)
		sleep(hold_time)
		p.keyUp(key)





def scan_keybind():
	p.press('tab')

def scan_enemy():
	global stop_bot
	global targetz
	global low_health
	global low_mana
	global combat_status
	if stop_bot is True:
		print('SCAN_ENEMY THREAD TO SLEEP, global stop_bot TRUE')
		sleep(100)
	elif keyboard.is_pressed('f6'):
		print('PAUSING SCAN ENEMY FUNCTION FOR 30 SECONDS')
		sleep(30)
	elif combat_status is False:
		if got_xp() is True:
			loot_enemy()

		if low_mana is True:
			p.press('v')
			sleep(14)
			
		if low_health is True:
			p.press('3')
			sleep(2)

		if targetz == False:
			turn(7,'left')
			press_key('w',.5)
			scan_keybind()
		else:
			p.hotkey('ctrl','6') # Interact with target wow keybind
			p.press('f2') #Attack Target wow keybind

def got_xp():
	#global mobs_killed
	xp = p.locateCenterOnScreen('got_xp.png',confidence=.7)
	if xp:
		#mobs_killed += 1
		#print('BOT HAS KILLED ' + str(mobs_killed) + str( ' MOBS'))
		return True
	else:
		return False

def loot_enemy():
	global combat_status
	if combat_status is False:
		p.click(x=1342,y=763)
		sleep(.05)
		p.click(x=1318,y=731)
		sleep(.05)
		p.click(x=1263,y=686)
		sleep(.05)
		p.click(x=1220,y=701)
		sleep(.05)
		p.click(x=1200,y=736)
		sleep(.05)
		p.click(x=1184,y=790)
		sleep(.05)
		p.click(x=1230,y=770)


def clear_loot():
	#if got_xp():
		#print('GOT XP')
	loot_enemy()
	greed()
		#p.hotkey('ctrl','y')

def greed():
	greed1 = p.locateCenterOnScreen('greed1.png',confidence=.7)
	if greed1 != None:
		p.click(greed1)
	greed2 = p.locateCenterOnScreen('greed2.png',confidence=.7)
	if greed2 != None:
		p.click(greed2)


def flying():
	flying = p.locateCenterOnScreen('flying.png',grayscale=True)
	if flying != None:
		p.hotkey('alt','2')
		now_flying = True
		while now_flying is True:
			flying = p.locateCenterOnScreen('flying.png',grayscale=True)
			if flying is None:
				p.hotkey('alt','1')
				now_flying = False

def dungeon_target():
	dt = p.locateCenterOnScreen('dungeon_target.png',confidence = .7,region=(18,1187,75,75),grayscale=True)
	global targetz
	global stop_bot
	if stop_bot is True:
		print('TARGET THREAD TO SLEEP, global stop_bot TRUE (F8 KEY)')
		sleep(100)
	if dt != None:
		print('ACTIVE TARGET')
		targetz = True
		return True
	else:
		targetz = False
		return False
	

while True:



	start_time = perf_counter()


	t1 = Thread(target=enemy_low)
	t2 = Thread(target=health_check)
	t3 = Thread(target=dungeon_target)

	t5 = Thread(target=mana_check)
	t6 = Thread(target=in_combat)
	t7 = Thread(target=pause_bot)
	t8 = Thread(target=follow_ally)

	# start the threads
	t1.start()
	t2.start()
	t3.start()
	#t4.start()
	t5.start()
	t6.start()
	t7.start()
	t8.start()

	t1.join()
	t2.join()
	t3.join()

	t5.join()

	t7.join()


	end_time = perf_counter()

	print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')
	sleep(.5)