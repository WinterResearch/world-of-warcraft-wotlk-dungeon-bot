# world-of-warcraft-wotlk-dungeon-bot

https://www.youtube.com/watch?v=qc3QvQZHkv4

please consider giving repo a star if you enjoy

a world of warcraft pixel bot aimed at botting dungeons.

this program was built specifically for paladin, though can be modified to work for other classes with relative ease.

yes the code is sloppy, but its a proof of concept for botting dungeons with a simple pixel based bot.

put script in same folder as the images. likely may need to retake these images as they are sensitive to specific monitors.
reference python file, find/replace all png pictures that are being used within script. (windows+shift+s to take screenshot, save over same picture).
reference the weakauras as those are a majority of the pictures that are being scanned for.

if you see within the python file, each png has an associated region where the image can be found on the screen. this is very monitor specific, you will need to
either remove this region parameter, or reference pyautogui docs to find how to source this region parameter for each image. I recommend going through the effort 
of doing so, as it will increase the speed of each function.

install weakauaras addon, one by one, import all of the weakauras strings from weakauras.txt file, each separated by spaces.

to pause the bot, spam the f7 key to free mouse, then cancel running script.

required settings:

/follow macro, modify this macro each dungeon, to dps that your character will be following

macro keybind = Alt5
  
keybinds / targeting:

interact with target: CTRL-6

assist target: F1

attack target: F2

interface / controls:

interact on left click
  
![image](https://user-images.githubusercontent.com/95959417/198861122-0e000cb5-4553-4466-98c8-bdd01f550a0d.png)
![image](https://user-images.githubusercontent.com/95959417/198861184-c18ddd87-f51f-48c3-9f7b-d2c3512f389a.png)

