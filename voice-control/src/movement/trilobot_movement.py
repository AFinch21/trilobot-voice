# from trilobot import *

def move_forward(duration: int = 1):
    """Move the trilobot forward for a given duration."""
    print(f"Moving the trilobot forward for {duration} seconds.")
    return {"message": f"Moving the trilobot forward for {duration} seconds."}

def move_backward(duration: int = 1):
    """Move the trilobot backward for a given duration."""
    print(f"Moving the trilobot backward for {duration} seconds.")
    return {"message": f"Moving the trilobot backward for {duration} seconds."}

def turn_right(duration: int = 1):
    """Turn the trilobot right for a given duration."""
    print(f"Turning the trilobot right for {duration} seconds.")
    return {"message": f"Turning the trilobot right for {duration} seconds."}

def turn_left(duration: int = 1):
    """Turn the trilobot left for a given duration."""
    print(f"Turning the trilobot left for {duration} seconds.")
    return {"message": f"Turning the trilobot left for {duration} seconds."}