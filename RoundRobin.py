at = []
bt = []
copy_bt = []
ct = []
tat = []
atat = 0
awt = 0
top = 0
p = []

print("Round Robin CPU Scheduling Algorithm.")
print("Consider arrival time as 0 for all processes.\n")

size = int(input("Enter number of processes : "))
quantum = int(input("Enter the quantum : "))
wt = [0]*size
for i in range(size):
              p.append("P%d"%(i+1))
              at.append(0)
              time = int(input("Enter the burst time of P%d : "%(i+1)))
              bt.append(time)
              copy_bt.append(time)
del time

while(True):
              done = True

              for i in range(size):
                            if(copy_bt[i]>0):
                                          done = False
                                          if(copy_bt[i]>quantum):
                                                        top += quantum

                                                        copy_bt[i] -= quantum
                                          else:
                                                        top += copy_bt[i]
                                                        wt[i] = top-bt[i]
                                                        copy_bt[i] = 0

              if done == True:
                            break

for i in range(size):
              tat.append(bt[i]+wt[i])
              awt += wt[i]
              atat += tat[i]
              
awt /= size
atat /= size

print("Process\tArrivalTime\tBurstTime\tTurnAroundTime\tWaitingTime")
for i in range(size):
              print(p[i]+"\t"+str(at[i])+"\t"+str(bt[i])+"\t"+"\t"+str(tat[i])+"\t"+str(wt[i]))

print("Average TurnAroundTime : %fm/s"%atat)
print("Average Waiting Time : %fm/s"%awt)
