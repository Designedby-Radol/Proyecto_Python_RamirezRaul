from thechachipun.ui import util
from thechachipun.ui.messages import incorrectOption

def ask(msg):
    try:
        selected = input(msg)
        util.clear()
        return selected
    except:
        return None

def verify(selected, lastOption):
    return selected if selected in range(1, lastOption) else None

def askAndVerify(askStruct):
    selected = verify(ask(askStruct['msg']), askStruct['lastOption'])
    if selected:
        return selected
    else:
        print(incorrectOption)
        return None
