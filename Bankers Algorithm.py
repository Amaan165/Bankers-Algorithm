import numpy as np


def display(allocation, need, max, Process):
    if len(allocation) == 0 or len(need) == 0 or len(max) == 0:
        return
    print("So, State of System Currently is: \n")
    print("Process ID\t\tAllocated\t\t Maximum\t\t  Need")
    global Resource
    x = Resource[0] + " " + Resource[1] + " " + Resource[2]
    x = x.center(9)
    print("           \t\t" + x + "\t\t" + x + "\t\t" + x)
    for i in range(len(need)):
        processFormat = Process[i].center(10)
        allocFormat = ' '.join([str(a) for a in allocation[i]]).center(9)
        maxFormat = ' '.join([str(a) for a in max[i]]).center(9)
        needFormat = ' '.join([str(a) for a in need[i]]).center(9)
        print(processFormat + "\t\t" + allocFormat + "\t\t" + maxFormat + "\t\t" + needFormat)


def safety(A, N, M, P, AV):
    arr1 = np.array(AV)
    safety = []
    i = 0
    while i != n:
        for j in range(len(N)):
            arr2 = np.array(N[j])
            if np.all(arr2 <= arr1):
                print("Presently Available: " + str(arr1))
                arr1 = arr1 + np.array(A[j])
                display(A, N, M, P)
                A.pop(j)
                N.pop(j)
                M.pop(j)
                print()
                print(
                    "Process " + P[j] + "'s need is less then the available ,Hence we can give available resource to " +
                    P[j])
                print("                 So now Available: " + str(arr1))
                safety.append(P[j])
                P.pop(j)
                print()
                break
        else:
            if len(N) != 0:
                print("SYSTEM: DeadLock Occurred")
                SystemExit(0)
        i += 1
        print()

    print("All Processes have received their resources as per their needs.")
    print("Hence, System is NOT in Deadlock!")
    print("Therefore, Safe Sequence is: ")
    print(safety)
    return 0


def request(A1, N1, M1, P1, AV1):
    print("\n")
    y = input("Enter the process which makes the request: ")
    Req = []
    print()
    for i in Resource:
        t = "Enter the request for resource of type " + i + ": "
        j = int(input(t))
        Req.append(j)

    t = Process.index(y)
    ar = np.array(Req)
    ar1 = np.array(N1[t])
    ar2 = np.array(AV1)
    ar3 = np.array(A1[t])

    if np.all(ar <= ar1) and np.all(ar <= ar2):
        print(
            "\nAs the request made by " + y + " is less then its Need & Available, So we temporarily grant the resources")
        print("\n           New Available is : ")

        # Available = Available - Request
        ar2 = ar2 - ar
        ar2 = ar2.tolist()
        print(ar2)

        # Allocation = Allocation + Request
        ar3 = ar3 + ar
        ar3 = ar3.tolist()

        # Need= Need - Request
        ar1 = ar1 - ar

        ar1 = ar1.tolist()
        N1.pop(t)
        A1.pop(t)
        A1.insert(t, ar3)
        N1.insert(t, ar1)

        display(A1, N1, M1, P1)
        print("        Now checking if resources can be given to " + y + " or not: ")
        print()
        Y = safety(A1, N1, M1, P1, ar2)
        print("\n")
        if Y == 0:
            print("As we have a Safe Sequence for the request.")
            print("SYSTEM IS NOT IN DEADLOCK")


allocation = []
max = []
available = []
Resource = []
need = []
Process = []

n = int(input("Enter total number of Resource Types: "))

for i in range(n):
    t = "Enter the Name of Resource " + str(i + 1) + ": "
    x = input(t)
    Resource.append(x)

# Allocated Resources
print()

n = int(input("Enter the total number of Process: "))
print()

for i in range(n):
    p = "P" + str(i)
    Process.append(p)

print("ALLOCATED MATRIX DATA:\n")

for i in range(n):
    temp = []
    for resource in Resource:
        alloc_temp = "ALLOCATED Instances of Resource Type " + resource + " for " + Process[i] + ": "
        t = int(input(alloc_temp))
        temp.append(t)
    print()
    allocation.append(temp)

P = Process.copy()
P1 = Process.copy()
A = allocation.copy()
A1 = allocation.copy()
print()

# Maximum Resources
print("MAXIMUM MATRIX DATA:\n")
for i in range(n):
    temp = []
    for resource in Resource:
        max_temp = "MAXIMUM Instances of Resource Type " + resource + " required by " + Process[i] + ": "
        t = int(input(max_temp))
        temp.append(t)
    print()
    max.append(temp)
M = max.copy()
M1 = max.copy()

# Available Number of Resource
print("AVAILABLE MATRIX DATA:\n")
for resource in Resource:
    avail_temp = "AVAILABLE Instances of Resource Type " + resource + " in system: "
    t = int(input(avail_temp))
    available.append(t)

AV = available.copy()
AV1 = available.copy()

# Calculating Need

for i in range(n):
    a1 = np.array(allocation[i])
    a2 = np.array(max[i])
    t = a2 - a1
    t = t.tolist()

    y = []
    for i in t:
        if i >= 0:
            y.append(i)

    need.append(y)

N = need.copy()
N1 = need.copy()

print()
print("              CURRENT STATE OF THE SYSTEM: \n")

print("Process ID\t\tAllocated\t\t Maximum\t\t  Need")

for i in range(n):
    processFormat = Process[i].center(9)
    allocFormat = ' '.join([str(a) for a in allocation[i]]).center(9)
    maxFormat = ' '.join([str(a) for a in max[i]]).center(9)
    needFormat = ' '.join([str(a) for a in need[i]]).center(9)
    print(processFormat + "\t\t" + allocFormat + "\t\t" + maxFormat + "\t\t" + needFormat)
print()

print("         Initially Available Resources: " + str(AV))

# Determining Safe Sequence
print("\n")

# Safety Algorithm
safety(A, N, M, P, AV)

print("\n")

print("Press 1 if a Process wants to request for Resource.")
print("Press 2 to EXIT.")
choice = int(input("Enter the choice: "))

if choice == 1:
    # Resource request algorithm
    request(A1, N1, M1, P1, AV1)
elif choice == 2:
    print("Exiting...")
    exit(0)
else:
    print("ERROR: Invalid Choice!")