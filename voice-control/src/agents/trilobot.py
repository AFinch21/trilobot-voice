from dotenv import load_dotenv

from livekit import agents, rtc
from livekit.agents import AgentServer,AgentSession, Agent, room_io
from livekit.agents import function_tool, Agent, RunContext

from typing import Any, Literal

prompt = """
# Role & Objective
- You are an AI mounted in a Rasberry Pi Trilobot robot.
- You are to act as the trilobot's brain and personality.

# Tools
- You have access to a number of function tools that will help you operate your trilobot body.
- You have the capability to move forward, backward, left, right.
- You have the capability to view images from a camera mounted on the trilobot - facing forward.

# Instructions / Rules
- You may interpret the images to determine the environment around you.
- You may act based on the information gathered from the images.
- You can receive commands via voice from users.
- You cannot respond via voice - there is no audio output.
- You must respond to the user's questions in any physical way you can - move, rotate, etc.
"""

class Trilobot(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=prompt,
        )

    @function_tool()
    async def move_robot_in_direction(self, context: RunContext, movement_action: Literal["forward", "backward", "left", "right"], movement_duration: int = 1) -> dict[str, Any]:
        """
        Move the robot in a given direction. Use this function to move the trilobot in a given direction for a given duration.

        The movement_action argument must be one of the following: forward, backward, left, right.
        The movement_duration argument must be an integer representing the duration of the movement in seconds.

        Args:
            movement_action: The action to move the robot in, can be one of the following: forward, backward, left, right.
            movement_duration: The duration of the movement in seconds.
        """

        print(f"Moving the robot in the {movement_action} direction for {movement_duration} seconds.")

        return {"message": f"Moving the robot in the {movement_action} direction for {movement_duration} seconds."}
    
    @function_tool()
    async def use_camaera_to_view_environment(self, context: RunContext) -> dict[str, Any]:
        """View the camera mounted on the trilobot.

        Args:
            None
        """

        print("Viewing the camera.")

        return {"message": "Viewing the camera. I can see humans in front of me."}

    @function_tool()
    async def respond_to_user_question(self, context: RunContext, response: Literal["yes", "no", "unsure"]) -> dict[str, Any]:
        """
        Respond to the user's question. Use this tool to respond physically to any questions that can be answered with a yes, no, or unsure.
        The response argument must be one of "yes", "no", "unsure".
        The response arguemnt will be parsed and translated into a physical action by the trilobot's body to indicate your response to the user's question.

        Args:
            response: The response to the user's question. Must be one of "yes", "no", "unsure"
        """

        print(f"Responding to the user with: {response}")

        return {"message": f"Responding to the user with: {response} - executing physical action."}