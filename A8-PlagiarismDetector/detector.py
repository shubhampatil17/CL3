from flask import Flask, render_template, request

app = Flask(__name__, template_folder="common", static_folder="common", static_url_path="")


@app.route("/")
def renderApp():
	return render_template("app.html")

@app.route("/plagiarismDetection", methods=["POST"])
def plagiarismDetection():
	data = request.form["inputText"]

	if data == "":
		return render_template("app.html", result="Error ! No input !", text=data)



	#detection logic goes here


	plagiarismRatio = 90
	return render_template("app.html", result = "Test Completed ! Plagiarism Ratio :" + str(plagiarismRatio)+"%", text=data)

if __name__=="__main__":
	app.run(host="0.0.0.0", debug=True)