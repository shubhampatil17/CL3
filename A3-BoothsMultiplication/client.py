
from flask import Flask, render_template, request
import socket

app = Flask(__name__, template_folder="common", static_folder="common",static_url_path="")

multiplier = 0
multiplicand = 0

@app.route("/")
def renderWebApp():
	global multiplier
	global multiplicand

	clientsocket1 = socket.socket()
	clientsocket2 = socket.socket()

	host = socket.gethostname()
	port_s1 = 8888
	port_s2 = 8889

	clientsocket1.connect((host, port_s1))
	multiplier = clientsocket1.recv(1024)
	clientsocket1.close()

	clientsocket2.connect((host, port_s2))
	multiplicand = clientsocket2.recv(1024)
	clientsocket2.close()

	return render_template("app.html", multiplier=multiplier, multiplicand=multiplicand, result="")


@app.route("/boothsMultiplication", methods=["POST"])
def boothsDriver():
	global multiplier
	global multiplicand

	multiplier = request.form["multiplier"]
	multiplicand = request.form["multiplicand"]

	print multiplicand
	print multiplier

	if isdigit(multiplier) and isdigit(multiplicand):
		result = boothsMultiplicationAlgorithm(int(multiplier), int(multiplicand))
		return render_template("app.html", multiplier=multiplier, multiplicand=multiplicand, result="Success ! Multiplication is :"+str(result))
	else:
		result = "Error ! Wrong input."
		return render_template("app.html", multiplier=multiplier, multiplicand=multiplicand, result=result)

def boothsMultiplicationAlgorithm(multiplier, multiplicand):
	#write your booths logic in this function
	return multiplier*multiplicand

def isdigit(number):
	try:
		int(number)
		return True
	except:
		return False

if __name__=="__main__":
	app.run(host="0.0.0.0", debug=True)