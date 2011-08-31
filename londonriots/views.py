def view_root(context, request):
    return {'items':list(context), 'project':'londonriots'}

def view_model(context, request):
    return {'item':context, 'project':'londonriots'}
