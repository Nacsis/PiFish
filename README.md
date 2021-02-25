# PiFish

Hi,

some time ago I bought the animatronic fish big mouth billy bass on a flea market. It could could dance and sing "take me to the river" and "don't worry be happy".

Later I stumbled across some interesting projects that hook up animatronics on voice assistants:
https://anotherpiblog.blogspot.com/2017/01/billy-bass-alexa-and-raspberry-pi.html
https://albertarmea.com/post/alexa-tree/
https://www.instructables.com/Animate-a-Billy-Bass-Mouth-With-Any-Audio-Source/

I wanted to try this myself and started this project. I installed AlexaPi on my Raspberry Pi and hooked it up to my fish.

You can see its current state in this video:
https://www.instagram.com/p/CLpg0YXqlmk


## Big mouth billy bass
There are plenty of animatronics which can be used for this. I choosed billy bass, as I had owned one already.
Billy bass has just enough space in it, to fit a raspberry pi with attached motor hat in it. 
It has 3 dc-motors (Head, Tail and Mouth), two of them (Head, Tail) are pulled back with a feather, as soon as the motor stops.
I removed the original circuit board, so that you end up with 3 times 2 wires coming out of the backside of the fish.
I soldered longer wires (jumper) onto the ends of the wires to be able to operate easier. Unluckily I screwed up and damaged the head motor while soldering a cable onto it. I had to replace it with another dc motor, which turned out to be less powerfull, than the original one, and therefore the head won't move as wide, as it should. Also I removed some of the interior plastic and the small leg on the backside, which allowed it to stand, but I needed that extra space to fit the pi better into it, and didn't need the leg anyway, as the fish will end up hanging on a wall.
The fish uses a small speaker which I kept.

## Raspberry Pi
Basically you could just use a regular Echodot and a small arduino or esp, but I prefered to use the raspberry pi as it is powerfull and could handle other tasks as well, so I am able to switch to another voice assistent like Mycroft. 
I use an "Raspberry Pi 4 (Modell B, 2GB RAM)

## Motor HAT
To controll the motors I use an "Adafruit DC & Stepper Motor HAT for Raspberry Pi - Mini Kit [ADA2348]"
This comes with a python libary that alows you to controll the motors easily.

## Amplifier
For the small speaker I choose the amplifier "5 V-12 V 200 Gain LM386 Audio Verstärker Modul für Arduino EK1236".
The sound level can be adjusted using a small screwdriver. The sound is kind of crapy, maybe but enough for a voice assistent. The raspberry pi alows conencting bluetooth speakers, so I might go for that in the future.

## Sound sensor
In order to transfer Alexas voice into mouth movements I used the sound sensor "ANGEEK KY-037 4pin Voice Sound Detection Sensor". I place it next to the speaker, so it picks up the sound of Alexas voice and if it reaches a threshold (screwdriver adjustable) it sends a zero otherwise one.

## Wiring
[Todo: add a picture]

Maybe there is a better way to do this, but I just connected the Alexa's output pins for Activity-Led and Record-Led with two other GPIOs I used as input.

GPIO#22 -> GPIO#23 LED1 (Head)
GPIO#24 -> GPIO#25 LED2 (Tail)

In my code I check GPIO#23 for acitvity and GPIO#25 for recording and then control the Head and Tail movement acordingly.

Further I connected the Button and the mouth sensor:
GPIO#5 -> Button
GPIO#6 -> Sound Sensor (Mouth)

The motors are hooked up to the motor hat:
Motor1: Head
Motor2: Tail
Motor3: Mouth

## AlexaPi
I did not manage to install the original sample from the amazon developer site but the AlexaPi project worked.
https://github.com/alexa-pi/AlexaPi

I'm currently thinking about switching to Mycroft, as it's opensource and more privacy friendly.




