---
layout: default
title: 7. Modules
nav_order: 7
description: "How modules work in Aergia."
parent: "Syntax"
---

# 7. Modules

Modules are a great way to break up large projects into multiple smaller files. In Aergia, modules work by essentially running the imported file and putting all the variables and functions within the file into the global environment.

Modules also have a very special quality in Aergia: you can import Python modules directly.

## 7.1 Defining Modules
Modules can be defined by simply writing a file in Aergia. By importing said file, you can use values and functions from the file in another Aergia file.

## 7.2 Importing Modules
You can import modules with `+> "<filename.aer>"`.
```
# The following imports the file `math.aer`:
+> "math.aer"
```

To import Python modules, use `*> <module>` instead.
```
*> random
```

Note that importing a module puts all the variables and classes into the global namespace.