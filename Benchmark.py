import matplotlib.pyplot as pt
import subprocess
from tqdm import tqdm
mode = 1
counter = 0
x = []
y = []
x1 = []
y1 = []

def Plot(x,y):
    if mode <= 2:


        pt.plot(x, y, label = "int")
        pt.plot(x1, y1, label = "byte")
        pt.title("byte vs int")
    if mode > 2:
        pt.plot(x, y, label="int")
        pt.plot(x1, y1, label="short")
        pt.title("short vs int")
    pt.xlabel("Länge des Array")
    pt.ylabel("verwendeter Speicherplatz")
    pt.legend()
    pt.show()

def dataCreateX(ret):
    ret = str(ret).split(":")[1].split(" ")
    ret = int(ret[1])
    return(ret)

def getData(n,c, mode):
    if mode == 1:
        mode1 = "Byte_Vs_Int\ByteInt.jar"
    if mode == 2:
        mode1 = "Byte_Vs_Int\Byte.jar"
    if mode == 3:
        mode1 = "Short_Vs_Int\ShortInt.jar"
    if mode == 4:
        mode1 = "Short_Vs_Int\Short.jar"
    ges = 0
    for s in range (10):
        process = subprocess.Popen("java -jar {} {}".format(mode1,str(n)), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ret = process.stdout.read() + process.stderr.read()
        ges = ges + dataCreateX(ret)
    if mode == 1 or mode == 3:
        x.append(n)
        y.append(int(ges/10))
    else:
        x1.append(n)
        y1.append(int(ges / 10))
    save(c, y, mode)
    #print(c)


def save(x,y, mode):
    if mode == 1:
        save = "Byte_Vs_Int\ByteInt.sv"
    if mode == 2:
        save = "Byte_Vs_Int\Byte.sv"
    if mode == 3:
        save = "Short_Vs_Int\ShortInt.sv"
    if mode == 4:
        save = "Short_Vs_Int\Short.sv"

    with open("{}".format(save), "a") as file:
        file.write("n: {} y:{}".format(x,y[x]) + "\n")


def dataCorrection(counter):
    for i in range(counter):
        y[i] = y[i] - y[0]
        y1[i] = y1[i] - y1[0]

def start(mode, counter):
    for i in tqdm(range(3  )):
        getData(i*10000, i, mode)
    if mode %2 == 0:
        dataCorrection(i)
        Plot(x, y)
    else:
        mode = mode + 1
        start(mode,i)


start(mode, counter)