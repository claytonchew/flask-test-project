import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail


def save_picture(picture_upload):
    random_hex = secrets.token_hex(16)
    _, extension = os.path.splitext(picture_upload.filename)
    picture_filename = random_hex + extension
    picture_path = os.path.join(
        current_app.root_path, "static/profile_pics", picture_filename
    )

    with Image.open(picture_upload) as img:
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
        img.save(picture_path)

    return picture_filename


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message(
        "Password Reset Request",
        sender="noreply@claytonchew.com",
        recipients=[user.email],
    )
    msg.body = f"""To reset your password, visit the following link: 
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request, then simply ignore this email.
"""
    mail.send(msg)
