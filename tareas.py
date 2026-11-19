tareas=[]

def agregar_tarea(titulo):
    if not titulo.strip():
        raise ValueError("El titulo no puede estar vacio")
    tareas.append(titulo.strip())

def listar_tareas():
    return tareas