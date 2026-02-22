from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://remotive.com/api/remote-jobs"

@app.route("/")
def home():
    search = request.args.get("search", "")
    category = request.args.get("category", "")
    company = request.args.get("company", "")
    page = int(request.args.get("page", 1))

    params = {}

    if search:
        params["search"] = search
    if category:
        params["category"] = category
    if company:
        params["company_name"] = company

    response = requests.get(API_URL, params=params)
    data = response.json()

    all_jobs = data.get("jobs", [])
    per_page = 10
    start = (page - 1) * per_page
    end = start + per_page

    jobs = all_jobs[start:end]
    total_pages = len(all_jobs) // per_page + (1 if len(all_jobs)% per_page else 0 )

    return render_template("index.html", jobs=jobs, search=search, category = category, company = company, page=page, total_pages=total_pages)

if __name__ == "__main__":
    app.run(debug=True)