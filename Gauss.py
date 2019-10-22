

iMATRIX=[[1,2,3,10,12],[2,2,5,2,20],[1,8,9,10,12],[10,2,0,5,2]]   

def PrintMatrix(Matrix):
    for i in range(len(Matrix)):
        for j in range(len(Matrix[i])):
            print(Matrix[i][j],end="\t")
        print()
        
def MultiplyRow(Row,Scalar): #Multiply an 1D list with a scalar (in place)
    for i in range(len(Row)):
        Row[i]=Row[i]*Scalar

def AddRow(Matrix,RowNR1,RowNR2,multi=1): #add a multiplum af RowNR1 to a RowNR2, defualt multi is 1
    for i in range(len(Matrix[RowNR2])):
        Matrix[RowNR2][i]+=Matrix[RowNR1][i]*multi

def SwitchRow(Matrix,RowNR1,RowNR2): #switch two rows in a matrix
    bufrow=Matrix[RowNR1]
    Matrix[RowNR1]=Matrix[RowNR2]
    Matrix[RowNR2]=bufrow
    return 0
    
def ZeroRowsBelow(Matrix,RowNR,CollumnNR): #Zero the fields of this collumn in the 
    for i in range(len(Matrix)-RowNR-1):
        if not(Matrix[RowNR][CollumnNR]==0):
            AddRow(Matrix,RowNR,i+1+RowNR,-float(Matrix[i+1+RowNR][CollumnNR])/Matrix[RowNR][CollumnNR])
            #print(i)
        
        
def SolveMatrix(Matrix):     
    #Bring To Row-Echelon Form
    for i in range(len(iMATRIX)):
        ZeroRowsBelow(iMATRIX,i,i)
    #    print ("O",i)
    #Make Row-Echelon 1
    for i in range(len(iMATRIX)):
        if not(iMATRIX[i][i]==0):
            MultiplyRow(iMATRIX[i],1./iMATRIX[i][i])
    #BackMultiply-thingy
    for i in range(len(iMATRIX)):
        for j in range(i):
            if not(iMATRIX[i][i]==0):
                AddRow(iMATRIX,i,j,-float(iMATRIX[j][i])/iMATRIX[i][i])
                
def IsRRowEchelon(Matrix): #Check if the matrix i in reduced Row-echolon form
    for i in range(len(Matrix)):
        pos=[1,0]
        if not(Matrix[i][i] in pos):
            return 0
    return 1



def CheckForEqualRows(Matrix):
    newlist=[]
    for i in Matrix:
        if i not in newlist:
            newlist.append(i)
    return newlist
    


    
MatrixNew=[]
for j in range(len(iMATRIX)):
    RowNew=[]
    for i in range(len(iMATRIX[j])):
        RowNew.append(iMATRIX[j][i])
    MatrixNew.append(RowNew)
iMATRIX=MatrixNew
PrintMatrix(iMATRIX)
print()
while True:
    SolveMatrix(iMATRIX)
    iMATRIX=CheckForEqualRows(iMATRIX)
    if IsRRowEchelon(iMATRIX):
        break
PrintMatrix(iMATRIX)
