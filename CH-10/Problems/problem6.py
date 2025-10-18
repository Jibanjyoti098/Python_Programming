from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo
   
    def book(slf, fro, to):
        print(f"Ticket is booked in train no: {slf.trainNo} from {fro} to {to}")
    def getStatus(slf):
        print(f"Train no: {slf.trainNo} is running successfully.")
    def getFare(slf, fro, to):
        print(f"Ticket fare in train no: {slf.trainNo} from {fro} to {to} is {randint(222, 5555)}")
              

t = Train(12377)
t.book("Cuttack", "Puri")
t.getFare("Cuttack", "Puri")
t.getStatus()
