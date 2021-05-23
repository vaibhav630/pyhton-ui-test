import logging

class LogGen:
    
    @staticmethod
    def loggen():
        logging.basicConfig(filename='.\\logs\\automatedTest.log',
                        format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger