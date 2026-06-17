import base64
import sys

def encode(text):
    encoded = base64.b64encode(text.encode("utf-8")).decode("utf-8")
    print("\n" + "=" * 40)
    print("         BASE64 ENCODER")
    print("=" * 40)
    print(f"  Input   : {text}")
    print(f"  Encoded : {encoded}")
    print("=" * 40 + "\n")

def decode(text):
    try:
        decoded = base64.b64decode(text.encode("utf-8")).decode("utf-8")
        print("\n" + "=" * 40)
        print("         BASE64 DECODER")
        print("=" * 40)
        print(f"  Input   : {text}")
        print(f"  Decoded : {decoded}")
        print("=" * 40 + "\n")
    except Exception:
        print("Error: Invalid Base64 string.")

def show_usage():
    print("Usage:")
    print("  python b64.py encode <text>")
    print("  python b64.py decode <base64>")
    print()
    print("Example:")
    print('  python b64.py encode "hello world"')
    print("  python b64.py decode aGVsbG8gd29ybGQ=")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        show_usage()
        sys.exit(1)

    mode = sys.argv[1].lower()
    text = " ".join(sys.argv[2:])

    if mode == "encode":
        encode(text)
    elif mode == "decode":
        decode(text)
    else:
        print(f"Unknown mode: '{mode}'")
        show_usage()
