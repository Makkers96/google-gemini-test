from flask import Flask, render_template, request, session
from main import run_llm

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def google_test():

    llm_response = ""

    if request.method == 'POST':
        if 'prompt' in request.form:
            prompt = request.form.get('prompt')

            global llm_response
            llm_response = run_llm(prompt)

    return render_template("google_test.html",
                           llm_response=llm_response,
                           )

if __name__ == "__main__":
    app.run()