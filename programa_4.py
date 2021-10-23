# software de voo - ANTENAS, COMM, ADCS, PAYLOAD
# com simulador de falha (pino GP28)

from machine import Pin
from utime import sleep

# define pinos de I/O
antenas = Pin(16, Pin.OUT)
comm = Pin(18, Pin.OUT)
adcs = Pin(19, Pin.OUT)
payload = Pin(20, Pin.OUT)

teste_falha = Pin(28, Pin.IN)

# Estados
INATIVO = 0
DEPLOY = 1
MODO_SEGURANCA = 2
MODO_ESTABILIZACAO = 3
MODO_NOMINAL = 4

estado = INATIVO    # inicia no estado = INATIVO

# maquina de estados
while True:
  
  if estado == INATIVO:
    antenas.off()
    comm.off()
    adcs.off()
    payload.off()
    sleep(5)
    falha = teste_falha.value()
    if falha == 1:
      estado = INATIVO
    else:
      estado = DEPLOY


  if estado == DEPLOY:
    antenas.on()
    sleep(2)
    antenas.off()
    estado = MODO_SEGURANCA

  if estado == MODO_SEGURANCA:
    comm.on()
    sleep(2)
    estado = MODO_ESTABILIZACAO

  if estado == MODO_ESTABILIZACAO:
    adcs.on()
    sleep(2)
    estado = MODO_NOMINAL

  if estado == MODO_NOMINAL:
    payload.on()
    falha = teste_falha.value()
    if falha == 1:
      estado = INATIVO
    else:
      estado = MODO_NOMINAL
    