from flask import Flask
from alhimik_work.data import db_session
from alhimik_work.data.Users import User
from alhimik_work.data.Jobs import Jobs
import datetime
from flask import url_for
from flask import render_template
from flask import request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def Job():
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs)
    return render_template("base.html", jobs=news)


def main():
    # name_sql = input()
    db_session.global_init('db/base_blok.db')
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    user = User()
    user.surname = "Scot"
    user.name = "Ridl"
    user.age = 21
    user.position = "matros"
    user.speciality = "engineer"
    user.address = "module_2"
    user.email = "scot_mat@mars.org"
    db_sess.add(user)
    db_sess.commit()
    user = User()
    user.surname = "Kuznecov"
    user.name = "Alex"
    user.age = 21
    user.position = "строитель"
    user.speciality = "engineer"
    user.address = "module_2"
    user.email = "Kuznecoм_Alex@mars.org"
    db_sess.add(user)
    db_sess.commit()
    user = User()
    user.surname = "Matros"
    user.name = "Vladislav"
    user.age = 21
    user.position = "ученый"
    user.speciality = "биолог"
    user.address = "module_3"
    user.email = "Vladislav@mars.org"
    db_sess.add(user)
    db_sess.commit()
    user = db_sess.query(User).filter(User.id == 1).first()
    news = Jobs(job="deployment of residential modules 1 and 2",
                collaborators="2, 3", is_finished=True,
                work_size=15, user=user)
    db_sess.add(news)
    db_sess.commit()
    job = db_sess.query(Jobs).filter(Jobs.id == 1).first()
    job.finished_date = datetime.datetime.now() + datetime.timedelta(hours=15)
    user = db_sess.query(User).filter(User.id == 2).first()
    news = Jobs(job="deployment of 3 modules and station 1",
                collaborators="3, 4", is_finished=False,
                work_size=14, user=user)
    db_sess.add(news)
    db_sess.commit()
    job = db_sess.query(Jobs).filter(Jobs.id == 2).first()
    job.finished_date = datetime.datetime.now() + datetime.timedelta(hours=14)
    user = db_sess.query(User).filter(User.id == 3).first()
    news = Jobs(job="drone base deployment and 4 modules",
                collaborators="2, 4", is_finished=False,
                work_size=48, user=user)
    db_sess.add(news)
    db_sess.commit()
    job = db_sess.query(Jobs).filter(Jobs.id == 3).first()
    job.finished_date = datetime.datetime.now() + datetime.timedelta(hours=48)
    db_sess = db_session.create_session()
    app.run()


if __name__ == '__main__':
    main()
