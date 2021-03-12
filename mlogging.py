#!/usr/bin/env python3
import logging, sys, os
from logging.handlers import RotatingFileHandler

def setup_logging(log_dir):
    # Main logger
    #main_logger = logging.getLogger()
    main_logger = logging.getLogger(__name__)
    main_logger.setLevel(logging.INFO)
    log_file_format = logging.Formatter("[%(levelname)s] - %(asctime)s - %(name)s - : %(message)s in %(pathname)s:%(lineno)d")
    log_console_format = logging.Formatter("[%(levelname)s]: %(message)s")

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(log_console_format)

    exp_file_handler = RotatingFileHandler('{}/exp_debug.log'.format(log_dir), maxBytes=10**6, backupCount=5) # 10MB file
    exp_file_handler.setLevel(logging.DEBUG)
    exp_file_handler.setFormatter(log_file_format)

    exp_errors_file_handler = RotatingFileHandler('{}/exp_error.log'.format(log_dir), maxBytes=10**6, backupCount=5)
    exp_errors_file_handler.setLevel(logging.WARNING)
    exp_errors_file_handler.setFormatter(log_file_format)

    main_logger.addHandler(console_handler)
    main_logger.addHandler(exp_file_handler)
    main_logger.addHandler(exp_errors_file_handler)
    return main_logger

if __name__ == "__main__":
    main_logger = setup_logging(os.path.dirname(os.path.abspath(__file__)))
    main_logger.info("setup logging module")