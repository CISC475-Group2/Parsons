#! /usr/bin/env racket
#lang racket/base
(require test-engine/racket-tests)

(define ( car-distance t)
 (* (/ 44 2.8) (* t t))) 

(check-within (* 0 0) 0 0.001)
(test)
