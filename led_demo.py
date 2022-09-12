import machine
import time
led=machine.Pin("LED",machine.Pin.OUT)
led.on()
time.sleep(3)
led.off()
 