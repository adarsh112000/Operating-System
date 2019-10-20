#Page Replacement Algorithms.
#Least recently used.

print("Least recent used (LRU) page replacement algorithm")

pageFaults = 0
hits = 0
queue = []
recentQueue = []
pages = []
rear = 0
front = 0

n = int(input("Enter number of pages : "))

for i in range(n):
              page = int(input("Enter a page : "))
              pages.append(page)
del page

frameSize = int(input("Enter frame size : "))

for page in pages:
              if page not in queue:
                            if rear<frameSize:
                                          queue.append(page)
                                          rear += 1
                                          recentQueue.append(page)
                            elif rear==frameSize:
                                          new_page = recentQueue.pop(front)
                                          pageindex = queue.index(new_page)
                                          queue.pop(pageindex)
                                          queue.insert(pageindex, page)
                                          recentQueue.append(page)

                            pageFaults += 1
                            print("Queue : ", queue, " Miss : ", page)
              else:
                            hits += 1
                            new_page = recentQueue.pop(recentQueue.index(page))
                            recentQueue.append(new_page)
                            print("Queue : ", queue, " Hit : ", page)

print("Page Faults : ", pageFaults)
print("Hits : ", hits)

#--Adarsh Choudhary
