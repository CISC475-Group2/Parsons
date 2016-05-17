#from django.db import Problem
import os.path
import subprocess

def compile_and_run(problem, userGeneratedResult, expectedTest ):
    generateTestFile(problem, userGeneratedResult, expectedTest)
    output = subprocess.check_output(["raco", "test" , "test.rkt" ])
    removeTestFile()
    if(str(output).find("passed")):
        return ["passed",output]
    return ["failed",output]

def generateTestFile(problem, userGeneratedResult, expectedTest):
    preface = '#! /usr/bin/env racket \n#lang racket/base \n(require test-engine/racket-tests)\n'
    suffix = '\n(test)'
    #randgen for file name
    if os.path.isfile("test.rkt"):
        #file is in use sleep?
        return
    else:
        file = open("test.rkt", "w")
        file.write(preface)
        file.write(userGeneratedResult)
        file.write(expectedTest)
        file.write(suffix)
        file.close()

def removeTestFile():
    os.remove("test.rkt")
