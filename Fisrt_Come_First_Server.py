#CPU scheduling algoritms.
#First Come First Serve

at = []
bt = []
ct = []
tat = []
wt = []
atat = 0
awt = 0
top = 0

size = int(input("Enter the number of processes : "))

for i in range(size):
              time = int(input("Enter the arrival time for process P%d : "%(i+1)))
              at.append(time)
              time = int(input("Enter the burst time for process P%d : "%(i+1)))
              bt.append(time)
del time

for i in range(size):
              if i==0:
                            top += bt[i]
                            ct.append(top)
              elif i>0:
                            if top<at[i]:
                                          top = at[i]+bt[i]
                                          ct.append(i)
                            else:
                                          top+=bt[i]
                                          ct.append(top)

for i in range(size):
              tat.append(ct[i] - at[i])
              wt.append(tat[i] - bt[i])
              atat +=tat[i]
              awt +=wt[i]

atat = atat/size
awt = awt/size

print("Process \t Arrival Time\tBurst Time\tCompletion Time\tTurnAroundTime\tWaiting Time")
for i in range(size):
              print("P%d"%(i+1)+"\t"+str(at[i])+"\t"+str(bt[i])+"\t"+str(ct[i])+"\t"+str(tat[i])+"\t"+str(wt[i]))

print("Average Turn Around Time : %fm/s"%atat)
print("Average Waiting Time : %fm/s"%awt)

#--Adarsh Choudhary
