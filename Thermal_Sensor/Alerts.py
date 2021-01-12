from twilio.rest import Client
import serial
import time
ser = serial.Serial('COM3', 9600)

account_sid = 'AC2969e30e24a9e996afc384dcc1319fd5'  
auth_token = '31198ffd1afeec4a845b2ab3fd2c55e3'
client = Client(account_sid, auth_token)
suhu_tinggi = 38
suhu_rendah = 32

while True:
	while ser.inWaiting():
		temp=float(ser.readline().decode())
		if temp > suhu_tinggi:
			messageTosend="Suhu Tubuh Tinggi (Bahaya !!!). Suhu: "+str(temp)+"*C"""
		elif (temp > suhu_rendah and temp < suhu_tinggi):
			messageTosend="Suhu Tubuh Normal. Suhu: "+str(temp)+"*C"""
		else:
			messageTosend="Suhu Tubuh Rendah (Spoofing !!!). Suhu: "+str(temp)+"*C""" 

		message=client.messages.create(
			body=messageTosend,
			from_='whatsapp:+14155238886',
			to='whatsapp:+6282364642717'
        	)
		time.sleep(10)

print(message.sid)	