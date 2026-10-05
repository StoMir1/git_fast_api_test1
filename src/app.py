from fastapi_offline import FastAPIOffline

app = FastAPIOffline()

mylist = [100, 200, 300]

@app.get('/home/')
def say_hello():
    return {'HELLO': 'WORLD'}

@app.get('/getItems/')
def get_items():
    return {'output' : mylist}

@app.get('/getLastItem/')
def get_last_item():
    if len(mylist) > 0:
        return {'output': mylist[-1]}
    else:
        return {'List is empty hehe.'}

@app.post('/addItem/{new_item}')
def insert_item(new_item:int):
    mylist.append(new_item)
    return {'new output': mylist}

@app.delete('/removeItem/{item_name}')
def remove_item(item:int):
    if item in mylist:
        mylist.remove(item)
        return {'list after remove': mylist}
    else:
        return {f'{item} Not Found in list'}

@app.delete('/removeIndex/')
def remove_item(index:int):
    if index >= 0 and index < len(mylist):
        r = mylist.pop(index)
        return {f'{r} deleted from list'}
    else:
        return {'index is wrong'}

@app.put('/updateItem_index/')
def update_item(index: int, new_item: int):
    if index >=0 and index < len(mylist):
        mylist[index] = new_item
        return {'updated list': mylist}
    else:
        return {f'{index} not exist in my list'}

@app.put('/updateItem/')
def update_item(item: int, new_item: int):
    if item in mylist:
        i = mylist.index(item)
        mylist[i] = new_item
        return {'updated list': mylist}
    else:
        return {f'{item} not found in list'}