class DevelopmentConfig():
    DEBUG = True

class ProductionConfig():
    DEBUG = False

config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)