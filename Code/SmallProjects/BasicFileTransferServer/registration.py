#! /usr/bin/python3

from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField

class RegistrationFrom(Form):
    """Registration class with validators"""
    username = TextField("Enter username",[validators.Required("Please enter your name.")])
    email = TextField("Enter your email",[validators.Required("Please enter your email address"),\
    validators.Email("Please enter your email address")])
    password = PasswordField("Enter your password")
    submit = SubmitField("Send")
    rpassword = PasswordField("Confirm your password")

