"""
...
"""
from link import link
from pymavlink import mavutil

master = mavutil.mavlink_connection('udp:127.0.0.1:14550')
master.wait_heartbeat()

link.set_mode(master, 'manual')
master.arducopter_arm()
link.takeoff(master, 10)
print(master.mode_mapping())

while True:
    link.send_ned_velocity(master, 1, 0, 0)