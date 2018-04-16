from flask import Flask, render_template, request
from difflib import get_close_matches
from collections import Counter
from forms import SearchForm
from dictionary.dict_data import load_data_to_dict

app = Flask(__name__)

app.config.from_object('config.settings')
app.config.from_pyfile('settings.py', silent=True)

our_dictionary = Counter(load_data_to_dict())


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm(request.form)
    query = request.args.get('q')

    if request.method == 'POST' and form.validate():

        word = form.word.data
        lower_word = word.strip().lower()
        proper_word = word.strip().title()
        upper_word = word.strip().upper()

        possibilities = [our_dictionary[lower_word], our_dictionary[proper_word], our_dictionary[upper_word]]

        meanings = max(possibilities, key=bool)

        if meanings:
            return render_template('/index.html', form=form, meanings=meanings, search_word=word)
        elif len(get_close_matches(lower_word, our_dictionary.keys(), cutoff=0.7)):
            return render_template('/index.html',
                                   form=form, matches=get_close_matches(lower_word, our_dictionary.keys(), cutoff=0.7))

        return render_template('/index.html', form=form, error_message='{} is not found'.format(word))
    elif query:
        return render_template('/index.html', form=form, meanings=our_dictionary[query], search_word=query)
    else:
        return render_template('/index.html', form=form)


if __name__ == '__main__':
    app.run()
