import socket

HOST = '127.0.0.1'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	while True:
		msg = input("Введите сообщение (пустая строка — выход): ")
		if not msg:
			break
		s.sendall(msg.encode())
		data = s.recv(1024)
		print(f"Ответ сервера: {data.decode()}")