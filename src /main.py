"""
Autonomous drone navigation using electrical supply line tracking.
"""
import asyncio
import cv2
from link import link
from model.model import model, cap, get_powerline_position
from utilities.constants import DESIRED_POSITION, SCALING_FACTOR


async def main():
    """
    Main mission loop
    """
    drone = await link.set_up()
    await link.takeoff(drone)
    ret, frame = cap.read()
    await while ret:
        x_curr, y_curr = get_powerline_position(frame)
        if x_curr is not None and y_curr is not None:
            delta_x = x_desired - x_curr
            delta_y = y_desired - y_curr

            k = SCALING_FACTOR

            theta_pan = k * delta_x
            theta_tilt = k * delta_y
            link.rotate_camera(drone, )
        link.fly_forward(drone, 5)
    await drone.action.land()
    await asyncio.sleep(10)
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    x_desired, y_desired = DESIRED_POSITION
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())