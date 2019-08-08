def takein(msg):
    try:
        txt = raw_input(msg)
    except NameError:
        txt = input(msg)
    return txt

while(1):
    addfile = takein("Enter *a* to add the file")
    if addfile=='a':
        filename = takein("Enter the complete name with extension of changed ")
        print ("enter y to add %s file" %(filename))
        if e == 'y':
            run_program("git add %s"%(filename))
        else:
            pass
    else:
        break

