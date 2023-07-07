from tkinter import *
import pickle

root = Tk()
root.title("CC Fraud Detection")
root.geometry("1100x400")


def entry_fields():
    v1=float(e1.get())
    v2=float(e2.get())
    v3=float(e3.get())
    v4=float(e4.get())
    v5=float(e5.get())
    v6=float(e6.get())
    v7=float(e7.get())
    v8=float(e8.get())
    v9=float(e9.get())
    v10=float(e10.get())
    v11=float(e11.get())
    v12=float(e12.get())
    v13=float(e13.get())
    v14=float(e14.get())
    v15=float(e15.get())
    v16=float(e16.get())
    v17=float(e17.get())
    v18=float(e18.get())
    v19=float(e19.get())
    v20=float(e20.get())
    v21=float(e21.get())
    v22=float(e22.get())
    v23=float(e23.get())
    v24=float(e24.get())
    v25=float(e25.get())
    v26=float(e26.get())
    v27=float(e27.get())
    v28=float(e28.get())
    v29=float(e29.get())


###  loading the pickle model
    
    model = pickle.load('CC Fraud Detection.pickle')
    y_pred = model.pred([list])


    list = [v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v25,v27,v28,v29]

### Result
    result = []

    if y_pred==0:
        result.append("Normal Transaction")
    else:
        result.append("Fraud Transaction")


    print("*** [",result,"] ***")


    Label(root,text="Final Prediction")
    Label(root,text=result).grid(row=32)


label = Label(root,text="CC Fraud Detection System",bg='black',fg='white',width=30).grid(row=10,column=3)

### For Entering the Data
Label(root,text="Enter value of v1").grid(row=1,column=0)
Label(root,text="Enter value of v2").grid(row=2,column=0)
Label(root,text="Enter value of v3").grid(row=3,column=0)
Label(root,text="Enter value of v4").grid(row=4,column=0)
Label(root,text="Enter value of v5").grid(row=5,column=0)
Label(root,text="Enter value of v6").grid(row=6,column=0)
Label(root,text="Enter value of v7").grid(row=7,column=0)

Label(root,text="Enter value of v8").grid(row=1,column=2)
Label(root,text="Enter value of v9").grid(row=2,column=2)
Label(root,text="Enter value of v10").grid(row=3,column=2)
Label(root,text="Enter value of v11").grid(row=4,column=2)
Label(root,text="Enter value of v12").grid(row=5,column=2)
Label(root,text="Enter value of v13").grid(row=6,column=2)
Label(root,text="Enter value of v14").grid(row=7,column=2)

Label(root,text="Enter value of v15").grid(row=1,column=4)
Label(root,text="Enter value of v16").grid(row=2,column=4)
Label(root,text="Enter value of v17").grid(row=3,column=4)
Label(root,text="Enter value of v18").grid(row=4,column=4)
Label(root,text="Enter value of v19").grid(row=5,column=4)
Label(root,text="Enter value of v20").grid(row=6,column=4)
Label(root,text="Enter value of v21").grid(row=7,column=4)

Label(root,text="Enter value of v22").grid(row=1,column=6)
Label(root,text="Enter value of v23").grid(row=2,column=6)
Label(root,text="Enter value of v24").grid(row=3,column=6)
Label(root,text="Enter value of v25").grid(row=4,column=6)
Label(root,text="Enter value of v26").grid(row=5,column=6)
Label(root,text="Enter value of v27").grid(row=6,column=6)
Label(root,text="Enter value of v28").grid(row=7,column=6)
Label(root,text="Enter value of v29").grid(row=8,column=6)



e1 = Entry(root)
e1.grid(row=1,column=1)
e2 = Entry(root)
e2.grid(row=2,column=1)
e3 = Entry(root)
e3.grid(row=3,column=1)
e4 = Entry(root)
e4.grid(row=4,column=1)
e5 = Entry(root)
e5.grid(row=5,column=1)
e6 = Entry(root)
e6.grid(row=6,column=1)
e7 = Entry(root)
e7.grid(row=7,column=1)
e8 = Entry(root)
e8.grid(row=1,column=3)
e9 = Entry(root)
e9.grid(row=2,column=3)
e10 = Entry(root)
e10.grid(row=3,column=3)
e11 = Entry(root)
e11.grid(row=4,column=3)
e12 = Entry(root)
e12.grid(row=5,column=3)
e13 = Entry(root)
e13.grid(row=6,column=3)
e14 = Entry(root)
e14.grid(row=7,column=3)
e15 = Entry(root)
e15.grid(row=1,column=5)
e16 = Entry(root)
e16.grid(row=2,column=5)
e17 = Entry(root)
e17.grid(row=3,column=5)
e18 = Entry(root)
e18.grid(row=4,column=5)
e19 = Entry(root)
e19.grid(row=5,column=5)
e20 = Entry(root)
e20.grid(row=6,column=5)
e21 = Entry(root)
e21.grid(row=7,column=5)
e22 = Entry(root)
e22.grid(row=1,column=7)
e23 = Entry(root)
e23.grid(row=2,column=7)
e24 = Entry(root)
e24.grid(row=3,column=7)
e25 = Entry(root)
e25.grid(row=4,column=7)
e26 = Entry(root)
e26.grid(row=5,column=7)
e27 = Entry(root)
e27.grid(row=6,column=7)
e28 = Entry(root)
e28.grid(row=7,column=7)
e29 = Entry(root)
e29.grid(row=8,column=7)


Button(root,text="Predict",command=entry_fields).grid(row=10,column=4)


mainloop()