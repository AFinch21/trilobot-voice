from dotenv import load_dotenv

from livekit import agents, rtc
from livekit.agents import AgentServer,AgentSession, Agent, room_io
from livekit.plugins import noise_cancellation, silero, openai
from livekit.plugins.turn_detector.multilingual import MultilingualModel
from src.agents.trilobot import Trilobot

load_dotenv(".env.local")


server = AgentServer()

@server.rtc_session()
async def my_agent(ctx: agents.JobContext):
    session = AgentSession(
        stt = openai.STT(model="gpt-4o-transcribe"),
        llm=openai.LLM(model="gpt-4o-mini"),
        tts = openai.TTS(
            model="gpt-4o-mini-tts",
            voice="ash",
            instructions="Speak in a friendly and conversational tone.",
        ),
        vad=silero.VAD.load(),
        # turn_detection=MultilingualModel(),
    )

    await session.start(
        room=ctx.room,
        agent=Trilobot(),
        room_options=room_io.RoomOptions(
            audio_input=room_io.AudioInputOptions(
                noise_cancellation=lambda params: noise_cancellation.BVCTelephony() if params.participant.kind == rtc.ParticipantKind.PARTICIPANT_KIND_SIP else noise_cancellation.BVC(),
            ),
        ),
    )

    await session.generate_reply(
        instructions="Greet the user and offer your assistance."
    )


if __name__ == "__main__":
    agents.cli.run_app(server)