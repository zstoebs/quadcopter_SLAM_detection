# SLAM and Object Detection

Demonstration of SLAM and object detection with a Parrot ANAFI. The code depends on [pyparrot](https://github.com/amymcgovern/pyparrot). Pyparrot is a Python API for Parrot quadcopters and I'm extremely thankful for the owner's work, after running into every issue that one could possibly have with the Parrot GroundSDK. 

## Usage
1. Initialize your Parrot and update firmware by downloading the app and connecting the phone to the controller --> firmware updates should begin automatically. 
2. Consult the [pyparrot documentation](https://pyparrot.readthedocs.io/) to install the dependences and clone the GitHub repo --> PyPi's version for pyparrot is behind and doesn't include ANAFI. 
3. From the pyparrot repo, copy the pyparrot directory into your project and make an `images` directory. 
4. Replace the original wifiConnection.py with the updated version --> I made small changes to the argument passed to the IPv4Address function on line 318, which is compatible with zeroconf's current API. 
5. Switch the Parrot on and connect your ground machine (e.g. laptop) to the *Parrot's* wifi. 
6. Run anafi_prelim.py to check that the Parrot will respond. 

## To-Do
- Add a requirements.txt
- Actually program SLAM and object detection

## References
References from my first exposure to quad programming:
- [TelloTV](https://github.com/Jabrils/TelloTV)
- [TelloPython](https://github.com/dji-sdk/Tello-Python)

More to come soon!
