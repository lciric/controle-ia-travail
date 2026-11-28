import sys
b = sys.stdin.buffer.read().split(b"\n")
b.insert(1, b"    | ligne coup\xc3")
sys.stdout.buffer.write(b"\n".join(b))
