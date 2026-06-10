# DevUtils 🛠️

A collection of handy developer utilities written in Python.

## Tools

- **txtimer** — Time how long a command takes to run
- **fstats** — Show file/directory statistics
- **passgen** — Generate secure random passwords
- **qrgen** — Terminal QR-code-ish art from any text
- **mood** — Daily developer mood forecast (deterministic, very scientific)

## Installation

```bash
pip install -e .
```

## Usage

```bash
# Time a command
python -m devutils txtimer -- pip install requests

# File stats
python -m devutils fstats ./src

# Generate a password
python -m devutils passgen --length 24
```

## License

MIT
