def interpret( command):
        """
        l=len(command)
        i=0
        r=""
        while i < l:
            if command[i] == "G":
                r = r + "G"
                i+=1
            else:
                if command[i] == "(" and command[i+1]==")":
                    r=r+"o"
                    i+=2
                else:
                    r=r+"al"
                    i+=4
        return r
        """
        return command.replace('()','o').replace('(al)','al')

s="G()(al)"
print(interpret(s))