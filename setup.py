LOG_CONFIG = {
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
            'handlers': ['console']
        }
    }
}

RE_PATTERNS = {
    'chunk_size': '(\\d+)([mkMK]?$)',
}

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.55'
