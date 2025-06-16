import customtkinter as ctk
from CTkListbox import CTkListbox 

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("GoBike - Carrera de ciclismo")
app.geometry("800x500")

start = ctk.CTkInputDialog(text="Ingrese cantidad de participantes:", title="Inicio")
parts_total = int(start.get_input())

TIME_RECORD = "00:00:55"
time_average = None
number_win = None
time_best = float('inf')
time_win = None
time_sum = 0


def view_result():
    new_window = ctk.CTkToplevel(app)
    new_window.title("GoBike - Resultado de la carrera")
    new_window.geometry("360x220")
    new_window.resizable(width=False, height=False)

    label_win = ctk.CTkLabel(new_window, text="Ganador de la carrera", fg_color="gray30", corner_radius=6)
    label_win.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="we")

    win = ctk.StringVar()
    input_win = ctk.CTkEntry(new_window, state=ctk.DISABLED, textvariable=win)
    input_win.grid(row=1, column=0, padx=20, pady=20, sticky="we")
    win.set(f"Participante N{number_win}")
    
    label_record_now = ctk.CTkLabel(new_window, text="Actual record", fg_color="green", corner_radius=6)
    label_record_now.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="ew")

    record_now = ctk.StringVar()
    input_record_now = ctk.CTkEntry(new_window, textvariable=record_now)
    input_record_now.grid(row=1, column=1, padx=20, pady=20)
    record_now.set(time_win)

    label_average = ctk.CTkLabel(new_window, text="Promedio de la carrera", fg_color="gray30", corner_radius=6)
    label_average.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="ew")

    average = ctk.StringVar()
    input_average = ctk.CTkEntry(new_window, textvariable=average)
    input_average.grid(row=3, column=0, padx=20, pady=20)
    average.set(time_average)

    label_record_best = ctk.CTkLabel(new_window, text="Mejor record", fg_color="green", corner_radius=6)
    label_record_best.grid(row=2, column=1, padx=10, pady=(10, 0), sticky="ew")

    input_record_best = ctk.CTkEntry(new_window)
    input_record_best.grid(row=3, column=1, padx=20, pady=20)
    input_record_best.delete(0, ctk.END)
    input_record_best.insert(0, TIME_RECORD)

def calculate_average():
    time_seconda = time_sum / 1 if list_parts.size() == 0 else time_sum / list_parts.size()
    hour = time_seconda // 3600
    min = (time_seconda % 3600) // 60
    sec = (time_seconda % 3600) % 60
    global time_average
    time_average = f"{int(hour)}:{int(min)}:{int(sec)}"

def update_parts():
    parts_joined = list_parts.size() 
    label_parts.configure(text=f"Ingresaste {parts_joined} de {parts_total} participantes")
    if parts_joined == parts_total: calculate_average(), view_result()

def add_parts():
    number_part = input_number.get()
    time_part = f"{input_hour.get()}:{input_min.get()}:{input_min.get()}"
    time_second = (int(input_hour.get()) * 3600) + (int(input_min.get()) * 60) + int(input_min.get())
    global time_best
    if time_second < time_best:
        time_best = time_second
        global number_win
        number_win = number_part
        global time_win
        time_win = time_part
    global time_sum
    time_sum += time_second
    list_parts.insert(number_part, f"Participante {number_part} -- Tiempo {time_part}")
    update_parts()

def del_parts():
    elementc = list_parts.curselection()
    elementn = int(input_number.get())
    list_parts.delete(elementn-1 if elementc is None else elementc)
    update_parts()


label_number = ctk.CTkLabel(app, text="Numero de participante", fg_color="gray30", corner_radius=6)
label_number.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

input_number = ctk.CTkEntry(app, placeholder_text="01")
input_number.grid(row=1, column=0, padx=20, pady=20)

label_time = ctk.CTkLabel(app, text="Tiempo de participante", fg_color="gray30", corner_radius=6)
label_time.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="ew")

input_hour = ctk.CTkEntry(app, placeholder_text="hh")
input_hour.grid(row=3, column=0, padx=20, pady=20)

input_min = ctk.CTkEntry(app, placeholder_text="mm")
input_min.grid(row=3, column=1, padx=20, pady=20)

input_sec = ctk.CTkEntry(app, placeholder_text="ss")
input_sec.grid(row=3, column=2, padx=20, pady=20)

btn_agregar = ctk.CTkButton(app, text="Agregar", command=add_parts)
btn_agregar.grid(row=1, column=1, padx=20, pady=20)

btn_borrar = ctk.CTkButton(app, text="Borrar", command=del_parts)
btn_borrar.grid(row=1, column=2, padx=20, pady=20)

list_parts = CTkListbox(app)
list_parts.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

label_parts = ctk.CTkLabel(app, fg_color="green", corner_radius=6)
label_parts.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

parts_joined = list_parts.size() 
label_parts.configure(text=f"Ingresaste {parts_joined} de {parts_total} participantes")


app.mainloop()