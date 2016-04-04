from brabbel import Expression


class foo():
    def __init__(self, id, role):
        self.id = id
        self.role=role

policies = {}

def new_policy(name, text, test_values=None):
    expr = Expression(text)
    if test_values:
        if not expr.evaluate(test_values):
            raise Exception
    policies[name] = expr

def evaluate(name, values):
    return policies[name].evaluate(values)

new_policy("is admin", "$a.role in ['admin']", {"a":foo(2,"admin")})
new_policy("is the same", "$a.id == $b.id")

print evaluate("is admin", {"a":foo(2, "admin")})
print evaluate("is the same", {"a":foo(2, "admin"), "b":foo(2, "author")})

