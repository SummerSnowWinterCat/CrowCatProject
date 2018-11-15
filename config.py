import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_crow_cat(crow_cat):  # 执行当前需要的环境的初始化
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


# class ProductionConfig(Config):
class ProductionConfig(Config):  # 生产坏境
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'devlopment': DevelopmentConfig,
    'tesing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
