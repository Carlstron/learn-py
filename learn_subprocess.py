import subprocess
import sys
print(sys.platform)

cmd = ['ping', '127.0.0.1']

proc = subprocess.run(
    cmd, capture_output=True, text=True, encoding='cp850'
)

# print(proc.args)
# print(proc.returncode)
# print(proc.stderr)
print(proc.stdout)
