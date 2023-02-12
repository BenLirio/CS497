#lang racket

(define (zero-qbit) '(1 (1 0)))
(define (one-qbit) '(1 (0 1)))
(define (flatten x) (apply append x))

(define (map-2d f a b)
  (flatten (map (lambda (x) (map (lambda (y) (f x y)) b)) a))
)
(define (tensor-qbit a b)
  (let ([a-scale (car a)]
        [b-scale (car b)]
        [a-vals (cadr a)]
        [b-vals (cadr b)])
      (let
        ([scale (* a-scale b-scale)]
         [vals (map-2d * a-vals b-vals)])
        (list scale vals)
      )
))

(define (hadamard-2-1) '(
  (/ 1 (sqrt 2) (1 1 0 0))
  (/ 1 (sqrt 2) (1 (- 1) 0 0))
  (1 (0 0 1 0))
  (1 (0 0 0 1))
))

(define (apply-2-gate gate 2-qbits)
)

(display (tensor-qbit (zero-qbit) (one-qbit)))