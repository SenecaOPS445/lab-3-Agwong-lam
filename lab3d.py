#!/usr/bin/env python3
# Author ID: agwong-lam

import os

def free_space():
    command = "df -h | grep '/$' | awk '{print $4}'"
    output = os.popen(command).read().strip()

    return output
   

if __name__ == "__main__":
    print(free_space())

