import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'bugzap'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser1@zwcluster1-znjzd.mongodb.net/bugzap?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_bugs')
def get_bugs():
    return render_template("bugs.html", bugs=mongo.db.bug.find())


@app.route('/new_bug')
def new_bug():
    return render_template('new_bug.html', users=mongo.db.users.find(), categories=mongo.db.category.find())


@app.route('/insert_bug', methods=['POST'])
def insert_bug():
    bugs = mongo.db.bug
    bugs.insert_one(request.form.to_dict())
    return redirect(url_for('get_bugs'))


@app.route('/edit_bug/<bug_id>')
def edit_bug(bug_id):
    the_bug = mongo.db.bug.find_one({"_id": ObjectId(bug_id)})
    all_users = mongo.db.users.find()
    all_categories = mongo.db.category.find()
    return render_template('editbug.html', bug=the_bug, users=all_users, categories=all_categories)


@app.route('/update_bug/<bug_id>', methods=["POST"])
def update_bug(bug_id):
    bugs = mongo.db.bug
    bugs.update({'_id': ObjectId(bug_id)},
                {
        'bug_summary': request.form.get('bug_summary'),
        'bug_area': request.form.get('bug_area'),
        'bug_description': request.form.get('bug_description'),
        'bug_priority': request.form.get('bug_priority'),
        'bug_category': request.form.get('bug_category'),
        'bug_user': request.form.get('bug_user'),
    })
    return redirect(url_for('get_bugs'))


@app.route('/delete_bug/<bug_id>')
def delete_bug(bug_id):
    mongo.db.bug.remove({'_id': ObjectId(bug_id)})
    return redirect(url_for('get_bugs'))


@app.route('/get_categories')
def get_categories():
    return render_template('categories.html', categories=mongo.db.category.find())


@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
                           category=mongo.db.category.find_one(
                               {'_id': ObjectId(category_id)}))


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.category.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('get_categories'))


@app.route('/get_users')
def get_users():
    return render_template('user_admin.html', users=mongo.db.users.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(
        os.environ.get('PORT')), debug=True)
