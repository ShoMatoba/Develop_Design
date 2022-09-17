def execute_param_fn(args,hosei,fn):
    return fn(args,hosei)

if __name__ == "__main__":
    execute_param_fn([1,2,3],4,(lambda x,y:max(x)+y))
    execute_param_fn([1,2,3],4,(lambda x,y:min(x)-y))
    