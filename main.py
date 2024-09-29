import tkinter as tk
from tkinter import messagebox

# Función para añadir una nueva tarea a la lista
def add_task(event=None):
    task = entry_task.get()  # Obtener el texto de la entrada
    if task:  # Verificar que no esté vacío
        listbox_tasks.insert(tk.END, task)  # Añadir tarea a la lista
        entry_task.delete(0, tk.END)  # Limpiar el campo de entrada
    else:
        messagebox.showwarning("Entrada vacía", "Debes escribir una tarea antes de añadirla.")

# Función para marcar la tarea seleccionada como completada
def complete_task():
    try:
        task_index = listbox_tasks.curselection()[0]  # Obtener el índice de la tarea seleccionada
        task_text = listbox_tasks.get(task_index)  # Obtener el texto de la tarea
        listbox_tasks.delete(task_index)  # Eliminar la tarea de la lista
        listbox_tasks.insert(tk.END, f"{task_text} - Completada")  # Añadirla de nuevo con "Completada"
    except IndexError:
        messagebox.showwarning("Selección requerida", "Debes seleccionar una tarea para marcarla como completada.")

# Función para eliminar la tarea seleccionada
def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]  # Obtener el índice de la tarea seleccionada
        listbox_tasks.delete(task_index)  # Eliminar la tarea de la lista
    except IndexError:
        messagebox.showwarning("Selección requerida", "Debes seleccionar una tarea para eliminarla.")

# Crear la ventana principal
window = tk.Tk()
window.title("Lista de Tareas")

# Crear un campo de entrada para añadir nuevas tareas
entry_task = tk.Entry(window, width=35)
entry_task.pack(pady=10)

# Añadir manejador de evento para añadir tarea al presionar 'Enter'
entry_task.bind("<Return>", add_task)

# Crear el botón para añadir una tarea
button_add_task = tk.Button(window, text="Añadir Tarea", width=20, command=add_task)
button_add_task.pack(pady=5)

# Crear la lista de tareas
listbox_tasks = tk.Listbox(window, width=50, height=10)
listbox_tasks.pack(pady=10)

# Crear el botón para marcar como completada
button_complete_task = tk.Button(window, text="Marcar como Completada", width=20, command=complete_task)
button_complete_task.pack(pady=5)

# Crear el botón para eliminar una tarea
button_delete_task = tk.Button(window, text="Eliminar Tarea", width=20, command=delete_task)
button_delete_task.pack(pady=5)

# Ejecutar la aplicación
window.mainloop()