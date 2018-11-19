import RPi.GPIO as GPIO
import time
import math
r = 3
R = 5.5

GPIO.setmode(GPIO.BOARD)
control_pins = [7,11,13,15,29,31,33,37]
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
halfstep_forward = [
  [1,0,0,0,1,0,0,0],
  [1,1,0,0,1,1,0,0],
  [0,1,0,0,0,1,0,0],
  [0,1,1,0,0,1,1,0],
  [0,0,1,0,0,0,1,0],
  [0,0,1,1,0,0,1,1],
  [0,0,0,1,0,0,0,1],
  [1,0,0,1,1,0,0,1]
]
halfstep_backward = [
  [0,0,0,1,0,0,0,1],
  [0,0,1,1,0,0,1,1],
  [0,0,1,0,0,0,1,0],
  [0,1,1,0,0,1,1,0],
  [0,1,0,0,0,1,0,0],
  [1,1,0,0,1,1,0,0],
  [1,0,0,0,1,0,0,0],
  [1,0,0,1,1,0,0,1]
]
halfstep_right = [
  [1,0,0,0,0,0,0,1],
  [1,1,0,0,0,0,1,1],
  [0,1,0,0,0,0,1,0],
  [0,1,1,0,0,1,1,0],
  [0,0,1,0,0,1,0,0],
  [0,0,1,1,1,1,0,0],
  [0,0,0,1,1,0,0,0],
  [1,0,0,1,1,0,0,1]
]
halfstep_left = [
  [0,0,0,1,1,0,0,0],
  [0,0,1,1,1,1,0,0],
  [0,0,1,0,0,1,0,0],
  [0,1,1,0,0,1,1,0],
  [0,1,0,0,0,0,1,0],
  [1,1,0,0,0,0,1,1],
  [1,0,0,0,0,0,0,1],
  [1,0,0,1,0,0,0,1]
]

def forward(d,r):
 s = int (d * 512 / (2*math.pi*r))
 steps = s / 512
 print (steps)
 for i in range(s):
  for halfstep in range(8):
    for pin in range(8):
      GPIO.output(control_pins[pin], halfstep_right[halfstep][pin])
    time.sleep(0.001)

def backward(d):
 for i in range(d):
  for halfstep in range(8):
    for pin in range(8):
      GPIO.output(control_pins[pin], halfstep_left[halfstep][pin])
    time.sleep(0.001)
    
def right(dg,r,R):
## steps = int(((dg * r / R)/360) * 512)
 porportion = (dg / 360) * R
 porportion = porportion / r
 steps = int(porportion * 512)
 print (steps)
 for i in range(steps):
  for halfstep in range(8):
    for pin in range(8):
      GPIO.output(control_pins[pin], halfstep_backward[halfstep][pin])
    time.sleep(0.001)

def left(dg,r,R):
 porportion = (dg / 360) * R
 porportion = porportion / r
 steps = int(porportion * 512)
 print (steps)
 for i in range(steps):
  for halfstep in range(8):
    for pin in range(8):
      GPIO.output(control_pins[pin], halfstep_forward[halfstep][pin])
    time.sleep(0.001)
    

##forward (30,3)
##backward (5 * 2 * math.pi * 2,2 )
right (90,3,5.5)
##left (360,r,R)
##left (512)
    
GPIO.cleanup()