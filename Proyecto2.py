# Código para Gauss-Seidel
def gauss_seidel( A, b,n, x, imax, es, lmda):
    for i in range (n):
      dummy = A[i][i]
      for j in range(n):
        A[i][j] =  A[i][j] /dummy
      b[i] = b[i]/dummy


    for i in range(n):
      sum = b[i]
      for j in range(n):
        if i !=j :
          sum = sum - A[i][j]*x[j]
      x[i] = sum

    iter = 0
    sentinel = 1
    while sentinel == 1 or (iter >= imax):
      for i in range(n):
        old = x[i]
        sum = b[i]
        for j in range (n):
          if i !=j :
            sum = sum - A[i][j]*x[j]
        x[i] = lmda*sum + (1-lmda)*old
        if sentinel == 1 and x[i]!= 0:
          ea = abs((x[i]- old)/x[i])*100
          if ea < es:
            sentinel = 0

      iter = iter + 1

    return x, iter


#PARTE B - GS
# Obtener la cantidad de acciones que cumplan con nuestras hipotesis de inversión y retorno

A = [[187.65, 328.79, 295.1],
     [1, 1, 1],
     [178.61, 322.98, 285.5]]

b = [11162.7, 50, 10721.25]
n = 3
x = [20, 5, 10]
lmda = 1  # Factor de relajación
es = 0.00001
imax = 1000

solution, iterations = gauss_seidel(A, b, n, x, imax, es, lmda)

if solution is not None:
    print("Solución:", solution)
    print("Número de iteraciones:", iterations)
else:
    print("El método no convergió en", imax, "iteraciones.")
