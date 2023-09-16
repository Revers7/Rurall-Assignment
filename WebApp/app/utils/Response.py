class Response:
    json_resp={}
    def __init__(self,er_code,reason):
        self.json_resp = {
            "err_code":er_code,
            "failure_reason":str(reason)
        }
    def add_key(self,key,value):
        self.json_resp[key] = value
    
    def setErrCode(self,err_code):
        self.json_resp['err_code'] = err_code
        
    def setFailReason(self,reason):
        self.json_resp['failure_reason'] = reason
