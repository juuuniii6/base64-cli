# base64-cli

A simple command-line Base64 encoder and decoder written in Python.

## Features

- Encode any text to Base64
- Decode Base64 back to plain text
- No external dependencies

## Usage

```bash
# Encode
python b64.py encode "hello world"

# Decode
python b64.py decode aGVsbG8gd29ybGQ=

# Encode a URL
python b64.py encode "https://github.com"
```

## Example Output

```
# Encode
========================================
         BASE64 ENCODER
========================================
  Input   : hello world
  Encoded : aGVsbG8gd29ybGQ=
========================================

# Decode
========================================
         BASE64 DECODER
========================================
  Input   : aGVsbG8gd29ybGQ=
  Decoded : hello world
========================================
```

## Requirements

- Python 3.x
