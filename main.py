import asyncio
from dash.robot import DashRobot, discover_and_connect

async def main():
    robot = await discover_and_connect()
    if robot:
        print(f"Connected to {robot.address}")
        # Example command to move Dash
        await robot.move(100, 100)  # Move forward 100mm at 100mm/s
        await robot.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
