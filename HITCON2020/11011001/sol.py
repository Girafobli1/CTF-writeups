from z3 import *

"""
The program seems to take in 20 integers and do various functions
to manipulate and check the bits in each number. There are 7 checks
that the program does
"""

#for part 5 and 6
#counts number of nonzero bits in the number
def sub(b):
    n = b.size()
    bits = [ Extract(i, i, b) for i in range(n) ]
    bvs  = [ Concat(BitVecVal(0, n - 1), b) for b in bits ]
    nb   = reduce(lambda a, b: a + b, bvs)
    return nb


s = Solver()

nums = [ BitVec('nums_%s' % i, 32) for i in range(20) ]

#check 1: nums[i]&0xfff00000==0
for i in range(20):
	s.add(nums[i]&0xfff00000==0)


arr=[]
arr2=[]
#check 2: num&arr[i]==arr2[i]
#arr and arr2 are 2 arrays in memory
arr.append(0x00081002)
arr2.append(0x00001000)
arr.append(0x00029065)
arr2.append(0x00029061)
arr.append(0x00000000)
arr2.append(0x00000000)
arr.append(0x00016c40)
arr2.append(0x00016c00)
arr.append(0x00020905)
arr2.append(0x00000805)
arr.append(0x00010220)
arr2.append(0x00000220)
arr.append(0x00098868)
arr2.append(0x00080860)
arr.append(0x00021102)
arr2.append(0x00021000)
arr.append(0x00000491)
arr2.append(0x00000481)
arr.append(0x00031140)
arr2.append(0x00001000)
arr.append(0x00000801)
arr2.append(0x00000000)
arr.append(0x00060405)
arr2.append(0x00000400)
arr.append(0x0000c860)
arr2.append(0x00000060)
arr.append(0x00000508)
arr2.append(0x00000400)
arr.append(0x00040900)
arr2.append(0x00000800)
arr.append(0x00012213)
arr2.append(0x00010003)
arr.append(0x000428c0)
arr2.append(0x00000840)
arr.append(0x0000840c)
arr2.append(0x0000000c)
arr.append(0x00043500)
arr2.append(0x00002000)
arr.append(0x0008105a)
arr2.append(0x00001000)



for i in range(20):
        s.add( arr[i] & nums[i] == arr2[i] )


#check 3:
#every num[i]&7!=7 and !=0
for i in range(20):
        temp = BitVec("temp",32)
        j=0x12
        temp = nums[i]
        while(j!=0):
                s.add(temp&7!=7)
                s.add(temp&7!=0)
                temp=temp>>1
                j-=1

#check 4:
#same algorithm as 6 but with the check from 3 instead of 5
for i in range(0,20):
        ans = 0
        for j in range(0,20):
                a = nums[j]
                a=a>>(i&0xff)
                a=a&1
                a=a<<(j&0xff)
                ans = ans | a
        k=0x12
        while(k!=0):
                s.add(ans&7!=7)
                s.add(ans&7!=0)
                ans=ans>>1
                k-=1

#check 5: c++ popcount = 10
for i in range(20):
	s.add(sub(nums[i])==10)

#check 6: This algorithm:
#mov     eax, dword [rbp+rdx*4] {var_128}
#mov     ecx, ebx
#shr     eax, cl
#mov     ecx, edx
#add     rdx, 0x1
#and     eax, 0x1
#shl     eax, cl
#or      esi, eax
#cmp     rdx, 0x14
#jne     0xe70
#for ebx and edx in [0,20]

#then the check from 5

for i in range(0,20):
	ans=0
	for j in range(0,20):
		a = nums[j]
		a=a>>(i&0xff)
		a=a&1
		a=a<<(j&0xff)
		ans = ans | a
	s.add(sub(ans)==10)


#check 7
#no 2 numbers the same
for i in range(0,20):
	for j in range(i):
		if i!=j:
			s.add(nums[i]!=nums[j])
print(s.check())
print(s.model())
#print the solution (z3 is weird so it doesn't print in order
