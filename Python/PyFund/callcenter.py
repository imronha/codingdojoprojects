class Call(object):
    def __init__(self, id_unique, name, number, time, reason):
        self.id_unique = id_unique
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
    def display_all(self):
        print "Unique ID: "+str(self.id_unique)
        print "Name: "+str(self.name)
        print "Number: "+str(self.number)
        print "Time: "+str(self.time)
        print "Reason: "+str(self.reason)

calls = Call(149, "Imron", 9167644580, "7pm", "Complaint")
call2 = Call(900, "Ethan", 4840831283, "5pm", "fsdkfjh")
class CallCenter(object):
    def __init__(self, calls):
        self.calls = calls
        self.queue_size = len(self.calls)
    def add_call(self, new_call):
        self.calls.append(new_call)
        return self
    def remove_call(self):
        self.calls.pop(0)
        return self
    def info(self):
        for i in self.calls:
          i.display_all()
          print "Calls in queue: "+str(self.queue_size)

ucdmc = CallCenter([calls])
ucdmc.add_call(call2).info()
