import ast

c = compile(ast.parse("print 1", "t.py", "exec"), "u.py", "exec")
print c.co_filename
exec c

try:
    c = compile(ast.parse("print 1", "t.py", "exec"), "u.py", "eval")
except Exception as e:
    print e

c = compile(ast.parse("print 2", "t.py", "exec"), "u.py", "exec")
print eval(c)

