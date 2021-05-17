def get_name_list(model):
    return list(map(lambda c: c.name, model.objects.all()))