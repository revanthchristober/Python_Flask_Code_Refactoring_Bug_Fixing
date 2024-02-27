from flask import Flask, render_template, request, session

app = Flask(__name__)

# notes = []
app.secret_key = 'innomaticscoderefactorbugfixsecret4'
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        if note:
            notes = session.get('notes', [])
            notes.append(note)
            session['notes'] = notes
    notes = session.get('notes', [])
    return render_template("home.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
    print('Completed!')