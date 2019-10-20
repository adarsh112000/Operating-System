print("First In First Out Page replacement Algorithm.")

pages = []
queue = []
page_faults = 0
hits = 0
front = 0
rear = 0

n = int(input("Enter number of pages : "))

for i in range(n):
              page = int(input("Enter a page : "))
              pages.append(page)
del page

frameSize = int(input("Enter frame size : "))

for page in pages:
              if page not in queue:
                            if rear <frameSize:
                                          queue.append(page)
                                          rear +=1
                            elif rear==frameSize:
                                          queue.pop(front)
                                          queue.insert(front, page)
                                          front += 1
                                          if front==frameSize:
                                                        front=0
                            page_faults += 1
                            print("Queue : ", queue, " Miss : %d"%page)
              else:
                            hits += 1
                            print("Queue : ", queue, " hit : %d"%page)

print("Total Page Faults : %d"%page_faults)
print("Total Hits : %d"%hits)
