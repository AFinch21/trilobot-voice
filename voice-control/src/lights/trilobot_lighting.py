# from trilobot import *

def turn_on_lights():
    """Turn on the lights on the trilobot."""
    print("Turning on the lights on the trilobot.")
    return {"message": "Turning on the lights on the trilobot."}

def turn_off_lights():
    """Turn off the lights on the trilobot."""
    print("Turning off the lights on the trilobot.")
    return {"message": "Turning off the lights on the trilobot."}

def flash_lights():
    """Flash the lights on the trilobot."""
    print("Flashing the lights on the trilobot.")
    return {"message": "Flashing the lights on the trilobot."}

def flash_lights_in_color(color: str):
    """Change the color of the lights on the trilobot."""
    print(f"Changing the color of the lights on the trilobot to {color}.")
    return {"message": f"Changing the color of the lights on the trilobot to {color}."}