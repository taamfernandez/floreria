def eliminar(id):
        id = Flor.objects.get(id=id)
        flores.delete()


