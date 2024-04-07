import datetime
import ipaddress

import Lista4_Final.functionalities as funcs
import functionalities
from abc import ABC,abstractmethod

class SSHLogEntry(ABC):
    def __init__(self,entry):
        self.time,self.hostname,self.pid,self.__content = functionalities.parse_entry(entry)

    def __str__(self):
        return f'{type(self).__name__}Object\t\tTime: {self.time}\tHostname: {self.hostname}\tPID: {self.pid}\tContent: {self.content}'
    def get_ip(self):
        ip = funcs.get_ipv4s_from_log(self.content)
        if ip:
            return ipaddress.IPv4Address(ip)
        else:
            return None
    @abstractmethod
    def validate(self):
        pass
    @property
    def has_ip(self):
        ip = self.get_ip(self)
        return ip !=None
    def __repr__(self):
        return self.__str__()



class PasswordFail(SSHLogEntry):
    def __init__(self,entry):
        super().__init__(entry)

class PasswordAccepted(SSHLogEntry):
    def __init__(self,entry):
        super().__init__(entry)

class Error(SSHLogEntry):
    def __init__(self,entry):
        super().__init__(entry)
class Other(SSHLogEntry):
    def __init__(self,entry):
        super().__init__(entry)

    def validate(self):
        return True




