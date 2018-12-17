class Client:
    def __init__(self,ip,port,username):
        self._ip = ip
        self._port = port
        self._username = username
    
    def getIp(self):
        return self._ip
    def getPort(self):
        return self._port
    def getUsername(self):
        return self._username