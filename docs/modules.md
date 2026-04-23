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
Modules can be defined by simply writing a file in Aergia. By importing said file, you can use values and functions from the file in another Aergia file. Note that **importing an Aergia module puts all the variables and classes into the global namespace.**

## 7.2 Importing Modules
You can import modules with `+> "<filename.aer>"`.
```
# The following imports the file `math.aer`:
+> "math.aer"
```

To import Python modules, use `*< <module>` or`*> <module>` instead.

`*>` will add all the values directly as is within the module into the global namespace, while `*<` will insert the module name at the beginning of them. (e.g. `*< math` -> `math_sqrt`)

Any classes will be flattened, with where dots would be there would be underscores (e.g. `pyray_KeyboardKey.KEY_SPACE` -> `pyray_KeyboardKey_KEY_SPACE`).
```
*> random
*< math

# Use the randint function directly
> @randint:1 100:

# Use the sqrt function with the module name inserted
> @math_sqrt:2:
```

Generally, using `*<` is recommended over `*>` to keep the global namespace clean. Note that Aergia modules do not have this functionality and will always be as is in the global namespace when imported.