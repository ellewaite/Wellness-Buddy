import playsound 

button_sounds = {
	gpiozero.Button(2): "podcast1.mp3",
	gpiozero.Button(3): "podcast2.mp3",
	gpiozero.Button(4): "podcast3.mp3",
}

while True:
    for button, sound in button_sounds.items():
        button.when_pressed = playsound.playsound(sound)
    sleep(1)