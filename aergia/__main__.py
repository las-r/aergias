import sys
from .lexer import tokenize
from .parser import parse

# aergia main
# made by las-r on github

def main():
    # arguments
    if len(sys.argv) < 2:
        print("Usage: aergia <filename.aer>")
        return
    filename = sys.argv[1]
    
    # read file
    with open(filename, "r") as f:
        code = f.read()

    # interpret
    try:
        tokens = tokenize(code)
        ast = parse(tokens)
        env = {}
        for node in ast:
            if node:
                node.eval(env)
    except Exception as e:
        print(f"Aergia Error: {e}")

if __name__ == "__main__":
    main()