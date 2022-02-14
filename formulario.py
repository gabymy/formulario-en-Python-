from tkinter import *
import xlrd


def send_data():
    asociado_data=asociado.get()
    cuit_data=cuit.get()
    domicilio_data=domicilio.get()
    periodo_data=periodo.get()
    monto_data=monto.get()
    eleccion_data=eleccion.get()

    print(asociado_data,"\n", cuit_data, "\n",domicilio_data,"\n", periodo_data, "\n", monto_data, "\n", eleccion_data)


    newfile = open("registro.txt", "w")
    newfile.write(asociado_data)
    newfile.write("\n")
    newfile.write(cuit_data)
    newfile.write("\n")
    newfile.write(domicilio_data)
    newfile.write("\n")
    newfile.write(periodo_data)
    newfile.write("\n") 
    newfile.write(monto_data)
    newfile.write("\n") 
    newfile.write(eleccion_data)
    newfile.write("\n") 
    newfile.close()
    print("new user registered. Usename: {} | fullname: {} ".format(asociado_data, cuit_data ))

    asociado_entry.delete(0, END)
    cuit_entry.delete(0, END)
    domicilio_entry.delete(0, END)
    periodo_entry.delete(0, END)
    monto_entry.delete(0, END)
    eleccion_entry.delete(0, END)


mywindow = Tk()
mywindow.geometry("650x550")
mywindow.title("Anticipo de Retorno")
mywindow.resizable(0,0)
mywindow.config(background="#213141")
main_title=Label(text="Cooperativa de Trabajo POLILU Ltda.",bd=5, font=("Curier",18),bg="#56CD63",fg="white",width="550",height="2")
main_title.pack()

asociado_label=Label(text="Apellido y Nombre", bg="#FFEEDD", font=("Curier 12 bold"))
asociado_label.place(x=22, y=70)
cuit_label=Label(text="C.U.I.T", bg="#FFEEDD",font=("Curier 12 bold") )
cuit_label.place(x=22, y=130)
domicilio_label=Label(text="Domicilio", bg="#FFEEDD", font=("Curier 12 bold"))
domicilio_label.place(x=22, y=190)
periodo_label=Label(text="Periodo a Liquidar", bg="#FFEEDD",font=("Curier 12 bold") )
periodo_label.place(x=22, y=250)
monto_label=Label(text="Monto en $",bg="#FFEEDD",font=("Curier 12 bold") )
monto_label.place(x=22, y=310)
eleccion_label=Label(text="Forma de pago", bg="#FFEEDD",font=("Curier 12 bold") )
eleccion_label.place(x=22, y=370)

asociado=StringVar()
cuit=StringVar()
domicilio=StringVar()
periodo=StringVar()
monto=StringVar()
eleccion=StringVar()

asociado_entry=Entry(textvariable=asociado, width="50")
cuit_entry=Entry(textvariable=cuit, width="50")
domicilio_entry=Entry(textvariable=domicilio, width="50")
periodo_entry=Entry(textvariable=periodo, width="40")
monto_entry=Entry(textvariable=monto, width="50")
eleccion_entry=Entry(textvariable=eleccion, width="50")

asociado_entry.place(x=22, y=100)
cuit_entry.place(x=22, y=160)
domicilio_entry.place(x=22, y=220)
periodo_entry.place(x=22, y=280)
monto_entry.place(x=22, y=340)
eleccion_entry.place(x=22, y=400)

submit_btn=Button(mywindow,text="EXPORTAR",bd=6,font=("Curier 11 bold"), command=send_data,width="30",height="2",bg="#00CD63")
submit_btn.place(x=22,y=450)












mywindow.mainloop()
