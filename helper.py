from PIL import Image
import numpy as np
import time
import random
import datetime

#converter matriz em vetor
def mat2vec(x):
    m = x.shape[0]*x.shape[1]
    tmp1 = np.zeros(m)

    c = 0
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            tmp1[c] = x[i, j]
            c += 1
    return tmp1

#Criar matriz de peso para uma única imagem
def create_W(x):
    #START TIME PARA SABER O TEMPO DO APRENDIZADO
    start_time_create_w = time.time()
    if len(x.shape) != 1:
        print("A entrada não é vetorial")
        return
    else:
        w = np.zeros([len(x), len(x)])
        for i in range(len(x)):
            for j in range(i, len(x)):
                if i == j:
                    w[i, j] = 0
                else:
                    w[i, j] = x[i]*x[j]
                    w[j, i] = w[i, j]
    #PRINTA O TEMPO
    print("--- %s Segundos IA ---" % (time.time() - start_time_create_w))
    return w

#Leia o arquivo de imagem e converta-o em matriz Numpy
def readImg2array(file, size, threshold=145):
    pilIN = Image.open(file).convert(mode="L")
    pilIN = pilIN.resize(size)
    #pilIN.thumbnail(size,Image.ANTIALIAS)
    imgArray = np.asarray(pilIN, dtype=np.uint8)
    x = np.zeros(imgArray.shape, dtype=np.float)
    x[imgArray > threshold] = 1
    x[x == 0] = -1
    return x

#Converter matriz Numpy para arquivo de imagem como Jpeg
def array2img(data, outFile = None):
    #data is 1 or -1 matrix
    y = np.zeros(data.shape, dtype=np.uint8)
    y[data == 1] = 255
    y[data == -1] = 0
    img = Image.fromarray(y, mode="L")
    if outFile is not None:
        img.save(outFile)
    return img

#Update
def update(w, y_vec, theta=0.5, time=100):
    for s in range(time):
        m = len(y_vec)
        i = random.randint(0, m-1)
        u = np.dot(w[i][:], y_vec) - theta

        if u > 0:
            y_vec[i] = 1
        elif u < 0:
            y_vec[i] = -1

    return y_vec

def nameFileNow():
    hoje = datetime.datetime.now()
    dt_string = hoje.strftime("%d/%m/%Y %H:%M:%S")
    return str(dt_string).replace(" ", "_").replace(":", "_").replace(".", "_").replace("/", "_")
