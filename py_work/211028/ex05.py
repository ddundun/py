from flask import Flask

app = Flask(__name__) 
# Flask가져와서 인스턴스화

@app.route("/")
def index():
    return "index"

@app.route("/aa/<ap1>")
def aa(ap1):
    return "aa"+ap1

@app.route("/aa/<int:bp1>")
def bb(bp1):
    bp1= str(bp1+10)
    return "bb"+str(bp1)
if __name__ =='__main__':
    app.run(debug=True)