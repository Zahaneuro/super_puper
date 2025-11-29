from customtkinter import*

app = CTk()
app.geometry('400x500')
app.title('carculator')

#я хз що мож зробити

result_text = ''
def click(s):
    global result_text
    if s == '=':
        r = result.get()
        result.delete(0,'end')
        result.insert(0, f'{eval(r)}')
    elif s =='c':
        result.delete(0,'end')
        result_text= ''
    else:
        result_text += s
        result.delete(0,'end')
        result.insert(0, result_text)


layout = CTkFrame(app)

symb = ['7','8','9','=','4','5','6','+','1','2','3','-','0',',','/','*']
i = 0
for row in range(4):
    for column in range(4):
        btn = CTkButton(layout, text= symb[i], width=90, height=90, command=lambda s=symb[i]: click(s))
        btn.grid(row=row,column=column, pady=5, padx=5)
        i += 1
    
result = CTkEntry(app,height=50)
clear = CTkButton(app, text='С', height=50, command=lambda s='c':click(s))

result.pack(fill='x')
layout.pack()
clear.pack(fill='x')


app.mainloop()
