---
layout: default
title: 9. Examples
nav_order: 9
description: "Aergia syntax examples."
parent: "Syntax"
---

# 9. Examples
This section has a few examples of how the Aergia language can be used.

## 9.1 Hello World
```
> "Hello, world!"
```

## 9.2 Fibonacci Sequence

```
> "How many numbers?"
= limit .
= n1 0
= n2 1
= i 0

[ << i limit
    > n1
    = temp + n1 n2
    = n1 n2
    = n2 temp
    = i + i 1
]
```

## 9.3 Factorial
```
{ factorial : n :
    ( <= n 1
        ? 1
    )
    ? * n @ factorial : - n 1 :
}

> "Enter n for n!:"
> @ factorial : . :
```