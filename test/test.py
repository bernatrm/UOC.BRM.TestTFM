from datetime import datetime
import tfm_helpers

tfm_helpers.createDirIfNoExists('data\\processed\\snapshots\reservas\\csv\\2010')

now = datetime.now()

print(f"{now.year}{now.strftime('%m')}{now.strftime('%d')}")
print(now.strftime('%m'))
print(now.strftime('%d'))


print(now.day)
print(now.month)
print(now.year)
print(now.hour)
print(now.minute)