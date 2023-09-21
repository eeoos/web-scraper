from flask import Flask, render_template, request, redirect, send_file
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from extractors.incruit import extract_incruit_jobs
from extractors.saramin import extract_saramin_jobs
from file import save_to_file

app = Flask("JobScrapper")



# Flask는 user가 이 주소의 page를 방문했을 때 이 함수를 호출해야 하는 것을 알게 됨
@app.route("/") # @가 있는 코드를 함수 위에 위치시켜야 함 (decorator), syntatic sugar
def home():
   return render_template("home.html", name="nico")

db = {}

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None or keyword == "":
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        indeed = extract_indeed_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
   # incruit = extract_incruit_jobs(keyword)
   # saramin = extract_saramin_jobs(keyword)

        jobs = indeed + wwr
        db[keyword] = jobs
   # + incruit + saramin
    return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])    
    return send_file(f"{keyword}.csv", as_attachment=True)
app.run("127.0.0.1") # Replit에게 만든 웹사이트로의 접속을 열어달라고 알려주는 코드

