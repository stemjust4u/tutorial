#!/usr/bin/env python3
import logging, sys, os, systemd.daemon
from systemd.journal import JournalHandler
from logging.handlers import RotatingFileHandler

def setup_logging(log_dir):
    # Main logger
    ''' 
    If main and journal use same name in getLogger then can't control individually
    If main/journal=INFO    then ALL (both loggers) info's get journal'd and logged
    If main=CRIT,journ=INFO then only journal.info's get journal'd
    If main=INFO,journ=CRIT then nothing journal'd but main info is logged
    $ journalctl --since "1 hour ago"
    '''
    main_logger = logging.getLogger(__name__)
    journal_logger = logging.getLogger('journal')
    #main_logger = logging.getLogger(__name__)
    main_logger.setLevel(logging.CRITICAL)
    journal_logger.setLevel(logging.INFO)  # use logging.CRITICAL to turn logging off

    log_file_format = logging.Formatter("[%(levelname)s] - %(asctime)s - %(name)s - : %(message)s in %(pathname)s:%(lineno)d")
    log_console_format = logging.Formatter("[%(levelname)s]: %(message)s")
    journal_format = logging.Formatter("[%(levelname)s] - %(name)s - : %(message)s in %(pathname)s:%(lineno)d")

    journal_logger.addHandler(JournalHandler())

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
    return main_logger, journal_logger

if __name__ == "__main__":
    main_logger, journal_logger = setup_logging(os.path.dirname(os.path.abspath(__file__)))   
    main_logger.info("Testing logger output")
    journal_logger.info(__file__ + ' Marking journal')

    mylist = [1, 2]
    try:
        print(mylist[4])
    except Exception as e:
        main_logger.error("exception error", exc_info=True)
        journal_logger.error("exception error", exc_info=True)