_DEFAULT_LOG_CONFIG = {
    'version': 1,
    'formatters': {
        'normal': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'detailed': {
            'format': '%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'normal',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'detailed',
            'filename': './execution.log',
            'maxBytes': 1024,
            'backupCount': 3
        }
    },
    'loggers': {
        'myctftools': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        }
    }
}


