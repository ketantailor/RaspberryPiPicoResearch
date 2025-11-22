#!/usr/bin/env python3


# Plasma Patterns
# by Ketan Tailor, November 2022.


# Plasma - https://github.com/pimoroni/pimoroni-pico/blob/main/micropython/modules/plasma/README.md


import time
from random import choice, random, uniform

import plasma
import uasyncio
from plasma import plasma_stick

NUM_LEDS = 50
FPS = 60

led_strip = plasma.WS2812(
    NUM_LEDS, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_RGB
)


def clear_all():
    """Clear all LEDs"""
    print("clear_all()")
    for i in range(NUM_LEDS):
        led_strip.set_rgb(i, 0, 0, 0)


def set_all_rgb(r, g, b):
    """Set all LEDs to the specified RGB value"""
    print(f"set_all_rgb() {r} {g} {b} {duration}")
    for i in range(NUM_LEDS):
        led_strip.set_rgb(i, r, g, b)


def set_all_hsv(h, s, v):
    """Set all LEDs to the specified HSV value"""
    # print(f"set_all_hsv() {h} {s} {v} {duration}")
    for i in range(NUM_LEDS):
        led_strip.set_hsv(i, h, s, v)


# sets the strip to the rainbox pattern and holds
# for the duration specified.
def rainbow_range(duration=30):
    print(f"rainbow_range() {duration}")
    for i in range(NUM_LEDS):
        h = i / NUM_LEDS
        led_strip.set_hsv(i, h, 1.0, 1.0)
    time.sleep(duration)


# smoothly cycles thru all the colors of the rainbow
# for the duration specified.
def rainbow_fade(duration=30):
    print(f"rainbow_fade() {duration}")
    for s in range(duration * 10):
        h = s / (duration * 10)
        set_all_hsv(h, 1.0, 1.0)
        time.sleep(0.1)


def up_and_down(r, g, b, fat=1, duration=30):
    print(f"up_and_down() {r} {g} {b} {fat} {duration}")
    step_delay = 0.5 * duration / (NUM_LEDS - fat + 1)
    for i in range(NUM_LEDS - fat + 1):
        for j in range(0, fat):
            led_strip.set_rgb(i + j, r, g, b)
        time.sleep(step_delay)
        for j in range(0, fat):
            led_strip.set_rgb(i + j, 0, 0, 0)
    for i in range(NUM_LEDS - fat + 1, 0, -1):
        for j in range(0, fat):
            led_strip.set_rgb(i + j, r, g, b)
        time.sleep(step_delay)
        for j in range(0, fat):
            led_strip.set_rgb(i + j, 0, 0, 0)


def sparkle_white(duration=30, blinks_per_sec=5):
    print(f"sparkle_white() {duration} {blinks_per_sec}")
    for s in range(duration * blinks_per_sec):
        for i in range(NUM_LEDS):
            intensity = int(uniform(0, 255))
            led_strip.set_rgb(i, intensity, intensity, intensity)
        time.sleep(1 / blinks_per_sec)


async def sparkle_white_async(duration=30, blinks_per_sec=5):
    print(f"sparkle_white_async() {duration} {blinks_per_sec}")
    for s in range(duration * blinks_per_sec):
        for i in range(NUM_LEDS):
            intensity = int(uniform(0, 255))
            led_strip.set_rgb(i, intensity, intensity, intensity)
        await uasyncio.sleep_ms(1000 / blinks_per_sec)


def sparkle_red(duration=30, blinks_per_sec=5):
    print(f"sparkle_red() {duration} {blinks_per_sec}")
    for s in range(duration * blinks_per_sec):
        for i in range(NUM_LEDS):
            led_strip.set_rgb(i, int(uniform(0, 255)), 0, 0)
        time.sleep(1 / blinks_per_sec)


async def sparkle_red_async(duration=30, blinks_per_sec=5):
    print(f"sparkle_red_async() {duration} {blinks_per_sec}")
    for s in range(duration * blinks_per_sec):
        for i in range(NUM_LEDS):
            led_strip.set_rgb(i, int(uniform(0, 255)), 0, 0)
        await uasyncio.sleep_ms(1000 / blinks_per_sec)


def sparkle_green(duration=30, blinks_per_sec=5):
    print(f"sparkle_green() {duration} {blinks_per_sec}")
    for s in range(duration * blinks_per_sec):
        for i in range(NUM_LEDS):
            led_strip.set_rgb(i, 0, int(uniform(0, 255)), 0)
        time.sleep(1 / blinks_per_sec)


async def sparkle_green_async(duration=30, blinks_per_sec=5):
    print(f"sparkle_green_async() {duration} {blinks_per_sec}")
    for s in range(duration * blinks_per_sec):
        for i in range(NUM_LEDS):
            led_strip.set_rgb(i, 0, int(uniform(0, 255)), 0)
        await uasyncio.sleep_ms(1000 / blinks_per_sec)


