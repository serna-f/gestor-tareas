# Evaluación

## Opción múltiple
1. ¿Qué comando mueve cambios al staging area?
b) git add
2. ¿Qué tipo de VCS es Git?
c) Distribuido
3. ¿Quién creó Git y en qué año?
b) Linus Torvalds, 2005
4. ¿Qué hace git fetch?
c) Descarga sin fusionar
5. Quieres deshacer un commit que ya subiste. ¿Qué usas?
b) git revert
6. ¿Qué es origin?
c) El nombre por defecto del remoto
7. ¿Qué es un fork?
a) Una copia del repo en tu cuenta de GitHub
8. Los marcadores <<<<<<<, =======, >>>>>>> indican… 
b) Un conflicto de fusión

## Preguntas abiertas
1. Explica con una analogía propia las tres áreas de Git.
R= Es como preparar una mochila para salir, el working directory es toda la ropa regada encima de tu cama mientras decides qué llevarte y qué doblar, el staging area es la pila de ropa ya doblada sobre la silla que sí va a entrar en el equipaje y el local repository es la maleta ya cerrada con candado y lista para guardarse o enviarse
2. ¿Cuándo usarías git stash?
R= Cuando tengo cambios a medias que aún no quiero guardar en un commit, pero necesito cambiar de rama o bajar cambios sin perder lo que llevo.
3. Encontraste un bug en una librería open source que usa tu sistema. Describe el flujo completo para enviar la corrección.
R= Lo clono, creo una rama, corrijo y pruebo yo mismo, guardo todo con commit, lo subo y mando un pull request.
4. Un compañero subió el .env con la contraseña de producción. ¿Por qué es grave y qué pasos sigues?
R= Es grave porque cualquiera ve la contraseña real del sistema, cambio la clave de inmediato, meto el .env al .gitignore, lo borro del historial y subo todo limpio.
5. Un deploy de ayer rompió producción y el commit ya está en main. ¿Usas reset o revert? ¿Por qué?
R= Uso revert porque deshace el commit con un commit nuevo sin borrar el historial de main ni causar conflictos al equipo.

## Ejercicio de diagnostico
Ordena correctamente esta secuencia para publicar un cambio nuevo:
git pull -> git switch -c feat/x -> Editar archivos -> git add -> git commit -m -> git push