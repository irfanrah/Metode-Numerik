x = [3,1,4,17]
y = [2,3,1,12]
z = [3,4,2,19]
MatTot = [x,y,z]

Mkos = []
MatrixSatu = []
MatrixI2 = []
MatrixE3 = []
MatrixE4 = []

def substractkalimatrix(m1,m2,param):
	if(len(Mkos) != 0):
		clearmat(Mkos)
	for i in range(0,4):
		sm = m1[i] - (m2[i]*m1[param]/m2[param])
		Mkos.append(sm)
	return Mkos
def identitymatrix(matrex,pos1):
	if(len(Mkos) != 0):
		clearmat(Mkos)
	for i in range(0,4):
			idMatrix = matrex[i]/matrex[pos1]
			Mkos.append(idMatrix)
	return Mkos

def clearmat(matkosong):
	while(len(matkosong) != 0):
		matkosong.remove(matkosong[0])
	return matkosong
	
def listomatrix(Min,Mout):
	Mout.append([])
	for x in range(0,4):
		Mout[i].append(Min[x])
			
def CallBack(m1,m2,m3): #ambil input gauss 
	if(len(Mkos) != 0):
		clearmat(Mkos)
	for i in range(0,4):
		sm = m1[i] - (m2[i]*m1[param]/m2[param])
		Mkos.append(sm)
	return Mkos


def AmbilMatrix(MaFul,p):
	return MaFul[p]



for i in range(0,3):
	#print(AmbilMatrix(MatTot,i))
	Matrix = AmbilMatrix(MatTot,i)
	MatrixI = identitymatrix(Matrix,i)
	#print(MatrixI)
	listomatrix(MatrixI,MatrixI2)
#print(MatrixI2)

for i in range(0,3):
	AntiLeb = i + 1
	if AntiLeb != 3 :
		MatEq = substractkalimatrix(MatrixI2[i+1],MatrixI2[i],0) #i+1 di jdiin ada 0
		listomatrix(MatEq,MatrixE3)

for i in range(0,2):
	AntiLeb = i + 1
	if AntiLeb != 2 :
		MatEq = substractkalimatrix(MatrixE3[i+1],MatrixE3[i],1)
		listomatrix(MatEq,MatrixE4)
		


#xxx = substractkalimatrix(MatrixI2[1],MatrixI2[0],0) # cobaaa tinggal forin
print(identitymatrix(MatrixI2[0],0))
print(identitymatrix(MatrixE3[0],1))
print(MatrixE4)
