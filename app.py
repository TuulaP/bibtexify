
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask import Flask, render_template, flash, request
from bibtexify import bibtexifyISBN
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'adfadfadfadadaf1341adfab'


class ReusableForm(Form):
    name = TextField('ISBN:', validators=[validators.required()])

    @app.route("/", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)

        print(form.errors)
        if request.method == 'POST':
            name = request.form['name']
            print(name)

        if form.validate():
            # Save the comment here.
            text = bibtexifyISBN(name)
            if text is not None:
                print("<PRE>"+text+"</PRE>")
                flash('Data Found\n'+text)
            #flash("For {0}: {1}".format("991", text))
            # flash(bibtexifyISBN(name))

        else:
            flash('Error: All the form fields are required. ')

        return render_template('hello.html', form=form)


@app.route('/hi')
def hello2():
    print(os.environ['APP_SETTINGS'])
    return "Bibtex from ISBN"


@app.route('/<name>')
def hello_name(name):
    return "Hello {} x !".format(name)


if __name__ == '__main__':
    app.run()
    app.debug = True
