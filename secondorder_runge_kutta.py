# consol https://www.youtube.com/watch?v=Fs1cRieo8XM
# y'' - x^2 y' -2xy =1


#pemecah 2 order
def TurunanY1(x,y,z): #order 1 dimana z = dy/dx
  return (z)  

def TurunanY2(x,y,z):#order 2 dimana dz/dx
  return (1+2*x*y-((x**2)*z))

xawal = 0 #boundary condition x awal soal
yinit = 1 #boundary condition y awal soal
zinit = 0 # karna f' = 0
x = 0.03  #nilai x yang ditanya
h = 0.01  #delta yang digunakan
 
 
angka = (int)((x - xawal)/h) #menghitung jumlah increment yg diperlukan  
for i in range(1, angka + 1):
    k1 = h * TurunanY1(xawal, yinit,zinit) #rumus runge kutta
    l1 = h * TurunanY2(xawal, yinit,zinit)
    k2 = h * TurunanY1(xawal + 0.5 * h, yinit + 0.5 * k1,zinit + l1/2 )
    l2 = h * TurunanY2(xawal + 0.5 * h, yinit + 0.5 * k1,zinit + l1/2 )
    k3 = h * TurunanY1(xawal + 0.5 * h, yinit + 0.5 * k2,zinit + l2/2)
    l3 = h * TurunanY2(xawal + 0.5 * h, yinit + 0.5 * k2,zinit + l2/2)
    k4 = h * TurunanY1(xawal + h, yinit + k3, zinit +l3)
    l4 = h * TurunanY2(xawal + h, yinit + k3, zinit +l3)
   
    yinit = yinit + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4) #menjumlahkan nilai k1,k2,k3,k4 ke y' yang baru dan membaginya  
    xawal = xawal + h #menambahkan xawal besarkan delta h
print(yinit)
