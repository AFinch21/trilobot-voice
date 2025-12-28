## Trilobot Voice Control - LiveKit x OpenAI

This repo holds a simple implementation of LiveKit and a STT → LLM → TTS pipeline to put a "headless" voice model into a Raspberry Pi powered Trilobot.

The setup is "headless" (no speaker output), but it can still respond to user commands, answer questions, and react via Trilobot movements/lights.

For instance - upon asking the trilobot a question that could be answered by "yes", "no" or "unsure" - the trilobot will react appropriately!

### Prerequisites

- **Python**: 3.12+
- **uv**: install via Homebrew: `brew install uv` (or see `https://docs.astral.sh/uv/`)

### Setup (uv)

From the `voice-control/` directory:

```bash
uv sync
```

If you're installing on a Raspberry Pi / Linux and want the hardware stack:

```bash
uv sync --extra robot
```

### Configure environment

This project loads environment variables from **`.env.local`** (see `main.py`).

Create `voice-control/.env.local`:

```bash
cat > .env.local <<'EOF'
# OpenAI
OPENAI_API_KEY=your_openai_api_key

# LiveKit (required for `start` / `dev`)
LIVEKIT_URL=wss://your-livekit-server
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
EOF
```

### Run

- **Local console mode (fastest to verify wiring):**

```bash
uv run python main.py console
```

- **Agent worker (connects to LiveKit):**

```bash
uv run python main.py start
```

- **Dev mode (typically enables auto-reload / dev ergonomics):**

```bash
uv run python main.py dev
```

