import os
import re

def getPathTrain():
    return "/train_pics/"

def getPathTest():
    return "/test_pics/"

def trainPath(current_path, wayPathTrain = getPathTrain()):
    train_paths = []
    path = current_path + wayPathTrain
    for i in os.listdir(path):
        if re.match(r'[0-9a-zA-Z-]*.jp[e]*g', i):
            train_paths.append(path + i)
    return train_paths

def testPath(current_path, wayPathTest = getPathTest()):
    test_paths = []
    path = current_path + wayPathTest
    for i in os.listdir(path):
        if re.match(r'[0-9a-zA-Z-_]*.jp[e]*g', i):
            test_paths.append(path + i)
    return test_paths
