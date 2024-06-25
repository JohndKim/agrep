from .re_to_nfa import re_to_nfa
from .nfa_path import match

def grep_func(w, regex):
    # convert regex --> regular operations --> nfa
    nfa = re_to_nfa(regex)  

    accept, path = match(nfa, w)
    if accept: return True, nfa, path
    return False, nfa, None
    

def main():
    pass
    # args = sys.argv
    # if len(args) != 2:
    #     print("Usage: agrep 'regexp'")
    #     return
    
    # # accept, nfa = re_to_nfa(args[1])
    # # if not accept: return
    
    # nfa = re_to_nfa(args[1])  
    
    # # print("nfa")
    # # print(nfa)
      
    # for line in sys.stdin:
    #     w = line.rstrip('\n')
    #     accept, path = match(nfa, w)
    #     if accept: print(w)
    

if __name__ == "__main__":
    main()