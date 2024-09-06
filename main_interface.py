import tkinter as tk
######################################
def on_btn1_click():
  txt = entry.get()
  label.configure(text=txt, bg="pink")
  btn1.configure(text="Já clicou aqui", bg="red")
  btn2.configure(text="Já clicou aqui", bg="yellow")
  app.configure(bg="purple")

def on_btn2_click():
  label.configure(text="Clicou 2", bg="magenta")
  btn1.configure(text="Já clicou aqui", bg="cyan")
  btn2.configure(text="Já clicou aqui", bg="white")
  app.configure(bg="lightgreen")

#######################################
app = tk.Tk()
app.geometry("300x200")
app.configure(bg="lightblue")
####################################
label = tk.Label(app, text="UNICID", bg="yellow", width="20", height="2")
label.grid(column=0, row=0, pady=10)

entry = tk.Entry(app, width=30)
entry.grid(column=0, row=1, pady=10)

btn1 = tk.Button(app, text="Clique aqui", command=on_btn1_click, bg="green", width=20, height=2)
btn1.grid(column=0, row=2, padx=5, pady=10)

btn2 = tk.Button(app, text="Clique aqui este outro botão", command=on_btn2_click, bg="yellow", width=20, height=2)
btn2.grid(column=1, row=2, padx=5, pady=10)

#######################################
app.mainloop()