import os
import datetime
import inspect
import logging
import openpyxl

class BaseClass:

    def getLogger(self):
        # Get caller name (the test or function using this logger)
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        if not logger.handlers:
            #  Define log directory and file
            log_dir = "/Users/jaypatel/PycharmProjects/NEAP Demo/Logs"
            os.makedirs(log_dir, exist_ok=True)

            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            log_file = os.path.join(log_dir, f"test_log_{timestamp}.log")

            #  Define log format
            formatter = logging.Formatter(
                "%(asctime)s :%(levelname)s :%(name)s :%(funcName)s :%(lineno)d : %(message)s",
                "%Y-%m-%d %H:%M:%S"
            )

            #  File handler
            fileHandler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
            fileHandler.setFormatter(formatter)
            logger.addHandler(fileHandler)

            #  Console handler
            consoleHandler = logging.StreamHandler()
            consoleHandler.setFormatter(formatter)
            logger.addHandler(consoleHandler)

            #  Set level to DEBUG for detailed logs
            logger.setLevel(logging.DEBUG)

            logger.info(f"Logger initialized ? {log_file}")

        return logger

    def take_screenshot(self, name):
        """Capture screenshot and save to Reports/Screenshots folder"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_dir = "/Users/jaypatel/PycharmProjects/NEAP Demo/Screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        filepath = os.path.join(screenshot_dir, f"{name}_{timestamp}.png")
        self.driver.save_screenshot(filepath)
        return filepath

    def read_excel_data(self, file_path, sheet_name, row, col):
        try:
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook[sheet_name]
            value = sheet.cell(row=row, column=col).value
            self.log.info(f"Read Excel cell ({sheet_name}, {row}, {col}) => {value}")
            return value
        except Exception as e:
            self.log.error(f"Error reading Excel: {e}")
            raise