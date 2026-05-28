import socket

HOST = '192.168.100.39'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	print(f'Сервер слушает {HOST}:{PORT}')
	s.settimeout(30)
	try:
    		conn, addr = s.accept()
	except socket.timeout:
		print("Никто не подключился за 30 секунд.")
		exit()
	with conn:
		print(f'Подключён клиент {addr}')
		while True:
			data = conn.recv(1024)
			if not data:
				break
			print(f'Получено: {data.decode()}')
			conn.sendall(data)  # эхо