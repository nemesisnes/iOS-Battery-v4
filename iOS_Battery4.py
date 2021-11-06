from objc_util import *
import sound
import time
import console

#on_main_thread(console.set_idle_timer_disabled)(True)

broken = 0
dict = {0:'idk', 1:'unplugged', 2:'charging', 3:'charged'}

try:
    device = ObjClass('UIDevice').currentDevice()
    device.setBatteryMonitoringEnabled_(True)
    battery_level = device.batteryLevel()
    battery_state = device.batteryState()
except Exception as error:
    broken += 1
    print(error)
    pass

while broken == 0:
    if (battery_level < 0.95) and (battery_state == (0 or 1)):
        x = sound.play_effect('arcade:Powerup_3', 1, pitch=1, pan=0, looping=False)
    else:
        y = sound.play_effect('arcade:Coin_1', 0, pitch=1, pan=0, looping=False)
    battery_level = device.batteryLevel()
    battery_state = device.batteryState()
    state = dict[battery_state]
    print(state, ' @ ', battery_level)
    time.sleep(10)

