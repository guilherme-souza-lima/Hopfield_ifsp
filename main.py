import os
import time
import hopfield
import settings
import config

##INICIO DO CODIGO
def main():
    start_time = time.time()
    current_path = os.getcwd()
    train_paths = settings.trainPath(current_path)
    test_paths = settings.testPath(current_path)

    #A REDE HOPFIELD COMECA
    hopfield.hopfield(train_files=train_paths, test_files=test_paths, theta=config.THETA, time=config.TIME, size=(100, 100), threshold=config.THESHOLD, current_path=current_path)

    #PRINT PARA SABER O TEMPO QUE LEVOU PARA EXECUTAR A APLICAÇÃO
    print("--- %s Segundos ---" % (time.time() - start_time))

main()
