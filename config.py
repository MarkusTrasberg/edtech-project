
class Config(object):
    DEBUG = True
    TESTING = False


class DevelopmentConfig(Config):
    OPENAI_KEY = 'KEY HERE'
    COMPLETIONS_MODEL = "gpt-3.5-turbo"

    # EMBEDDINGS_MODEL_NEW = "text-embedding-ada-002"
    # COMPLETIONS_MODEL = "gpt-4-0314"
    # MAX_SECTION_LEN = 4000
    # if COMPLETIONS_MODEL == "gpt-3.5-turbo":
    #     MAX_SECTION_LEN = 3000

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}

