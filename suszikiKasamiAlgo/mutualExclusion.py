
class Process:
    def __init__(self,pid):
        self.processId = pid
        self.RN = {}
        self.token = None
        self.CS = None

class SuzukiKasami:
    def __init__(self):
        self.LN = []
        self.queue = []

    def request(self,process,processId):
        if process.token==True and processId==None:
            pass
        elif processId==None:
            process.RN[process.processId]+=1
            self.request(process, processId)
    
    def release(request):
        pass
    
    def start(self):
        pass
    

if __name__=='__main__':
    algo = Algo()
    algo.start()