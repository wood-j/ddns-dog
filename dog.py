import json
import re
import time
import requests
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest
from aliyunsdkalidns.request.v20150109.UpdateDomainRecordRequest import UpdateDomainRecordRequest
from aliyunsdkcore.client import AcsClient
from common.log import logger
from common.try_except import try_except
from config import Config


class Dog:
    def __init__(self):
        self._config = Config.load()
        self._client = AcsClient(
            self._config.access_key,
            self._config.access_passwd
        )
        self._target_ip = ''

    def get_record(self, index: int):
        """ get the domain record on ali yun control center """
        req = DescribeDomainRecordsRequest()
        req.set_DomainName(self._config.domain)
        req.set_RRKeyWord(self._config.rr_list[index])
        resp = self._client.do_action_with_exception(req).decode()
        dic = json.loads(resp)
        records = dic['DomainRecords']['Record']
        if not records:
            raise Exception('record not exist')
        record = records[0]
        return record

    def update_record(self, index: int, record_id: str, ip: str):
        """ update domain item to target ip address """
        req = UpdateDomainRecordRequest()
        req.set_RR(self._config.rr_list[index])
        req.set_RecordId(record_id)
        req.set_Type('A')
        req.set_Value(ip)
        req.set_Line('default')
        resp = self._client.do_action_with_exception(req).decode()
        logger.debug(f'update domain response: {resp}')

    def get_ip_address(self):
        """ get ip address from cip.cc """
        url = 'http://www.cip.cc/'
        resp = requests.get(url)
        assert resp.status_code == 200, f'get ip address error code {resp.status_code}: {resp.text}'
        se = re.search(r'(?<=<pre>IP\s:\s)\d+\.\d+\.\d+\.\d+', resp.text)
        assert se, f'no ip address found from cip.cc'
        ip = se.group(0)
        logger.debug(f'got current ip: {ip}')
        return ip

    @try_except('process')
    def process(self):
        ip = self.get_ip_address()
        if ip == self._target_ip:
            logger.debug(f'local ip address has no changes: {ip}')
            return
        # record
        for i, rr in enumerate(self._config.rr_list):
            record = self.get_record(i)
            record_id = record['RecordId']
            record_ip = record['Value']
            if ip == record_ip:
                logger.debug(f'remote record ip address has no changes: {record_ip}')
                self._target_ip = ip
                continue
            # update
            self.update_record(i, record_id, ip)
            logger.debug(f'update record "{rr}" ip to: {ip}')
            self._target_ip = ip

    def run(self):
        while 1:
            self.process()
            logger.debug(f'wait 30 seconds for next loop ...')
            time.sleep(30)


if __name__ == '__main__':
    dog = Dog()
    dog.run()
