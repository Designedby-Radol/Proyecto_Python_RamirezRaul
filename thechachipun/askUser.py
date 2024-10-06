from thechachipun.ui import util
from thechachipun.ui.messages import incorrectOption

def ask(msg):
    try:
        selected = int(input(msg))
        util.clear()
        return selected
    except:
        return None

def verify(selected, lastOption):
    # print(type(selected))
    # print(type(lastOption))
    # if selected in range(1, lastOption):
    #     selected = True
    # else:
    #     selected = False
    # print (selected)
    return selected if selected in range(1, lastOption+1) else None

def askAndVerify(askStruct):
    selected = verify(ask(askStruct['msg']), askStruct['lastOption'])
    print(selected)
    if selected:
        return selected
    else:
        print(incorrectOption)
        return None
