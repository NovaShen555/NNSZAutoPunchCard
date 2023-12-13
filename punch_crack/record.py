import requests
from .constants import RECORD_URL, HEADERS
from .export import *

def makeRecordPostContent(cardId: str = ""):
    return {
        "cardno": {cardId},
        "startdt": "2022-11-01",  
        "enddt": "2032-12-31",  
        "pageIndex": 1,  
        "pageSize": 100,  
        "sign": f"cardno={cardId}startdt=2022-11-01enddt=2032-12-31pageIndex=1pageSize=100"
    }

def __checkRecord(recordUrl: str = "", recordHeaders: str = "", recordData: dict = {}):
    return requests.post(
        url = recordUrl,
        data = recordData,
        headers = recordHeaders
    ).json()

def checkRecord(recordCardId: str | int = ""):
    recordCardId = str(recordCardId)
    return __checkRecord(RECORD_URL, HEADERS, makeRecordPostContent(recordCardId))

def exportRecordToCSV(recordCardId: str | int = "", exportFileName: str = "record.csv"):
    exportDictToCSV(exportFileName, ['Account', 'Terminal', 'RecordState', 'WorkPlaceName', 'DeptName1', 'DeptName2', 'RecordDT', 'UserName'], checkRecord(recordCardId)['data'])