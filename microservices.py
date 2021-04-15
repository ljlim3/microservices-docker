from flask import Flask, render_template
import subprocess

app = Flask(__name__)

#app.register_blueprint(mod)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/on')
def run_script():
    subprocess.call(['docker run -ti --rm -e DISPLAY=192.168.1.69:0 -v /tmp/.X11-unix:/tmp/.X11-unix git'], shell=True)
    return '', 204 

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)