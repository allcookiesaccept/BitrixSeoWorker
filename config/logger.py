import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)
# update

def log_func_calls(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Вызвана функция: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper
