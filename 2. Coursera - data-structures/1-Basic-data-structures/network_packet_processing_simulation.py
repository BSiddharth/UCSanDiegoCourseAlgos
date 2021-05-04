# 2021-04-13-12-11-50.png

from basicDS import Queue, DoubleNode


class processingNode:
    def __init__(self, arrivalTime, timeToComplete):
        self.arrivalTime = arrivalTime
        self.timeToComplete = timeToComplete


def process(buffer, arrivalTimeList=[], timeToCompleteList=[]):
    currentTime = 0
    successList = [0]*len(arrivalTimeList)

    if buffer >= 1 and len(successList) >= 1:
        successList[0] = arrivalTimeList[0]
    if len(arrivalTimeList) != 0:
        processingQueue = Queue(DoubleNode(processingNode(
            arrivalTimeList[0], timeToCompleteList[0])))

    for i in range(1, len(arrivalTimeList)):
        if processingQueue.length < buffer:
            processingQueue.addAtLast(DoubleNode(processingNode(
                arrivalTimeList[i], timeToCompleteList[i])))
        else:
            if processingQueue.first.key.timeToComplete + currentTime <= arrivalTimeList[i]:
                successList[i] = arrivalTimeList[i]
                currentTime += processingQueue.first.key.timeToComplete
                processingQueue.popFirst()
                processingQueue.addAtLast(DoubleNode(processingNode(
                    arrivalTimeList[i], timeToCompleteList[i])))
            else:
                successList[i] = -1

    for x in successList:
        print(x)


if __name__ == '__main__':

    process(1),
    process(1, [0], [0]),
    process(1, [0, 0], [1, 1]),
    process(1, [0, 1], [1, 1]),
