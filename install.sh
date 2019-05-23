#!/bin/bash

echo "----install Virtual environment----"
pip3 install virtualenv

cd ~/
echo ''
echo '---Загружаю репозиторий Blog---'
echo ''
git clone https://github.com/deepzeedi/Blog.git


cd ~/Blog
echo ''
echo '---Устанавливаю виртуальное окружение venv---'
echo ''

virtualenv venv



echo ''
if test -f './venv/bin/activate'
then 
    echo '---Активирую виртуальное окружение---'
    source venv/bin/activate
else
    echo 'xxx---виртуальное окружение не установлено!'
fi


echo ''
echo '---Устанавливаю Flask---'
echo ''

pip install flask

echo ''
echo '---Устанавливаю Flask Admin---'
echo ''

pip install flask_admin

echo ''
echo '---Устанавливаю Flask QLAlchemy---'
echo ''

pip install Flask-SQLAlchemy

echo ''
echo '---Устанавливаю Flask Migrate---'
echo ''

pip install Flask-Migrate

echo ''
echo '---Устанавливаю Flask Script---'
echo ''

pip install flask_script

echo ''
echo '---Устанавливаю Flask Security---'
echo ''

pip install flask_security

echo ''
echo '---Устанавливаю Flask jsonify---'
echo ''

pip install jsonify

echo ''
echo '---Устанавливаю requests---'
echo ''

pip install requests

echo ''
echo '---Запускаю сайт---'
echo '---на  localhost---'
echo ''

cd app
python main.py



