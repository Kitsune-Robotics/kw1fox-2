import subprocess

from datetime import date

proj_name = "KW1FOX-2"

today = date.today()

revision = (
    subprocess.check_output(
        [
            "git",
            "describe",
            "--abbrev=8",
            "--dirty",
            "--always",
            "--tags",
        ]
    )
    .strip()
    .decode("utf-8")
)

host = (
    subprocess.check_output(
        [
            "hostname",
        ]
    )
    .strip()
    .decode("utf-8")
)

username = (
    subprocess.check_output(
        [
            "id",
            "-u",
            "-n",
        ]
    )
    .strip()
    .decode("utf-8")
)

# Cleanup CI
if username == "root":
    username = "github"
    host = "github"

print(f"-DREVISION='\"{revision}\"'")  # Just the revision as a var

# Colors!
revision = revision.replace("dirty", "\x1B[31mdirty\x1B[0m")
host = "\x1B[34m" + host + "\x1B[0m"
username = "\x1B[34m" + username + "\x1B[0m"


motd = f"\\r\\nStarting {proj_name}.\\r\\nThis software expects your terminal to be \x1B[46mVT100 Compatable\x1B[0m,\\r\\n\\r\\nUsing version {revision}.\\r\\ncompiled on {today.strftime('%B %d, %Y')} by {username} using {host}.\\r\\n\\r\\n"

print(f"-DMOTD='\"{motd}\"'")  # Needed for the MOTD section
