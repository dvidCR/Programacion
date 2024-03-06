import calendar
 
horas_semana_asignatura = [ [0,2,3,3,0,0,0] , [0,2,3,3,0,0,0]]
 
'''
  Calcula el numero de dias de la semana por mes
'''
def num_dias_semanales_por_mes (calendario, year, month):
   
    num_dias_semana =[0,0,0,0,0,0,0]
    mes =calendario.monthdays2calendar(year, month)
    for semana in mes:
        for dias in semana:
            if dias[0] != 0:
                num_dias_semana[dias[1]] = num_dias_semana[dias[1]] + 1
    return num_dias_semana
 
 
##usar metodo
calendario = calendar.Calendar()
lista_dias_por_mes = num_dias_semanales_por_mes (calendario,2024,2)
print (lista_dias_por_mes)
resultado_horas_asignatura_SI = [0,0,0,0,0,0,0]
for i in range (0,7):
    resultado_horas_asignatura_SI[i] =  lista_dias_por_mes[i] * horas_semana_asignatura [0][i]
 
print (resultado_horas_asignatura_SI)