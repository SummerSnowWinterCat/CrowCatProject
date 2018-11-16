from crow_cat import crow_cat_body
from crow_cat import crow_cat_create
from flask_script import Manager, Shell, Server
from flask_migrate import Migrate, MigrateCommand
import os

crow_cat_runner = crow_cat_create(os.getenv('FLASK_CONFIG') or 'default')
crow_cat_manager = Manager(crow_cat_runner)


# crow_cat_migrate = Migrate(crow_cat_runner)


def make_shell_context():
    return dict(crow_cat_runner=crow_cat_runner)
    crow_cat_manager.add_command('shell', Shell(make_context=make_shell_context))
    crow_cat_manager.add_command('runserver', host='0.0.0.0')


if __name__ == '__main__':
    print("===================================")
    print("<<<<<<crow-cat-server on!>>>>>>")
    print("===================================")
    crow_cat_manager.run()
