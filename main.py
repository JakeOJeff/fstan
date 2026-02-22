from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://remotive.com/api/remote-jobs"

@app.route("/")
def home():
    search = request.args.get("search", "")
    category = request.args.get("category", "")
    company = request.args.get("company", "")

    params = {}

    if search:
        params["search"] = search
    if category:
        params["category"] = category
    if company:
        params["company_name"] = company

    response = requests.get(API_URL, params=params)
    data = requests.json()

    jobs = data.get("jons", [])
    return