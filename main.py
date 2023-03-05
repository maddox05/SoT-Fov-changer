from pymem import Pymem
from pymem.ptypes import RemotePointer
import time

try:
    pm = Pymem("SoTGame.exe")
except:
    print("SOT not opened")
    time.sleep(2)
    quit()

fov = 1123024896  # 4byte = 120


def getPointerAddress(base, offsets):
    remote_pointer = RemotePointer(pm.process_handle, base)
    for offset in offsets:  # goes through the offsets and adds them
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(pm.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset  # returns last one which should give destination of fov


def write():
    try:
        pm.write_int(getPointerAddress(pm.base_address + 0x076CD7F0, offsets=[0x240, 0x3B8, 0x54]),
                     fov)  # writes to the location with the selected fov
        print("SUCCESS! FOV has been changed")
        time.sleep(1)
    except:
        print("error writing fov - restart sot or the application")


if __name__ == '__main__':
    time.sleep(1.5)
    write()
