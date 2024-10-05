from flask import Flask

app = Flask(__name__)

liste = "Teknoloji bağımlılığı zararlıdır çünkü ailene,çevrene,mahallene,şehrine,ülkene,dünyaya ve evrene tek bir katkının bile olmaması üzücüdür bu yüzden bağımlı olmayın ve faydalı bişeyler yapın,saygılar","teknoloji bağımlılığı seni sevdiklerinden ve dış dünyadan uzak tutar birazcık dışarı çıkıp ciğerlerini temiz havayla doldurmak istemez misin,saygılar","Teknoloji bağımlısı olup geçinemezsin bu yüzden sevdiğin başka işlerle ilgilenebilirsin,saygılar"
@app.route("/") #Url
def Hello_World():
    return"<h1>başka sayfalara geçmek için</h1>"

@app.route("/123") #Url
def Hello_Guest():
    return"<h1>heyyo world</h1>"

@app.route("/abc") #Url
def Hello_Intruder():
    return"<h1>hallo world</h1>"


app.run(debug = True)
