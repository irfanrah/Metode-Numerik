# dibuat oleh irfan rahadi 1706036255
 
def TurunanY(x, y): #Fungsi Turunan Y
    return ((x**2 - 4*y))  
 
xawal = 0 #boundary condition x awal soal
yinit = 1 #boundary condition y awal soal
x = 0.03  #nilai x yang ditanya
h = 0.01  #delta yang digunakan
 
 
angka = (int)((x - xawal)/h) #menghitung jumlah increment yg diperlukan  
for i in range(1, angka + 1):
    k1 = h * TurunanY(xawal, yinit) #rumus runge kutta
    k2 = h * TurunanY(xawal + 0.5 * h, yinit + 0.5 * k1)
    k3 = h * TurunanY(xawal + 0.5 * h, yinit + 0.5 * k2)
    k4 = h * TurunanY(xawal + h, yinit + k3)
   
    yinit = yinit + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4) #menjumlahkan nilai k1,k2,k3,k4 ke y' yang baru dan membaginya  
    xawal = xawal + h #menambahkan xawal besarkan delta h
print(yinit)
