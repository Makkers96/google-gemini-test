from flask import Flask, render_template, request, session
from main import run_llm

app = Flask(__name__)
app.secret_key = "thisisasupersecretkey124"

@app.route("/", methods=["GET", "POST"])
def google_test():

    if 'llm_response' not in session:
        session['llm_response'] = ""

    if request.method == 'POST':
        if 'prompt' in request.form:
            session['prompt'] = request.form.get('prompt')

            session['llm_response'] = run_llm(session['prompt'])

    return render_template("google_test.html",
                           llm_response=session['llm_response'],
                           )

if __name__ == "__main__":
    app.run()