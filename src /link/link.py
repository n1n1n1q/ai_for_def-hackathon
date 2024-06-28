"""
MavSDK
"""
import asyncio
from mavsdk import System

async def get_altitude(drone):
    """
    Get abs altitude
    """
    async for terrain_info in drone.telemetry.home():
        absolute_altitude = terrain_info.absolute_altitude_m
        break
    return absolute_altitude

async def set_up(address = "udp://:14540"):
    """
    Set the connection up
    """
    drone = System()
    print("Waiting for drone to connect...")
    await drone.connect(system_address=address)
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(" -- Drone connected")
            break

    print("Waiting for drone to have a global position estimate...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            print("-- Global position state is good enough for flying.")
            break
    return drone

async def takeoff(drone, sleep_time = 10):
    """
    Arm the drone
    """
    print(" -- Arming the drone...")
    await drone.action.arm()
    print(" -- Drone armed!")
    print(" -- Taking off...")
    await drone.action.takeoff()
    await asyncio.sleep(sleep_time)

async def rotate_camera(drone, pitch, yaw):
    """
    Rotate camera
    """
    await drone.gimbal.set_pitch_and_yaw(pitch, yaw)
    print(f" -- Rotated camera to pitch: {pitch}, yaw: {yaw}")

async def fly_forward(drone, distance, speed = 5):
    """
    Fly forward
    """
    print(f" -- Flying forward for {distance} meters at {speed} m/s")
    async for position in drone.telemetry.position():
        current_lat = position.latitude_deg
        current_lon = position.longitude_deg
        break

    new_lat = current_lat
    new_lon = current_lon + (distance / 111139)

    await drone.action.goto_location(new_lat, new_lon, get_altitude(drone), 0)
    await asyncio.sleep(distance / speed)
