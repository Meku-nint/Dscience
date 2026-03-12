# match statement is like switch statement in other languages, but more powerful and flexible.b/c it can match complex patterns, not just simple values.
def http_error(status):
    match status:
        case 400 | 500:
            return "Bad request"
        case 400:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
print(http_error(400)) # this will print "Bad request"