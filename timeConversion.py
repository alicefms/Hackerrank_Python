def timeConversion(s):
    hora = int(s[0:2])
    minuto = s[3:5]
    segundo = s[6:8]
    periodo = s[8:10]

    if ('PM' in periodo) and (hora != 12):
        hora = hora + 12
    if ('AM' in periodo) and (hora == 12):
        hora = 0

    return str(hora).zfill(2)+":"+ minuto+":"+ segundo

print(timeConversion("12:00:00AM"))
