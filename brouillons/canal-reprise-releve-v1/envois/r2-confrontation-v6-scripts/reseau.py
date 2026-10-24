import socket
try:
    socket.create_connection(("export.arxiv.org", 443), timeout=3).close()
    print("reseau OUVERT")
except OSError as e:
    print("reseau coupe :", type(e).__name__)
