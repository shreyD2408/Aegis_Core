import sys
import uselect
import time
from machine import Pin, PWM

PIN_PAN_SERVO = 2
PIN_TILT_SERVO = 3
PIN_RELOAD_SERVO = 4
PIN_FLYWHEEL = 6
PIN_BUZZER = 7

pan_pwm = PWM(Pin(PIN_PAN_SERVO))
pan_pwm.freq(50)

tilt_pwm = PWM(Pin(PIN_TILT_SERVO))
tilt_pwm.freq(50)

reload_pwm = PWM(Pin(PIN_RELOAD_SERVO))
reload_pwm.freq(50)

def set_servo_angle(pwm_obj, angle):
  angle = max(0, min(180, angle))
  duty_ns = int(500000 + (angle / 180.0) * 2000000)
  pwm_obj.duty_ns(duty_ns)

flywheel_pin = Pin(PIN_FLYWHEEL, Pin.OUT)
flywheel_pin.value(0)

buzzer_pwm = PWM(Pin(PIN_BUZZER))
buzzer_pwm.duty_u16(0)

def play_tone(frequency, duration_ms):
  if frequency > 0:
    buzzer_pwm.freq(frequency)
    buzzer_pwm.duty_u16(32768)
    time.sleep_ms(duration_ms)
  buzzer_pwm.duty_u16(0)

def play_startup_tone():
  play_tone(1200, 100)
  time.sleep(0.02)
  play_tone(1800, 150)
  time.sleep(0.02)
  play_tone(2400, 200)

current_pan = 90
current_tilt = 90
set_servo_angle(pan_pwm, current_pan)
set_servo_angle(tilt_pwm, current_tilt)
set_servo_angle(reload_pwm, 0)

spoll = uselect.poll()
spoll.register(sys.stdin, uselect.POLLIN)

play_startup_tone()
print("SENTRY-2350 MicroPython Initialized and Ready.")

while True:
  if spoll.poll(10):
    raw_line = sys.stdin.readline().strip()
    if raw_line:
      cmd_type = raw_line[0].upper()
      try:
        val = int(raw_line[1:])
      except ValueError:
        val = 0

      if cmd_type == 'P':
        current_pan = max(0, min(180, val))
        set_servo_angle(pan_pwm, current_pan)

      elif cmd_type == 'T':
        current_tilt = max(0, min(180, val))
        set_servo_angle(tilt_pwm, current_tilt)

      elif cmd_type == 'F':
        if val == 1:
          flywheel_pin.value(1)
          play_tone(2000, 80)
        else:
          flywheel_pin.value(0)

      elif cmd_type == 'R':
        play_tone(1000, 100)
        set_servo_angle(reload_pwm, 90)
        time.sleep_ms(350)
        set_servo_angle(reload_pwm, 0)
