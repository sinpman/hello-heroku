import os
import datetime

from flask import Flask, redirect, render_template, request, url_for, session
from flask_session import Session
from flask_bcrypt import generate_password_hash, check_password_hash
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')