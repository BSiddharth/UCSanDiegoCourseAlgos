# 2021-05-04-13-52-24.png


# isme galti samaj aagyi hai mujhe bas likhne mein alaas hai. most probably future mei samaj nhi aaega but shift down galat kar rha hoo. shift down mein dono child mei jo chotta hai usse swap karna chaiye jaise yha second round mei 1 , 3 se swap ho rha hai and 2 niche rhe jaa rha hai right mei

class Thread:
    def __init__(self, index):
        self.index = index
        self.time = 0

    def __str__(self):
        return str(self.index)


class AvailableThreads:
    def __init__(self, threadsList):
        self.len = len(threadsList)
        self.pq = threadsList

    # makes a priority queue

    def add(self, thread):
        self.pq.append(thread)

        self.len += 1
        index = len(self.pq) - 1
        if index != 0:
            while self.pq[index].index < self.pq[int((index-1)/2 if index//2 == 1 else (index-2)/2)].index:
                self.pq[index], self.pq[int((index-1)/2 if index//2 == 1 else (index-2)/2)] = self.pq[int(
                    (index-1)/2 if index//2 == 1 else (index-2)/2)], self.pq[index]

                index = int((index-1)/2 if index//2 == 1 else (index-2)/2)

                if index == 0:
                    break

    def getMin(self):
        print(self.pq[0].index, "will pick this at time", self.pq[0].time)
        self.pq[0], self.pq[-1] = self.pq[-1], self.pq[0]
        minThread = self.pq.pop(-1)
        self.len -= 1
        currentIndex = 0

        if (2*currentIndex) + 1 <= self.len-1:
            while self.pq[currentIndex].index > self.pq[(2*currentIndex) + 1].index:
                self.pq[currentIndex], self.pq[(
                    2*currentIndex) + 1] = self.pq[(2*currentIndex) + 1], self.pq[currentIndex]
                currentIndex = (2*currentIndex) + 1
                if (2*currentIndex) + 1 > self.len-1:
                    break

        if (2*currentIndex) + 2 <= self.len-1:
            while self.pq[currentIndex].index > self.pq[(2*currentIndex)+2].index:

                self.pq[currentIndex], self.pq[(
                    2*currentIndex) + 2] = self.pq[(2*currentIndex) + 2], self.pq[currentIndex]
                currentIndex = (2*currentIndex)+2
                if (2*currentIndex)+2 > self.len-1:
                    break
        return minThread

    # return min and print the thread index and current time

    def isEmpty(self):
        return self.len == 0


class WorkingThreads:
    def __init__(self):
        self.pq = []
    # initializes an empty pq

    def add(self, thread, time):
        thread.time += time

        self.pq.append(thread)
        index = len(self.pq) - 1

        if index != 0:
            while self.pq[index].time <= self.pq[int((index-1)/2 if index//2 == 1 else (index-2)/2)].time:
                if self.pq[index].time == self.pq[int((index-1)/2 if index//2 == 1 else (index-2)/2)].time:
                    if self.pq[index].index < self.pq[int((index-1)/2 if index//2 == 1 else (index-2)/2)].index:
                        self.pq[index], self.pq[int((index-1)/2 if index//2 == 1 else (index-2)/2)] = self.pq[int(
                            (index-1)/2 if index//2 == 1 else (index-2)/2)], self.pq[index]
                    else:
                        break
                else:
                    self.pq[index], self.pq[int((index-1)/2 if index//2 == 1 else (index-2)/2)] = self.pq[int(
                        (index-1)/2 if index//2 == 1 else (index-2)/2)], self.pq[index]

                index = int((index-1)/2 if index//2 == 1 else (index-2)/2)

                if index == 0:
                    break

    # this will apart from adding the thread to the pq , update the time of that thread

    def getFree(self):
        print([x.index for x in self.pq])
        self.pq[0], self.pq[-1] = self.pq[-1], self.pq[0]

        freeThread = self.pq.pop(-1)
        currentIndex = 0

        if (2*currentIndex) + 1 <= len(self.pq)-1:
            while self.pq[currentIndex].time >= self.pq[(2*currentIndex) + 1].time:
                if self.pq[currentIndex].time > self.pq[(2*currentIndex) + 1].time:
                    self.pq[currentIndex], self.pq[(
                        2*currentIndex) + 1] = self.pq[(2*currentIndex) + 1], self.pq[currentIndex]
                else:
                    if self.pq[currentIndex].index > self.pq[(2*currentIndex) + 1].index:
                        self.pq[currentIndex], self.pq[(
                            2*currentIndex) + 1] = self.pq[(2*currentIndex) + 1], self.pq[currentIndex]
                    else:
                        break

                currentIndex = (2*currentIndex) + 1
                if (2*currentIndex) + 1 > len(self.pq)-1:
                    break

        if (2*currentIndex) + 2 <= len(self.pq)-1:
            while self.pq[currentIndex].time >= self.pq[(2*currentIndex) + 2].time:
                if self.pq[currentIndex].time > self.pq[(2*currentIndex) + 2].time:
                    self.pq[currentIndex], self.pq[(
                        2*currentIndex) + 2] = self.pq[(2*currentIndex) + 2], self.pq[currentIndex]
                else:
                    if self.pq[currentIndex].index > self.pq[(2*currentIndex) + 2].index:
                        self.pq[currentIndex], self.pq[(
                            2*currentIndex) + 2] = self.pq[(2*currentIndex) + 2], self.pq[currentIndex]

                currentIndex = (2*currentIndex) + 2
                if (2*currentIndex) + 2 > len(self.pq)-1:
                    break
        return freeThread
    # returns the max priority element on the basis of min time

    def isEmpty(self):
        return self.len == 0


def scheduler(n, timingList):
    availableThreads = AvailableThreads([Thread(x) for x in range(n)])
    workingThreads = WorkingThreads()

    for x in timingList:
        if availableThreads.isEmpty():

            availableThreads.add(workingThreads.getFree())

        workingThreads.add(availableThreads.getMin(), x)


if __name__ == '__main__':
    # scheduler(2, [1, 2, 3, 4, 5])
    scheduler(4, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
