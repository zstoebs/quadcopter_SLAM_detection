"""
Preliminary checks for Parrot ANAFI

Modified from Bebop demo in pyparrot docs:
https://pyparrot.readthedocs.io/en/latest/quickstartbebop.html
"""
from pyparrot.Anafi import Anafi

anafi = Anafi()

print("connect")
success = anafi.connect(num_retries=10)
print(success)

print("sleep")
anafi.smart_sleep(5)

#anafi.set_indoor(is_outdoor=0) # uncomment if indoors

print("asking for update")
anafi.ask_for_state_update() # no return but populates state data

print("takeoff")
anafi.safe_takeoff(10) # takeoff

print("sleep")
anafi.smart_sleep(5) # sit still

print("land")
anafi.safe_land(10) # land

print("DONE - disconnect")
anafi.disconnect()
