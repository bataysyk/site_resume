#!/usr/bin/python3
import requests

token = "*****************"
chat_id_to = ****************
last_send_log = ""

while True:
	file = open(r"/home/bataysk55/my_site/logs/debug6.log", "r")
	text = file.read().split("\n")
	lastlog = text[-2]
	if lastlog != last_send_log:
		last_send_log = lastlog
		requests.get(f'https://api.telegram.org/bot{token}/sendMessage',
                 	{'chat_id': chat_id_to,
                  	'text': f'{"=" * 40 + last_send_log}'})
