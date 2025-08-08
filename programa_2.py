# software de voo - Missao RaioSat exemplo

from machine import Pin
from utime import sleep

# define pinos de IO
antenas = Pin(16, Pin.OUT)
comm = Pin(18, Pin.OUT)

# Estados
INATIVO = 0
DEPLOY = 1
MODO_SEGURANCA = 2

estado = INATIVO

# maquina de estados
while True:
  
  if estado == INATIVO:
    antenas.off()
    sleep(5)
    estado = DEPLOY
    

  if estado == DEPLOY:
    antenas.on()
    sleep(2)
    antenas.off()
    estado = MODO_SEGURANCA

  if estado == MODO_SEGURANCA:
    comm.on()
    estado = MODO_SEGURANCA
    


