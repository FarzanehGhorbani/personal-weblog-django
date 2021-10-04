# Intrudoction
This website is a personal website to introduce your services that you can easily use to introduce a company or person. This site includes the following sections:
Introduction

Publishers

researches

students

articles

Education

And the communication part.

In the introduction section, the person or company is introduced and awards and honors are mentioned.

In the publishing section, the published books are mentioned, the specifications of which can be viewed by clicking on each one.

The research section includes sections on current issues that you are researching and the organizations that sponsored the projects and the research partners.

The student section includes all of your successful students.

The articles section, the research is completed.

The training section includes lessons and topics that you have provided so far.

In the communication section, all communication channels are mentioned and you can express your opinions and criticisms.

# Setup
The first thing to do is to clone the repository:

$ git clone https://github.com/FarzanehGhorbani/personal-weblog-django

Create a virtual environment to install dependencies in and activate it:

$ virtualenv2 --no-site-packages env
$ source env/bin/activate

Then install the dependencies:

(env)$ pip install -r requirements.txt

Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once pip has finished downloading the dependencies:

(env)$ python manage.py runserver

And navigate to http://127.0.0.1:8000.
