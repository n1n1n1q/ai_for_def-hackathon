"""
Main
"""
from link import link
from pymavlink import mavutil
from model.model import model, cap, get_powerline_position
from utilities.constants import DESIRED_POSITION, SCALING_FACTOR
import cv2

master = mavutil.mavlink_connection('udp:127.0.0.1:14550')
master.wait_heartbeat()

link.set_mode(master, 'manual')
master.arducopter_arm()
link.takeoff(master, 10)
print(master.mode_mapping())

x_desired, y_desired = DESIRED_POSITION

while True:
    ret, frame = cap.read()
    if not ret:
        break
    x_curr, y_curr = get_powerline_position(frame)
    if x_curr is not None and y_curr is not None:
        delta_x = x_desired - x_curr
        delta_y = y_desired - y_curr

        k = SCALING_FACTOR

        theta_pan = k * delta_x
        theta_tilt = k * delta_y

        master.mav.command_long_send(
            master.target_system,
            master.target_component,
            mavutil.mavlink.MAV_CMD_DO_MOUNT_CONTROL,
            0,
            theta_tilt,
            theta_pan,
            0,
            0, 0, 0,
            mavutil.mavlink.MAV_MOUNT_MODE_MAVLINK_TARGETING
        )

    link.send_ned_velocity(master, 1, 0, 0)

cap.release()
cv2.destroyAllWindows()