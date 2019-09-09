
def soal(x):
	pembilang = x**2-1
	penyebut = x -1
	try:
		hasil = pembilang/penyebut
	except ZeroDivisionError:
		hasil = float('inf')
	return hasil

limx = 1
limb = limx + 0.5
limp = 0.05
limx1 = limx - limp
hasilnya = 0
while limx < limb+ 0.5:
	#print(limx1)
	limx1 =limx1 + 0.01
	print(soal(limx1))
	limx = limx + 0.1
	if soal(limx1) != float('inf'):
		#print(soal(limx1))
		hasilnya = hasilnya + soal(limx1)

		
print("hasil limitnya = ")
print(hasilnya/9)
	
