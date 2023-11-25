class Config_Dev():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Admin@localhost/rehvital_ips_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Config_Prod():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://g2dsg34n0iq6:AdminRehvital.2023*@186.155.143.109/rehvital_ips_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False