from flask import Blueprint, render_template
from flask_login import login_required, current_user

from flask import Flask, render_template, request, jsonify

views = Blueprint('views', __name__)


@views.route('/')
@login_required 
def home():
    return render_template('index.html', user=current_user)



@views.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)


