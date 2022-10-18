from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
import pandas as pd

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    # if request.method == 'POST':
    #     note = request.form.get('note')

    #     if len(note) < 1:
    #         flash('Note is too short!', category='error')
    #     else:
    #         new_note = Note(data=note, user_id=current_user.id)
    #         db.session.add(new_note)
    #         db.session.commit()
    #         flash('Note added!', category='success')
    df = pd.read_csv('/home/priyam/Flask_test/event.csv')
    la = df.iloc[-1:]
    last = la.iloc[0]
    last_time = last[0]
    last_date = last[1]
    last_temp = last[2]
    last_hum = last[3]
    return render_template("home.html", user=current_user, time=last_time, date=last_date, temp=last_temp, hum=last_hum)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
