tareas=[]

def agregar_tarea(titulo):
    if not titulo.strip():
        raise ValueError("El titulo no puede estar vacio")
    tareas.append(titulo.strip())

def listar_tareas():
    return tareas

def eliminar_tarea(indice):
    return tareas.pop(indice)

def tareas_priotitarias(prefijo="!"):
    return [t for t in tareas if t.startswitch(prefijo)]