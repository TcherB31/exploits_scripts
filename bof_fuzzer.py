#!/usr/bin/env python3
import pwntools pwn
from pwn import *

target_host = "example.com" 
target_port = 80 

conn = pwntools.remote(target_host, target_port) 

payload_size = 100

while True:  
    payload = 'A' * payload_size  
    conn.send(payload)                                                            
   
   print("Sent %d bytes" % len(payload))                                       
