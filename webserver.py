import socketserver
from os import path

class WebServer(socketserver.BaseRequestHandler):
	def serve_content(self, path, headers):
		with open(path, 'r') as f:
			lines_list = f.readlines()
			content = "\n".join(lines_list)
			response = headers + content
			self.request.sendall(response.encode())

	def handle(self):
		self.data = self.request.recv(1024).strip()
		request_list = self.data.decode().split()
		if len(request_list) == 0:
			self.request.send("HTTP/1.0 404 Not Found\r\n\r\n".encode())
			return
		request_method = request_list[0] # want to response 405 if this is not GET
		if request_method != "GET":
			self.request.send("HTTP/1.0 405 Method Not Allowed\r\n\r\n".encode())
			return
		address = request_list[1]
		file_name = address[1:] # get rid of the "/"
		if '../' in file_name:
			# if tries to access any thing above www/
			self.request.send("HTTP/1.0 404 Not Found\r\n\r\n".encode())
			return
		file_path = "./content/" + file_name
		if path.isfile(file_path) and path.exists(file_path):
			text_type = file_name.split('.')[-1].strip()
			headers = "HTTP/1.0 200 OK\r\nContent-Type: text/" + text_type + "\r\n\r\n"
			self.serve_content(file_path, headers)
		else:
			self.request.send("HTTP/1.0 404 Not Found\r\n\r\n".encode())

if __name__ == "__main__":
	HOST, PORT = "localhost", 8080
	socketserver.TCPServer.allow_reuse_address = True
	server = socketserver.TCPServer((HOST, PORT), WebServer)
	server.serve_forever()
