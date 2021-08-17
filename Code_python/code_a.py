from configparser import ConfigParser , ExtendedInterpolation
import serial
import psutil
import time


#ACESSA ARQUIVO .CONF
config = ConfigParser(interpolation=ExtendedInterpolation())
config.read("serial.conf")

#RECEBE CONFIGURAÇÕES DO ARQUIVO SERIAL.CONF
port = config["SERIAL"]["PORT"]
baud = config["SERIAL"]["BAUDRATE"]
placa_rede = config["REDE"]["placa_rede"]

#INICIA COMUNICAÇÃO COM ARDUINO
arduino = serial.Serial()
arduino.baudrate = baud
arduino.port = port
arduino.open()


    #ARMAZENANDO ESTATISTICAS DO HARDWARE
info_net = psutil.net_if_addrs()
info_memory = psutil.virtual_memory() 
info_disk = psutil.disk_usage('/') 
boot_minutes = psutil.boot_time()/120
    #hardware_temp = psutil.sensors_temperatures(fahrenheit=False)
    #keylist = list(hardware_temp.keys())
    #for d in range(len(keylist)):
    #   print(f" {keylist[d]}  :{hardware_temp[keylist[d]][0].current}° Graus

stats = {
    "CPU_PERCENT":      psutil.cpu_percent(interval= 1) ,
    "MEMORY_TOTAL" :    int(info_memory.total/10000000) ,
    "MEMORY_AVAILABLE": int(info_memory.available /10000000),
    "MEMORY_USED"  :    int(info_memory.used/10000000),
    "HD" :              info_disk.percent,
    "IPV4" :            info_net[placa_rede][0].address,
    "TIME_BOOT":        boot_minutes
    }

print(stats)





