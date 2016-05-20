from app.models import  Problem
import os.path
import subprocess

def compile_and_run(problem, userGeneratedResult):
    generateTestFile(problem, userGeneratedResult)
    try:
        output = subprocess.check_output(["raco", "test" , "test.rkt" ])
        removeTestFile()
        if(str(output).find("passed")):
            return ["passed",output]
        return ["failed",output]
    except:
        return ["failed","parse Error"]

def generateTestFile(problem, userGeneratedResult):
    preface = '#! /usr/bin/env racket \n#lang racket/base \n(require test-engine/racket-tests)\n'
    suffix = '\n(test)'
    expectedTest = problem.test_code
    if(expectedTest== ""):
        expectedTest= "(check-within "+ userGeneratedResult+" " + str(problem.evaluates_to)+ " 0.001)"
    #randgen for file name
    if os.path.isfile("test.rkt"):
        #file is in use sleep?
        removeTestFile()
    file = open("test.rkt", "w")
    file.write(preface)
    if (expectedTest == ""):
        expectedTest = "(check-within " + userGeneratedResult + " " + str(problem.evaluates_to) + " 0.001)"
        file.write(userGeneratedResult)
    file.write(expectedTest)
    file.write(suffix)
    file.close()

def removeTestFile():
    os.remove("test.rkt")
