d = float(input('Informe a distância (em metros): '))
cm = d * 100
mm = cm * 10
dm = d * 10
dam = d / 10
hm = dam / 10
km = hm / 10
print(' O valor da distância apresentada convertido em: \n\n {:.2f} mm \n {:.2f} cm'.format(mm, cm))
print(' {:.2f} dm \n {:.2f} dam \n {:.2f} hm \n {:.2f} km'.format(dm, dam, hm, km))
