from flask import Flask, render_template, request, flash, redirect
from forms import UploadImageForm

app = Flask(__name__)

@app.route('/upload', methods=["GET", "POST"])
def signup():
    """Handle display and processing of image uploads

    If form not valid, present form.
    """

    form = UploadImageForm()

    if form.validate_on_submit():
        # if we make it here, form passes WTForms validation
        # step 1: fetch image from form
        # step 2: upload image to s3 and get URL
        url = ''
        # step 3: redirect to image
        return redirect(f"{url}")

    else:
        return render_template('upload-form.html', form=form)

"""
@app.route('/signup', methods=["GET", "POST"])
def signup():

    do_logout()

    # the logout method.

    form = UserAddForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                username=form.username.data,
                password=form.password.data,
                email=form.email.data,
                image_url=form.image_url.data or User.image_url.default.arg,
            )
            db.session.commit()

        except IntegrityError:
            flash("Username already taken", 'danger')
            return render_template('users/signup.html', form=form)

        do_login(user)

        return redirect("/")

    else:
        return render_template('users/signup.html', form=form)

"""