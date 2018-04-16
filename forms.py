from wtforms import Form, StringField, validators


class SearchForm(Form):
    word = StringField('Word', [validators.DataRequired()])
