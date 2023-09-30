__all__ = (
    "TRUE",
    "FALSE",
    "NOT",
    "AND",
    "OR",
    "XOR",
    "_0",
    "_1",
    "_2",
    "_3",
    "_4",
    "_5",
    "_6",
    "_7",
    "_8",
    "_9",
    "_10",
    "INCERENTED",
    "PLUS",
    "MUL",
    "POW",
    "PAIR",
    "LEFT_OF",
    "RIGHT_OF",
    "REC",
    "VOID",
    "RUN",
    "DISCREMENTED",
    "MINUS",
    "IF",
    "IS_ZERO",
    "LE",
    "LT",
    "EQ",
    "DIV",
)


TRUE = lambda a: lambda b: a
FALSE = lambda a: lambda b: b


NOT = lambda a: a(FALSE)(TRUE)
AND = lambda a: lambda b: a(b)(FALSE)
OR = lambda a: lambda b: a(TRUE)(b)

XOR = lambda a: lambda b: AND(OR(a)(b))(OR(NOT(a))(NOT(b)))


_0 = lambda f: lambda v: v
_1 = lambda f: lambda v: f(v)
_2 = lambda f: lambda v: f(f(v))
_3 = lambda f: lambda v: f(f(f(v)))
_4 = lambda f: lambda v: f(f(f(f(v))))
_5 = lambda f: lambda v: f(f(f(f(f(v)))))
_6 = lambda f: lambda v: f(f(f(f(f(f(v))))))
_7 = lambda f: lambda v: f(f(f(f(f(f(f(v)))))))
_8 = lambda f: lambda v: f(f(f(f(f(f(f(f(v))))))))
_9 = lambda f: lambda v: f(f(f(f(f(f(f(f(f(v)))))))))
_10 = lambda f: lambda v: f(f(f(f(f(f(f(f(f(f(v))))))))))


INCERENTED = lambda n: lambda f: lambda v: f(n(f)(v))
PLUS = lambda a: lambda b: a(INCERENTED)(b)
MUL = lambda a: lambda b: lambda f: lambda v: a(b(f))(v)
POW = lambda a: lambda b: b(a)


PAIR = lambda a: lambda b: lambda k: k(a)(b)

LEFT_OF = lambda p: p(TRUE)
RIGHT_OF = lambda p: p(FALSE)


REC = lambda f: f(f)
VOID = REC(lambda void: lambda _: void(void))

RUN = lambda f: f(VOID)  # for laziness and avoiding `RecursionError`


DISCREMENTED = lambda n: lambda f: lambda v: RIGHT_OF(
    n(lambda p: PAIR(f(LEFT_OF(p)))(LEFT_OF(p)))(
        PAIR(v)(v)
    )
)
MINUS = lambda a: lambda b: b(DISCREMENTED)(a)


IF = lambda p: lambda a: lambda b: p(a)(b)
IS_ZERO = lambda n: n(lambda _: FALSE)(TRUE)

LE = lambda a: lambda b: IS_ZERO(MINUS(a)(b))
LT = lambda a: lambda b: LE(a)(DISCREMENTED(b))

EQ = lambda a: lambda b: AND(IS_ZERO(MINUS(a)(b)))(IS_ZERO(MINUS(b)(a)))

DIV = REC(lambda div: lambda a: lambda b: RUN(
    IF(LT(a)(b))(
        lambda _: _0
    )(
        lambda _: INCERENTED(div(div)(MINUS(a)(b))(b))
    )
))
