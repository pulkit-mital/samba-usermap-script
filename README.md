# samba-usermap-script

**Name:** Samba "username map script" Command Execution <br/>
**Supported Architecture:** cmd<br/>
**Supported Platform:** Unix <br />
**Target Service / protocol:** microsoft-ds, netbios-ssn <br />
**Target Network Port(s):** 139, 445 <br />
**List of CVEs:** CVE-2007-2447 <br />
<br />
This script will exploit a command execution vulnerability in Samba versions 3.0.20 through 3.0.25rc when using the non-default "username map script" configuration option. By specifying a username containing shell meta characters, attackers can execute arbitrary commands. No authentication is needed to exploit this vulnerability since this option is used to map usernames prior to authentication!

<br/>

## Usage:
```shell
$ python samba_usermap_script.py <RHOST> <RPORT> <LHOST> <LPORT>
```
  * `RHOST` -- The target address
  * `RPORT` -- The target port (TCP : 445)
  * `LHOST` -- The listen address
  * `LPORT` -- The listen port

## Installation

    sudo apt install python python-pip
    pip install --user pysmb
    git clone https://github.com/pulkit-mital/samba-usermap-script.git

### Disclaimer:

All the code provided on this repository is for educational/research purposes only. Any actions and/or activities related to the material contained within this repository is solely your responsibility. The misuse of the code in this repository can result in criminal charges brought against the persons in question. Author will not be held responsible in the event any criminal charges be brought against any individuals misusing the code in this repository to break the law.
