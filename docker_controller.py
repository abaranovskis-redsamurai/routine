import os

os.system('docker stop RedSamuraiWLS')
os.system('docker rm RedSamuraiWLS')
os.system('docker rmi abaranovskis/redsamurai-wls:v8')
os.system('docker run -d -m 4g -p 7001:7001 --name RedSamuraiWLS abaranovskis/redsamurai-wls:v8')