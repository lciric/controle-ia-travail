import sys, paramiko
K="/tmp/claude-0/-home-user-controle-ia-travail/445c1b8c-c9f5-52f6-966f-fc165ad0e0c8/scratchpad/cle-ligne1"
HOTE, PORT = "213.199.247.188", 21280
def client():
    c=paramiko.SSHClient(); c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(HOTE, PORT, username="root", pkey=paramiko.Ed25519Key.from_private_key_file(K), timeout=30, allow_agent=False, look_for_keys=False)
    return c
if __name__=="__main__":
    mode=sys.argv[1]; c=client()
    if mode=="put":
        s=c.open_sftp(); s.put(sys.argv[2], sys.argv[3]); s.close(); print("posé")
    elif mode=="get":
        s=c.open_sftp(); s.get(sys.argv[2], sys.argv[3]); s.close(); print("pris")
    else:
        i,o,e=c.exec_command(sys.argv[2], timeout=float(sys.argv[3]) if len(sys.argv)>3 else 600)
        out=o.read().decode(errors="replace"); err=e.read().decode(errors="replace"); code=o.channel.recv_exit_status()
        print(out[-6000:]); print(err[-3000:], file=sys.stderr); print("CODE", code)
