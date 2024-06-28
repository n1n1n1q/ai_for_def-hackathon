"""
Mavlink connection
"""

from pymavlink import mavutil

MODES = {
    "manual": [217, 1, 0],
    "stabilized": [209, 7, 0],
    "acro": [209, 5, 0],
    "rattitude": [193, 8, 0],
    "altitude": [193, 2, 0],
    "offboard": [209, 6, 0],
    "position": [209, 3, 0],
    "hold": [217, 4, 3],
    "missition": [157, 4, 4],
    "return": [157, 4, 5],
    "follow me": [157, 4, 8]
}

def set_mode(master, mode):
    """
    Set UAV's mode
    """
    if mode not in MODES:
        raise ValueError("Wrong input mode")
    curr = MODES[mode]
    master.mav.command_long_send(
    master.target_system, master.target_component,
    mavutil.mavlink.MAV_CMD_DO_SET_MODE, 0,
    curr[0], curr[1], curr[2], 0, 0, 0, 0)

def takeoff(master, altitude):
    """
    Take the UAV off
    """
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
        0,
        0, 0, 0, 0, 0, 0, altitude)

def send_ned_velocity(master, vx, vy, vz):
    """
    Change UAV's position
    """
    master.mav.set_position_target_local_ned_send(
        0,
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_FRAME_LOCAL_NED,
        0b0000111111000111,
        0, 0, 0,
        vx, vy, vz,
        0, 0, 0,
        0, 0)
