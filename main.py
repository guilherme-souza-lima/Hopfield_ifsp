import numpy as np
from PIL import Image
import os
import re
import random
import time

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

#TREINAMENTO, CONFIGURAÇÃO INICIAL.
def hopfield(train_files, test_files,theta=0.5, time=1000, size=(100,100),threshold=60, current_path=None):

    #leia a imagem e converta-a em matriz Numpy
    print("Importando imagens e criando matriz de peso....")

    #num_files é o número de arquivos
    num_files = 0
    for path in train_files:
        print(path)
        x = readImg2array(file=path, size=size, threshold=threshold)
        x_vec = mat2vec(x)
        print(len(x_vec))
        if num_files == 0:
            # NA PRIMEIRA PASSADA ELE ENTRAR AQUI, CASO TENHO MAIS FOTO, CAI NO ELSE.
            # print("IF-num_files")
            w = create_W(x_vec)
            num_files = 1
        else:
            # ELSE
            # print("else-num_files")
            tmp_w = create_W(x_vec)
            w = w + tmp_w
            num_files += 1

    print("Matriz de peso está pronta")


    #Import test data
    counter = 0
    for path in test_files:
        y = readImg2array(file=path, size=size, threshold=threshold)
        oshape = y.shape
        # ISSO AQUI ABRE UMA MODAL COM A FOTO
        # y_img = array2img(y)
        # y_img.show()
        print("Dados de teste importados")

        y_vec = mat2vec(y)
        print("Atualizando")
        y_vec_after = update(w=w, y_vec=y_vec, theta=theta, time=time)
        y_vec_after = y_vec_after.reshape(oshape)
        if current_path is not None:
            x = random.randint(1, 99999)
            outfile = current_path+"/after_"+str(counter)+"_"+str(x)+".jpeg"
            array2img(y_vec_after, outFile=outfile)
        else:
            after_img = array2img(y_vec_after, outFile=None)
            # after_img.show()
        counter += 1

##INICIO DO CODIGO
def main():
    start_time = time.time()
    #SETO O CAMINHO DAS PASTA
    wayPathTest = "/test_pics/"
    wayPathTrain = "/train_pics/"

    current_path = os.getcwd()
    train_paths = []
    path = current_path+wayPathTrain
    for i in os.listdir(path):
        if re.match(r'[0-9a-zA-Z-]*.jp[e]*g', i):
            train_paths.append(path+i)

    test_paths = []
    path = current_path+wayPathTest
    for i in os.listdir(path):
        if re.match(r'[0-9a-zA-Z-_]*.jp[e]*g', i):
            test_paths.append(path+i)

    #A REDE HOPFIELD COMECA
    hopfield(train_files=train_paths, test_files=test_paths, theta=1.9, time=200000, size=(100, 100), threshold=70,current_path=current_path)
    # ALGUNS TESTES:
    # hopfield(train_files=train_paths, test_files=test_paths, theta=0.1, time=1000, size=(100, 100), threshold=70, current_path=current_path)
    # hopfield(train_files=train_paths, test_files=test_paths, theta=1.9, time=5000, size=(100, 100), threshold=70, current_path=current_path)

    #PRINT PARA SABER O TEMPO QUE LEVOU PARA EXECUTAR A APLICAÇÃO
    print("--- %s Segundos ---" % (time.time() - start_time))

main()
