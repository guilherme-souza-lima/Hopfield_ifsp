import helper as func

#TREINAMENTO, CONFIGURAÇÃO INICIAL.
def hopfield(train_files, test_files,theta=0.5, time=1000, size=(100,100),threshold=60, current_path=None):

    #leia a imagem e converta-a em matriz Numpy
    print("Importando imagens e criando matriz de peso....")

    #num_files é o número de arquivos
    num_files = 0
    for path in train_files:
        print(path)
        x = func.readImg2array(file=path, size=size, threshold=threshold)
        x_vec = func.mat2vec(x)
        print(len(x_vec))
        if num_files == 0:
            w = func.create_W(x_vec)
            num_files = 1
        else:
            tmp_w = func.create_W(x_vec)
            w = w + tmp_w
            num_files += 1

    print("Matriz de peso está pronta")


    #Import test data
    counter = 0
    for path in test_files:
        y = func.readImg2array(file=path, size=size, threshold=threshold)
        oshape = y.shape
        print("Dados de teste importados")

        y_vec = func.mat2vec(y)
        print("Atualizando")
        y_vec_after = func.update(w=w, y_vec=y_vec, theta=theta, time=time)
        y_vec_after = y_vec_after.reshape(oshape)
        if current_path is not None:
            outfile = current_path+"/after_"+str(counter)+"_"+str(func.nameFileNow())+".jpeg"
            func.array2img(y_vec_after, outFile=outfile)
        else:
            after_img = func.array2img(y_vec_after, outFile=None)
        counter += 1