def sparkle_blue(duration=30, blinks_per_sec=5):
    print(f"sparkle_blue() {duration} {blinks_per_sec}")
    for s in range(duration * blinks_per_sec):
        for i in range(NUM_LEDS):
            led_strip.set_rgb(i, 0, 0, int(uniform(0, 255)))
        time.sleep(1 / blinks_per_sec)


async def sparkle_blue_async(duration=30, blinks_per_sec=5):
    print(f"sparkle_blue_async() {duration} {blinks_per_sec}")
    for s in range(duration * blinks_per_sec):
        for i in range(NUM_LEDS):
            led_strip.set_rgb(i, 0, 0, int(uniform(0, 255)))
        await uasyncio.sleep_ms(1000 / blinks_per_sec)


def sparkle_rainbow(duration=30, blinks_per_sec=5):
    print(f"sparkle_rainbow() {duration} {blinks_per_sec}")
    for s in range(duration * blinks_per_sec):
        for i in range(NUM_LEDS):
            h = i / NUM_LEDS
            v = random()
            led_strip.set_hsv(i, h, 1.0, v)
        time.sleep(1 / blinks_per_sec)


async def sparkle_rainbow_async(duration=30, blinks_per_sec=5):
    print(f"sparkle_rainbow_async() {duration} {blinks_per_sec}")
    for s in range(duration * blinks_per_sec):
        for i in range(NUM_LEDS):
            h = i / NUM_LEDS
            v = random()
            led_strip.set_hsv(i, h, 1.0, v)
        await uasyncio.sleep_ms(1000 / blinks_per_sec)


def sparkle_xmas(duration=30, blinks_per_sec=5):
    print(f"sparkle_xmas() {duration} {blinks_per_sec}")
    for s in range(duration * blinks_per_sec):
        for i in range(NUM_LEDS):
            if i % 4 == 0:
                led_strip.set_rgb(i, int(uniform(0, 255)), 0, 0)
            else:
                led_strip.set_rgb(i, 0, int(uniform(0, 255)), 0)
        time.sleep(1 / blinks_per_sec)


def sparkle_warm_white(duration=30, blinks_per_sec=5):
    print(f"sparkle_warm_white() {duration} {blinks_per_sec}")
    # (253, 244, 220)
    for s in range(duration * blinks_per_sec):
        for i in range(NUM_LEDS):
            intensity = random()
            led_strip.set_rgb(
                i, int(intensity * 253), int(intensity * 244), int(intensity * 220)
            )
        time.sleep(1 / blinks_per_sec)


duration = 30
blinks_per_sec = 1
led_strip.start(FPS)
fns = [
    # lambda: set_all_rgb(0, 0, 128),
    # lambda: set_all_rgb(0, 128, 0),
    # lambda: set_all_rgb(0, 128, 128),
    # lambda: set_all_rgb(128, 0, 0),
    # lambda: set_all_rgb(128, 0, 128),
    # lambda: set_all_rgb(128, 128, 0),
    # lambda: set_all_rgb(128, 128, 128),
    lambda: rainbow_range(duration),
    lambda: rainbow_fade(duration),
    lambda: rainbow_range(duration),
    lambda: rainbow_fade(duration),
    lambda: rainbow_range(duration),
    lambda: rainbow_fade(duration),

    lambda: up_and_down(0, 0, 128, fat=15, duration=duration / 5),
    lambda: up_and_down(0, 128, 0, fat=15, duration=duration / 5),
    lambda: up_and_down(0, 128, 128, fat=15, duration=duration / 5),
    lambda: up_and_down(128, 0, 0, fat=15, duration=duration / 5),
    lambda: up_and_down(128, 0, 128, fat=15, duration=duration / 5),
    lambda: up_and_down(128, 128, 0, fat=15, duration=duration / 5),
    lambda: up_and_down(128, 128, 128, fat=15, duration=duration / 5),

    lambda: sparkle_white(duration / 3, blinks_per_sec),
    lambda: sparkle_red(duration / 3, blinks_per_sec),
    lambda: sparkle_green(duration / 3, blinks_per_sec),
    lambda: sparkle_blue(duration / 3, blinks_per_sec),
    lambda: sparkle_rainbow(duration, blinks_per_sec),
    lambda: sparkle_xmas(duration, blinks_per_sec),
    # lambda: sparkle_warm_white(duration / 3, blinks_per_sec),

    lambda: sparkle_white(duration / 3, blinks_per_sec),
    lambda: sparkle_red(duration / 3, blinks_per_sec),
    lambda: sparkle_green(duration / 3, blinks_per_sec),
    lambda: sparkle_blue(duration / 3, blinks_per_sec),
    lambda: sparkle_rainbow(duration, blinks_per_sec),
    lambda: sparkle_xmas(duration, blinks_per_sec),
    # lambda: sparkle_warm_white(duration / 3, blinks_per_sec)
]


def main():
    try:
        while True:
            choice(fns)()
            clear_all()
    finally:
        clear_all()


main()
