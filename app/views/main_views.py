from flask import Blueprint, render_template, request, url_for, jsonify, flash
from werkzeug.utils import redirect
import base64
import json
from .. import db
from app.models import User
from app.forms import UserForm
from PIL import Image
from PIL import Image
import os

bp = Blueprint('main', __name__, url_prefix='/')
txt_f = "/Users/wooseoknam/Desktop/Assignment#1/users.txt"

@bp.route('/')
def hello_world():
    return render_template('index.html')

@bp.route('/regist', methods = ['GET', 'POST'])
def regist():
    form = UserForm()
    f = form.image_name.data
    if request.method == 'POST':
        if f.filename != '':    # 첨부 O
            try:
                user = User(name=form.name.data, age=form.age.data, image_name='')

                db.session.add(user)
                db.session.commit()

                f.save('/Users/wooseoknam/Desktop/Assignment#1/app/static/uploads/' + f'{user.id}.jpg')

                img = Image.open('/Users/wooseoknam/Desktop/Assignment#1/app/static/uploads/' + f'{user.id}.jpg')
                with open(txt_f, 'a') as f:
                    data = {
                                'id': f"{user.id}",
                                'name': f'{form.name.data}',
                                'age': f'{form.age.data}'
                            }
                    f.write(json.dumps(data))
                    f.write('\n')

                return redirect(url_for('main.From'))
            except:    # 이미지 파일 X
                flash('이미지 파일이 아닙니다')
                db.session.delete(user)
                db.session.commit()
                os.remove('/Users/wooseoknam/Desktop/Assignment#1/app/static/uploads/' + f'{user.id}.jpg')
                return redirect(url_for('main.regist'))
        elif f.filename == '':    # 첨부 X
            user = User(name=form.name.data, age=form.age.data, image_name='')
            db.session.add(user)
            db.session.commit()

            with open(txt_f, 'a') as f:
                data = {
                            'id': f"{user.id}",
                            'name': f'{form.name.data}',
                            'age': f'{form.age.data}'
                        }
                f.write(json.dumps(data))
                f.write('\n')
            return redirect(url_for('main.From'))

    return render_template('form.html', form = form)



@bp.route('/users', methods = ['GET'])
def list_users():
    use_db = request.args.get('use_db')
    if use_db == '1':
        user_list = User.query.all()
    else:
        with open('users.txt', 'r') as f:
            lines = f.readlines()
            user_list = []
        for line in lines:
            id = (eval(line))['id']
            name = (eval(line))['name']
            age = (eval(line))['age']
            user = User(id=id, name=name, age=age)
            user_list.append(user)
            
    return render_template('user_list.html', user_list = user_list, use_db = use_db)



@bp.route('/detail/<int:user_id>/')
def detail(user_id):
    use_db = request.args.get('use_db')
    if use_db == '1':
        user = User.query.get_or_404(user_id)
    else:
        with open(txt_f, 'r') as f:
            users = f.readlines()
            user_lst = []
            for user in users:
                if eval(user)['id'] == str(user_id):
                    user_lst.append(user)
            user = user_lst[0]
        user_id = eval(user)['id']
        user = User(id = user_id, name = eval(user)['name'], age = eval(user)['age'])
    return render_template('user_detail.html', user = user, user_id = str(user_id))



@bp.route('/from')
def From():
    return render_template('type.html')



def create_thumbnail(image_path, thumbnail_path, size=(128, 128)):
    with Image.open(image_path) as img:
        img.thumbnail(size)
        img.save(thumbnail_path)



@bp.route('/image')
def get_image():
    user_id = request.args.get('user_id')
    image_path = '/Users/wooseoknam/Desktop/Assignment#1/app/static/uploads/' + str(user_id) + '.jpg'
    thumbnail_path = '/Users/wooseoknam/Desktop/Assignment#1/app/static/thumbnail/' + str(user_id) + '.jpg'

    create_thumbnail(image_path, thumbnail_path)

    with open(thumbnail_path, 'rb') as f:
        thumbnail_bytes = base64.b64encode(f.read()).decode('utf-8')
    response = {'thumbnail': 'data:image/jpeg;base64,' + thumbnail_bytes}
    return jsonify(response)