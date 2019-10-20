at = []
bt = []
ct = []
tat = []
wt = []
p = []
atat = 0
awt = 0
top = 0

size = int(input("Enter the number of processes : "))

print("Non Pre-emptive Shortest Job Scheduling.")
print("Consider the arrival time as 0 for all processes.")

for i in range(size):
              p.append("P%d"%(i+1))
              at.append(0)
              time = int(input("Enter the burst time for process P%d : "%(i+1)))
              bt.append(time)
del time

for i in range(size):
              for j in range(0, size-i-1):
                            if bt[j]>bt[j+1]:
                                          bt[j], bt[j+1] = bt[j+1], bt[j]
                                          p[j], p[j+1] = p[j+1], p[j]

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
              print(p[i]+"\t"+str(at[i])+"\t"+str(bt[i])+"\t"+str(ct[i])+"\t"+str(tat[i])+"\t"+str(wt[i]))

print("Average Turn Around Time : %fm/s"%atat)
print("Average Waiting Time : %fm/s"%awt)
