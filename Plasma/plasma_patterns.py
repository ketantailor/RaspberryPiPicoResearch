#!/usr/bin/env python3


# Plasma Patterns
# by Ketan Tailor, November 2022.


import time
from random import random, uniform, choice
import plasma
from plasma import plasma_stick


HSV_RED = 0 / 360
HSV_ORANGE = 30 / 360
HSV_YELLOW = 60 / 360
HSV_H90 = 90 / 360
HSV_GREEN = 120 / 360
HSV_H150 = 150 / 360
HSV_CYAN = 180 / 360
HSV_AZURE = 210 / 360
HSV_BLUE = 240 / 360
HSV_VIOLET = 270 / 360
HSV_MAGENTA = 300 / 360
HSV_H330 = 330 / 360

NUM_LEDS = 50
FPS = 60

led_strip = plasma.WS2812(NUM_LEDS, 0, 0, plasma_stick.DAT,
                          color_order=plasma.COLOR_ORDER_RGB)


def clear_all():
    '''Clear all LEDs'''
    for i in range(NUM_LEDS):
        led_strip.set_rgb(i, 0, 0, 0)


def set_all_rgb(r, g, b):
    '''Set all LEDs to the specified RGB value'''
    for i in range(NUM_LEDS):
        led_strip.set_rgb(i, r, g, b)


def set_all_hsv(h, s, v):
    '''Set all LEDs to the specified HSV value'''
    for i in range(NUM_LEDS):
        led_strip.set_hsv(i, h, s, v)

        
def rainbow_range(duration=30):
    print(f"rainbow_range() {duration}")
    for i in range(NUM_LEDS):
        h = i / NUM_LEDS
        led_strip.set_hsv(i, h, 1.0, 1.0)
    time.sleep(duration)


def up_and_down(r, g, b, fat=1, duration=30):
    print(f"up_and_down() {r} {g} {b} {fat} {duration}")
    step_delay = 0.5 * duration / (NUM_LEDS-fat+1)
    for i in range(NUM_LEDS-fat+1):
        for j in range(0, fat):
            led_strip.set_rgb(i+j,r,g,b)
        time.sleep(step_delay)
        for j in range(0, fat):
            led_strip.set_rgb(i+j,0,0,0)
    for i in range(NUM_LEDS-fat+1, 0, -1):
        for j in range(0, fat):
            led_strip.set_rgb(i+j,r,g,b)
        time.sleep(step_delay)
        for j in range(0, fat):
            led_strip.set_rgb(i+j,0,0,0)
            

def sparkle(h, duration=30):
    print(f"sparkle() {h} {duration}")
    for s in range(duration * 5):
        for i in range(NUM_LEDS):
            led_strip.set_hsv(i, h, 1.0, random())
        time.sleep(0.2)


def sparkle_white(duration=30):
    print(f"sparkle_white() {duration}")
    for s in range(duration * 5):
        for i in range(NUM_LEDS):
            intensity = int(uniform(0, 255))
            led_strip.set_rgb(i, intensity, intensity, intensity)
        time.sleep(0.2)


def sparkle_rainbow(duration=30):
    print(f"sparkle_rainbow() {duration}")
    for s in range(duration * 5):
        for i in range(NUM_LEDS):
            h = i / NUM_LEDS
            v = random()
            led_strip.set_hsv(i, h, 1.0, v)
        time.sleep(0.2)


def main():
    '''Main'''
    
    patterns = [
        lambda : rainbow_range(15),
        lambda : up_and_down(0, 255, 255, 1, 15),
        lambda : up_and_down(0, 0, 255, 5, 15),
        lambda : sparkle(HSV_RED, 15),
        lambda : sparkle(HSV_BLUE, 15),
        lambda : sparkle_white(15),
        lambda : sparkle_rainbow(15),
    ]
    
    led_strip.start(FPS)
    
    clear_all()
    
    for a in range(2):
        choice(patterns)()
        clear_all()
    
    clear_all()

main()