import logging

from .hw import MFRC522

logger = logging.getLogger(__name__)


class RfidReader:
    def __init__(self):
        self.RFID_READER = MFRC522()
        logger.debug("Initializing RfidReader")

    def read(self):
        id, text = self.RFID_READER.read_no_block()
        counter = 0
        while id == "No_RFID_Reader_Connected" or id == "Multiple_Reader_isActice":
            if counter > 4:
                return self.RFID_READER.read_no_block()
            id, text = self.RFID_READER.read_no_block()
            counter += 1
        return id, text

    def read_id(self):
        id = self.RFID_READER.read_id_no_block()
        counter = 0
        while id == "No_RFID_Reader_Connected" or id == "Multiple_Reader_isActice":
            if counter > 4:
                return self.RFID_READER.read_id_no_block()
            counter += 1
            id = self.RFID_READER.read_id_no_block()
        return id
