# fun-home-projects
A small platform for parent-configurable child entertainment and education.

## Features
1. A small box with a simple screen, UI buttons, an audio system, and a lighting system.
2. A software platform that allows parents to create custom quiz questions (eg. "What does 5+5 equal?") or games.
3. A text to speech module reads the input prompts aloud through the audio speaker for children too young to read.
4. A bluetooth module allows for music streaming to the device from a parent's cellphone.
5. Computer control of the lighting system enhances the user experience for the child.
6. Customization of the underlying PCB's silkscreen artwork is displayed through a transparent front panel.

## Top level requirements
RPi.GPIO, inky, gTTS, circuitpython, adafruit-circuitpython-neopixel

## Installation
This module was developed on Raspberry Pi Zero W V1.1, but should be compatible with all newer RPi models running the latest version of Raspbian OS.
1. Ensure the OS is updated, and also ensure that Python 3 is used by default. Following the instructions here takes care of this as well as circuitpython installation: https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi
2. Follow these instructions to install inky: https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat
3. Download / clone this repository
4. Navigate to the base of the repository
5. Install setuptools (__pip install setuptools__)
6. Install module (__pip install .__)

## Updating Module from Repository
1. Pull changes from remote repository
2. Activate virtual environment with previous install
3. Navigate to the module directory
4. Test the module for completeness (__python setup.py test__)
5. Update module (__pip install . --upgrade__)