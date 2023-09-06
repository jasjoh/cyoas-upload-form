from flask_wtf import FlaskForm
from wtforms import FileField



class UploadImageForm(FlaskForm):

    image_file = FileField(
        'Image file',

    )
