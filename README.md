# Aergias
The most minimal yet still usable programming language.

## Syntax
### Comments
Comment lines are denoted with `/`
```
/ This is a comment!
```
Comments have zero effect on the program whatsoever and can be used for notes or organization.

### Returning Values
To return a value, simply put the value.
```
/ Returns 1.2
1

/ Returns "Hello, world!"
"Hello, world!"
```
Note that this does not print anything to the console.

### Variables and Values
Variables are set to returned values with `=`.
```
/ Sets variable `num` to 3.2
=num 3.2

/ Sets variable `hello` to "World"
=hello "World"
```
Variables can also be returned.
```
/ Based on the codeblock above, this will return "World"
hello
```
Variables names can also be set after the first setting.
```
/ Sets variable `x` to 1, then 2
=x 1
=x 2
```

### Output and Input
Returned values can be outputted to the console with `>`.
```
/ Prints "Hello, world!"
>"Hello, world!"
```
String values can be inputted from the console with the following per type:
- `,` String
- `.` Integer
- `'` Float
```
/ Sets `name` to inputted string
=name ,

/ Sets `id` to inputted integer
=id .

/ Sets `userNum` to inputted float
=userNum '
```
This can be paired with output to make a generic input.
```
>"How old are you?"
=age .
```
