# The module that contains the messages in English and Spanish

english_messages = {
    "creating_ext_dir": "Creating sub-directory \"Extracted\"...",
    "ext_dir_already_exists": "The sub-directory \"Extracted\" already \
exists, use it instead? [y/N (abort)]",
    "removing_files_in_path": "Removing all files in %s...",
    "remove_i?": "Remove %s? [Y/n] ",
    "i_not_removed": "%s will not be removed.",
    "removing_i": "Removing %s...",
    "exception_occurred": "An exception occurred.\nException Details: %s",
    "done_msg": "Done.",
    "finished_msg": "Finished.",
    "list_of_files_removed_in_path": "List of files removed in %s:\n",
    "no_args_were_given": "No arguments were given.\nUse -h for details.",
    "missing_arg": "Missing argument: keyword\nUse -h for details.",
    "dir_does_not_exist": "The directory %s does not exist.",
    "keyword_cant_have_chars": "The keyword cannot have the \"/\" or \"\\\" \
characters.",
    "help_msg": """
Remove the files inside a directory that have the specified
keyword in their name, version 0.8
Usage:
CLI> python3 RemoveFiles.py [arguments] [keyword] [directory]

Some arguments can also have sub-arguments. For example:
CLI> python3 RemoveFiles.py -e /my/dir -da hello /foo/bar
                            ^     ^
Could be interpreted as: extract here

If your directory has spaces, use quotes:
\"/dire c/tory w/ith s/pa ces/\"

Unrecognized arguments will be ignored.
Whenever you are asked for confirmation, the uppercase letter
is the value that will be used if you don't input anything.

Arguments/Options:

-h (help)       Get information about the program.

-e (extract)    Copy the given directory and its files
                into a sub-directory and manipulate the
                files inside of it.
                Optional: If an existing directory is
                specified after the argument, use it
                instead of creating a sub-directory.

-k (keep)       Instead of removing the files, keep them
                and remove the ones that don't have the
                keyword in their name.

-v (verbose)    Print the action being done.

-da (don't ask) Don't ask before deleting a file.

-r (recursive)  Also manipulate the files inside
                sub-directories.

-ncs (no case sensitive) Ignore all uppercase letters,
                    including the ones in the keyword.

-l (log)        Write the list of removed files to a
                TXT file in the same directory where
                the script is located.
                Optional: If an existing directory is
                specified after the argument, write the
                log to it instead of using the
                directory where the script is located.
"""
    }

spanish_messages = {
    "creating_ext_dir": "Creando sub-directorio \"Extracted\"...",
    "ext_dir_already_exists": "El sub-directorio \"Extracted\" ya existe, \
usarlo en cambio? [y (sí)/N (abortar)]",
    "removing_files_in_path": "Removiendo todos los archivos en %s...",
    "remove_i?": "Remover %s? [Y (sí)/n (no)]",
    "i_not_removed": "%s no será removido.",
    "removing_i": "Removiendo %s...",
    "exception_occured": "Una excepción ocurrió.\nDetalles: %s",
    "done_msg": "Hecho.",
    "finished_msg": "Terminado.",
    "list_of_files_removed_in_path": "Lista de archivos removidos en %s:\n",
    "no_args_were_given": "No hay argumentos.\nUse -h para más detalles.",
    "missing_arg": "Argumento Faltante: palabra clave\nUse -h para más \
detalles.",
    "dir_does_not_exist": "El directorio %s no existe.",
    "keyword_cant_have_chars": "La palabra clave no puede contener los \
caracteres \"/\" o \"\\\".",
    "help_msg": """
Remueve los archivos dentro de un directorio si tienen la palabra clave
especificada en su nombre, versión 0.8
Uso:
CLI> python3 RemoveFiles.py [argumentos] [palabra clave] [directorio]

Algunos argumentos también pueden tener sub-argumentos. Por ejemplo:
CLI> python3 RemoveFiles.py -e /mi/dir -da hola /foo/bar
                            ^     ^
Se puede interpretar como: extrae aquí

Si tu directorio tiene espacios, use comillas:
\"/dire c/torio c/on es/pa cios/\"

Los argumentos no identificados serán ignorados.
Cuando se quiera confirmar algo con usted, el valor en mayúscula es el
valor que será usado si es que no da una respuesta.

Argumentos/Opciones:

-h (ayuda)      Obtener información sobre el programa.

-e (extraer)    Copiar el directorio dado y sus archivos a
                un sub-directorio y manipular los archivos
                dentro de este.
                Opcional: Si un directorio existente es
                especificado después del argumento, usarlo
                en vez de crear un sub-directorio.

-k (conservar)  En vez de remover los archivos, conservarlos
                y remover los que no tienen la palabra clave
                en su nombre.

-v (verboso)    Imprime la acción que esté llevando a cabo.

-da (no preguntar) No preguntar antes de remover un archivo.

-r (recursivo)  También manipular los archivos dentro de
                sub-directorios.

-ncs (no distinguir entre mayúsculas y minúsculas) Ignorar
                todas las letras mayúsculas, incluyendo las
                que estén en la palabra clave.

-l (log)        Escribir la lista de archivos removidos a
                un archivo TXT en el mismo directorio
                donde se encuentra el script.
                Opcional: Si un directorio existente es
                especificado después del argumento, escribe
                el archivo en él en vez de usar el mismo
                directorio donde se encuentra el script.
"""
    }

