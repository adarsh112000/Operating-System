#CPU scheduling algorithms.
#Round Robin

at = []
bt = []
ct = []
tat = []
wt = []
atat = 0
awt = 0
top = 0
p = []
priority = []

print("Non pre-emptive Priority Scheduling Algorithm.")
print("Consider arrival time as 0 for all processes.")

size = int(input("Enter number of processes : "))

for i in range(size):
              p.append("P%d"%(i+1))
              at.append(0)
              time = int(input("Enter brust time of P%d : "%(i+1)))
              bt.append(time)
              pri = int(input("Enter priority of P%d : "%(i+1)))
              priority.append(pri)
del time, pri

for i in range(size):
              for j in range(0, size-i-1):
                            if priority[j]<priority[j+1]:
                                          bt[j], bt[j+1] = bt[j+1], bt[j]
                                          priority[j], priority[j+1] = priority[j+1], priority[j]
                                          p[j], p[j+1] = p[j+1], p[j]

for i in range(size):
              if i==0:
                            top +=bt[i]
                            ct.append(top)
              elif i>0:
                            if top<at[i]:
                                          top = at[i] + bt[i]
                                          ct.append(top)
                            else:
                                          top+=bt[i]
                                          ct.append(top)

for i in range(size):
              tat.append(ct[i]-at[i])
              wt.append(tat[i]-bt[i])
              atat += tat[i]
              awt += wt[i]

awt /= size
atat /= size

print("Process\tArrivalTime\tBurstTime\tPriority\tCompletionTime\tTurnAroundTime\tWaitingTime")
for i in range(size):
              print(p[i]+"\t"+str(at[i])+"\t"+str(bt[i])+"\t"+str(priority[i])+"\t"+str(ct[i])+"\t"+str(tat[i])+"\t"+str(wt[i]))

print("Average TurnAroundTime : %fm/s"%atat)
print("Average Waiting Time : %fm/s"%awt)

#-- Adarsh Choudhary
