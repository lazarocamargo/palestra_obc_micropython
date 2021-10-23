# software de voo - Missao RaioSat

from machine import Pin
from utime import sleep

antenas = Pin(16, Pin.OUT)

while True:
  antenas.on()
  sleep(0.5)
  antenas.off()
  sleep(0.5)
