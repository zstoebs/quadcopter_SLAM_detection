"""
Demo with Parrot ANAFI

Modified from Bebop demo in pyparrot docs:
https://pyparrot.readthedocs.io/en/latest/quickstartbebop.html
"""

from pyparrot.Anafi import Anafi

anafi = anafi()

print("connecting")
success = anafi.connect(num_retries=10)
print(success)

print("sleeping")
anafi.smart_sleep(5)

anafi.ask_for_state_update()

anafi.safe_takeoff(10) # takeoff

anafi.smart_sleep(5) # sit still

anafi.safe_land(10) # land

print("DONE - disconnecting")
anafi.disconnect()
