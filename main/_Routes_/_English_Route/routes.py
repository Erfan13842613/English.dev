from flask import render_template, Blueprint, flash
from main import r
import re

english = Blueprint('english', __name__)


@english.route('/English')
@english.route('/home/English')
def English_Web():
    return render_template('EnglishTemplate/English_Web.html', flash=flash)


@english.route('/full_subtitle')
@english.route('/home/full_subtitle')
def Full_Subtitle_Web():
    text = r.get('SUBTITLE')
    if text is None:
        with open("main/static/english/Full_Subtitle.txt") as file:
            r.set('SUBTITLE', file.read())
            text = r.get('SUBTITLE')
    modified_text = None
    pattern = r'[â€™]'
    modified_text = re.sub(pattern, "'", text.decode('utf-8'))
    return render_template('EnglishTemplate/Full_Subtitle_Web.html', text=modified_text, flash=flash)


@english.route('/words')
@english.route('/home/words')
def English_Words_Web():
    English_words = []
    Persion_words = []
    r = re.compile('(\w+(?:\s+\w+)*)\s')
    with open('main/static/english/English.txt') as file:
        en_words = r.findall(file.read())
        for en_word in en_words:
            if en_word not in English_words:
                English_words.append(en_word)

    reg = re.compile('([\u0600-\u06FF]+(?:\s+[\u0600-\u06FF]+)*)\s*')
    with open('main/static/english/Persion.txt', encoding='utf-8') as file:
        pe_words = reg.findall(file.read())
        for pe_word in pe_words:
            if pe_word not in Persion_words:
                Persion_words.append(pe_word)
    return render_template('EnglishTemplate/English_Words_Web.html', English_words=English_words, Persion_words=Persion_words, zip=zip, flash=flash)


@english.route('/persion/full_subtitle')
@english.route('/home/persion/full_subtitle')
def Persion_Full_Subtitle_Web():
    text = None
    reg = re.compile('([\u0600-\u06FF]+(?:\s+[\u0600-\u06FF]+)*)\s*')
    with open('main/static/english/Persion_Full_Subtitle.txt', encoding='utf-8') as file:
        text = reg.findall(file.read())
    return render_template('EnglishTemplate/Persion_Full_Subtitle_Web.html', text=text, flash=flash)
