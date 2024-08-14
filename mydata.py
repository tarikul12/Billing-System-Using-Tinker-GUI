import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
from tkinter import ttk,HORIZONTAL, VERTICAL,BOTTOM,X,Y,END

class PharmacyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1900x800+0+0") 
        
        # Define StringVars for entry widgets
        self.refMed = tk.StringVar()
        self.addMed = tk.StringVar()
        #+++++++++++++++++++++++++++++++++++++++++++ Main table variable  ++++++++++++++++++++++++
        self.refNo = tk.StringVar()
        self.compName = tk.StringVar()
        self.typeName = tk.StringVar()
        self.medName = tk.StringVar()
        self.lotNo = tk.StringVar()
        self.issDate = tk.StringVar()
        self.expDate = tk.StringVar()
        self.uses = tk.StringVar()
        self.sideEffect = tk.StringVar()
        self.waring = tk.StringVar()
        self.dosage = tk.StringVar()
        self.price = tk.StringVar()
        self.proQt = tk.StringVar()
        
        
        
        
        #+++++++++++++++++++++++++++++++++++++++++++ Left Side ++++++++++++++++++++++++
        
         # Title label using grid instead of pack
        #lbltitle = tk.Label(self.root, text="PHARMACY MANAGEMENT SYSTEM", bd=15, relief=tk.RIDGE, bg="White",
                           # fg="darkgreen", font=("times new roman", 50, "bold"), padx=2, pady=4)
        #lbltitle.place(x=0, y=0, width=800)
        
        conn = mysql.connector.connect(host='localhost', username="root", password="", database="mydata", port='3306')
        mycursor = conn.cursor()
        mycursor.execute("select Ref from pharma")
        row =mycursor.fetchall()

        # Reference No
        lblRefNo = tk.Label(root, text="Reference No", font=("arial", 12, "bold"), padx=2)
        lblRefNo.place(x=50, y=135)
        ref_combo = ttk.Combobox(root,textvariable=self.refNo, width=32, font=("arial", 12, "bold"), state="readonly")
        ref_combo["values"] = row
        ref_combo.place(x=200, y=135)
        ref_combo.current(0)

        # Company Name
        lblComNa = tk.Label(root, text="Company Name", font=("arial", 12, "bold"), padx=2)
        lblComNa.place(x=50, y=185)
        ComNa_combo = ttk.Combobox(root, textvariable=self.compName,width=32, font=("arial", 12, "bold"), state="readonly")
        ComNa_combo["values"] = ("ACI Limited", "Beximco ", "Ibn Sina","Beacon ","Astra","Healthcare","Incepta")
        ComNa_combo.place(x=200, y=185)
        ComNa_combo.current(0)

        # Type of Medicine
        lblTyOfMed = tk.Label(root, text="Type of Medicine",font=("arial", 12, "bold"), padx=2)
        lblTyOfMed.place(x=50, y=235)
        TyOfMed_combo = ttk.Combobox(root, textvariable=self.typeName,width=32, font=("arial", 12, "bold"), state="readonly")
        TyOfMed_combo["values"] = ("Liquid", "Tablet", "Capsules","Suppositories","Drops","Inhalers","Injections")
        TyOfMed_combo.place(x=200, y=235)
        TyOfMed_combo.current(0)
        
        conn = mysql.connector.connect(host='localhost', username="root", password="", database="mydata", port='3306')
        mycursor = conn.cursor()
        mycursor.execute("select MedName from pharma")
        med =mycursor.fetchall()

        # Medicine Name
        lblMedNa = tk.Label(root, text="Medicine Name", font=("arial", 12, "bold"), padx=2)
        lblMedNa.place(x=50, y=285)
        MedNa_combo = ttk.Combobox(root,textvariable=self.medName, width=32, font=("arial", 12, "bold"), state="readonly")
        MedNa_combo["values"] = med
        MedNa_combo.place(x=200, y=285)
        MedNa_combo.current(0)

        # Lot No
        lblLotNo = tk.Label(root, text="Lot No", font=("arial", 12, "bold"), padx=2)
        lblLotNo.place(x=50, y=335)
        txtLotNo = tk.Entry(root,textvariable=self.lotNo, bd=3, relief=tk.RIDGE, width=34, font=("arial", 12, "bold"))
        txtLotNo.place(x=200, y=335)

        # Issue Date
        lblIssDat = tk.Label(root, text="Issue Date", font=("arial", 12, "bold"), padx=2)
        lblIssDat.place(x=50, y=385)
        txtIssDat = tk.Entry(root,textvariable=self.issDate, bd=3, relief=tk.RIDGE, width=34, font=("arial", 12, "bold"))
        txtIssDat.place(x=200, y=385)

        # Exp Date
        lblExpDat = tk.Label(root, text="Exp Date", font=("arial", 12, "bold"), padx=2)
        lblExpDat.place(x=50, y=435)
        txtExpDat = tk.Entry(root,textvariable=self.expDate, bd=3, relief=tk.RIDGE, width=34, font=("arial", 12, "bold"))
        txtExpDat.place(x=200, y=435)

        # Uses
        lblUses = tk.Label(root, text="Uses", font=("arial", 12, "bold"), padx=2)
        lblUses.place(x=50, y=485)
        txtUses = tk.Entry(root,textvariable=self.uses, bd=3, relief=tk.RIDGE, width=34, font=("arial", 12, "bold"))
        txtUses.place(x=200, y=485)

        # Side Effect
        lblSideEffect = tk.Label(root, text="Side Effect", font=("arial", 12, "bold"), padx=2)
        lblSideEffect.place(x=50, y=535)
        txtSideEffect = tk.Entry(root,textvariable=self.sideEffect, bd=3, relief=tk.RIDGE, width=34, font=("arial", 12, "bold"))
        txtSideEffect.place(x=200, y=535)

        # Prec & Warning
        lblPrecWarning = tk.Label(root, font=("arial", 12, "bold"), text="Prec & Warning:", padx=10, pady=5)
        lblPrecWarning.place(x=600, y=135)
        txtPrecWarning = tk.Entry(root, textvariable=self.waring,font=("arial", 12, "bold"), bg="white", bd=2, relief=tk.RIDGE, width=34)
        txtPrecWarning.place(x=800, y=135)

        # Dosage
        lblDosage = tk.Label(root, font=("arial", 12, "bold"), text="Dosage:", padx=10, pady=5)
        lblDosage.place(x=600, y=185)
        txtDosage = tk.Entry(root,textvariable=self.dosage, font=("arial", 12, "bold"), bg="white", bd=2, relief=tk.RIDGE, width=34)
        txtDosage.place(x=800, y=185)

        # Price
        lblPrice = tk.Label(root, font=("arial", 12, "bold"), text="Tablets Price:", padx=10, pady=5)
        lblPrice.place(x=600, y=235)
        txtPrice = tk.Entry(root,textvariable=self.price, font=("arial", 12, "bold"), bg="white", bd=2, relief=tk.RIDGE, width=34)
        txtPrice.place(x=800, y=235)

        # Product QT
        lblProductQt = tk.Label(root, font=("arial", 12, "bold"), text="Product QT:", padx=10, pady=5)
        lblProductQt.place(x=600, y=285)
        txtProductQt = tk.Entry(root, textvariable=self.proQt,font=("arial", 12, "bold"), bg="white", bd=2, relief=tk.RIDGE, width=34)
        txtProductQt.place(x=800, y=285)
        
        image1 = Image.open("C:/Users/tarik/Desktop/code/RAW_python/Pharmacy/12.jpg")
        image1 =image1.resize((550,250),Image.Resampling.LANCZOS)
        self.photoimage1 =ImageTk.PhotoImage(image1)
        button1 =tk.Button(self.root,image=self.photoimage1,borderwidth=0)
        button1.place(x=560,y=320)

    
        #____________________+++++++++++++++Right Side++++++++++++++++++++++++++++++++++++++++++++++
        Side_Frame = tk.Frame(root, bd=4, relief=tk.RIDGE, bg="white")
        Side_Frame.place(x=1420, y=250, width=425, height=138)
        
        sc_x = ttk.Scrollbar(Side_Frame, orient=tk.HORIZONTAL)
        sc_x.pack(side=tk.BOTTOM, fill=tk.X)

        sc_y = ttk.Scrollbar(Side_Frame, orient=tk.VERTICAL)
        sc_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.medicine_table = ttk.Treeview(Side_Frame, column=("ref", "medname"), xscrollcommand=sc_x.set, yscrollcommand=sc_y.set)
        
        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)
    
        
        
        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name")
        
        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=tk.BOTH,expand=1)
        self.medicine_table.bind("<ButtonRelease-1>",self.Medget_Curser)
        self.fetch_dataMed()
        
        image2 = Image.open("C:/Users/tarik/Desktop/code/RAW_python/Pharmacy/tab.jpeg")
        image2 =image2.resize((450,170),Image.Resampling.LANCZOS)
        self.photoimage2 =ImageTk.PhotoImage(image2)
        button1 =tk.Button(self.root,image=self.photoimage2,borderwidth=0)
        button1.place(x=1420,y=400)
        
        
        lbltitle = tk.Label(self.root, text="PHARMACY MANAGEMENT SYSTEM", bd=15, relief=tk.RIDGE, bg="White",
                            fg="darkgreen", font=("times new roman", 50, "bold"), padx=2, pady=4)
        lbltitle.place(x=0, y=0, relwidth=1)

        # Creating Labels and Entry widgets using place
        lblRefNo = tk.Label(root, font=("arial", 12, "bold"), text="Reference No", padx=10, pady=5)
        lblRefNo.place(x=1400, y=125)
        self.txtRefNo = tk.Entry(root, textvariable=self.refMed, font=("arial", 12, "bold"), bg="white", bd=2, relief=tk.RIDGE, width=32)
        self.txtRefNo.place(x=1600, y=125)
        
        lblMedNam = tk.Label(root, font=("arial", 12, "bold"), text="Medicine Name", padx=10, pady=5)
        lblMedNam.place(x=1400, y=155)
        self.txtMedNam = tk.Entry(root, textvariable=self.addMed, font=("arial", 12, "bold"), bg="white", bd=2, relief=tk.RIDGE, width=32)
        self.txtMedNam.place(x=1600, y=155)

        # Button to trigger AddMed function
        btnAddMed = tk.Button(root, text="Add", command=self.AddMed, bg="lime", fg="white", padx=10, pady=5)
        btnAddMed.place(x=1410, y=195)

        # Button to trigger Update function (assuming you have an Update function)
        btnUpdateMed = tk.Button(root, text="Update",  command=self.Update,bg="yellow", fg="red", padx=10, pady=5)
        btnUpdateMed.place(x=1530, y=195)

        # Button to trigger Delete function (assuming you have a Delete function)
        btnDeleteMed = tk.Button(root, text="Delete",command=self.Delete, bg="red", fg="white", padx=10, pady=5)
        btnDeleteMed.place(x=1700, y=195)

        # Button to trigger Clear function (assuming you have a Clear function)
        btnClearMed = tk.Button(root, text="Clear", command=self.Clear,bg="blue", fg="white", padx=10, pady=5)
        btnClearMed.place(x=1830, y=195)
        #+++++++++++++++++++++++++++++++++++++++++ Down Button ++++++++++++++++++++++++++++++++++++++
        
        # Button to trigger AddMed function
        btnAddMed = tk.Button(root,command=self.AddMed_downTable, text="Add Medicine", bg="Green", fg="white", padx=10, pady=5,width=15)
        btnAddMed.place(x=50, y=595)

        # Button to trigger Update function (assuming you have an Update function)Update_downTable
        btnUpdateMed = tk.Button(root, command=self.Update_downTable,text="Update",bg="yellow", fg="red", padx=10, pady=5)
        btnUpdateMed.place(x=200, y=595)

        # Button to trigger Delete function (assuming you have a Delete function)
        btnDeleteMed = tk.Button(root,command=self.Delete_downTable, text="Delete", bg="red", fg="white", padx=10, pady=5)
        btnDeleteMed.place(x=400, y=595)

        # Button to trigger Clear function (assuming you have a Clear function)
        btnClearMed = tk.Button(root,command=self.Clear_downTable, text="Reset",bg="blue", fg="white", padx=10, pady=5)
        btnClearMed.place(x=600, y=595)
        
        btnClearMed = tk.Button(root, text="Exit",bg="blue", fg="white", padx=10, pady=5)
        btnClearMed.place(x=800, y=595)
        
        lblSearch = tk.Label(root, text="Search By", bg="red", font=("arial", 17, "bold"), fg="white")
        lblSearch.place(x=1000,y=595)
        
        self.search=tk.StringVar()
        serch_combo = ttk.Combobox(root,textvariable=self.search, width=12, font=("arial", 17, "bold"), state="readonly")
        serch_combo["values"] = ("Select Option", "Ref", "Lot")
        serch_combo.place(x=1200,y=595)
        serch_combo.current(0)
         
        self.txtSearch=tk.StringVar()
        txtsearch = tk.Entry(root, textvariable=self.txtSearch,font=("arial", 17, "bold"), bg="white", bd=2, relief=tk.RIDGE, width=13)
        txtsearch.place(x=1400, y=595)
        
        btnClearMed = tk.Button(root,command=self.Search_downTable, text="Search",bg="blue", fg="white", padx=10, pady=5)
        btnClearMed.place(x=1600, y=595) 
        
        btnClearMed = tk.Button(root,command=self.fetch_dataMed_downTable, text="Show All",bg="blue", fg="white", padx=10, pady=5)
        btnClearMed.place(x=1800, y=595)    
        
         #+++++++++++++++++++++== Down Frame Scroll bar ++++++++++++++++++++++++++++==
        TableFrame =tk.Frame(root,bd=15,relief=tk.RIDGE)
        TableFrame.place(x=10,y=650,width=1890,height=350)
         
        scroll_x = ttk.Scrollbar(TableFrame, orient=tk.HORIZONTAL)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

        scroll_y = ttk.Scrollbar(TableFrame, orient=tk.VERTICAL)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)  
        
        self.pharmacy_table = ttk.Treeview(TableFrame, column=("ref", "companyname","type","tabletname","lotno","issuedate","expdate","uses","sideeffect","warning",
                                                               "dosage","price","productqt"), xscrollcommand=sc_x.set, yscrollcommand=sc_y.set)     
        
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y) 
        
        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)
        
        self.pharmacy_table["show"]="headings"
        
        
        self.pharmacy_table.heading("ref",text="Reference No")
        self.pharmacy_table.heading("companyname",text="Company Name")
        self.pharmacy_table.heading("type",text="Type of Medicine")
        self.pharmacy_table.heading("tabletname",text="Tablet  Name")
        self.pharmacy_table.heading("lotno",text="Lot No")
        self.pharmacy_table.heading("issuedate",text="Issues Date")
        self.pharmacy_table.heading("expdate",text="Exp Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideeffect",text="Side Effect")
        self.pharmacy_table.heading("warning",text="Pre&Warning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("productqt",text="Producr Quntity")
        self.pharmacy_table.pack(fill=tk.BOTH,expand=1)
        
        
        self.pharmacy_table.column("ref",width=100)
        self.pharmacy_table.column("companyname",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("tabletname",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("issuedate",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("uses",width=100)
        self.pharmacy_table.column("sideeffect",width=100)
        self.pharmacy_table.column("warning",width=100)
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("productqt",width=100)
        self.pharmacy_table.bind("<ButtonRelease-1>",self.Medget_Curser_downTable)
        self.fetch_dataMed_downTable()

        
     
    def AddMed(self):
        try:
            # Establishing the connection
            conn = mysql.connector.connect(host='localhost', username="root", password="", database="mydata", port='3306')
            mycursor = conn.cursor()

            # Inserting data into the database
            mycursor.execute("INSERT INTO pharma (Ref, MedName) VALUES (%s, %s)", (
                self.refMed.get(), self.addMed.get()
            ))
            conn.commit()
            self.fetch_dataMed()
            self.Medget_Curser()
            messagebox.showinfo("Success", "Medicine added")
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            if conn.is_connected():
                mycursor.close()
                conn.close()
    
    def fetch_dataMed(self):
        conn = mysql.connector.connect(host='localhost', username="root", password="", database="mydata", port='3306')
        mycursor = conn.cursor()
        mycursor.execute("select * from pharma ")
        rows =mycursor.fetchall()
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def Medget_Curser(self, event=""):
      try:
        cursor_row = self.medicine_table.focus()
        content = self.medicine_table.item(cursor_row)
        row = content["values"]
        self.refMed.set(row[0])
        self.addMed.set(row[1])
      except IndexError:
        print("No values found in the selected row.")
        
    def Update(self):
        if self.refMed.get=="" or self.addMed.get()=="":
            messagebox.showerror("eror","All field are requird")
        else:
            conn = mysql.connector.connect(host='localhost', username="root", password="", database="mydata", port='3306')
            mycursor = conn.cursor()
            mycursor.execute("Update pharma set MedName=%s where Ref=%s",(
                self.addMed.get(),self.refMed.get(),
            ))
            conn.commit()
            self.fetch_dataMed()
            conn.close()
            messagebox.showerror("Success","Medicine update")
    def Delete(self):
        conn = mysql.connector.connect(host='localhost', username="root", password="", database="mydata", port='3306')
        mycursor = conn.cursor()
        sql="delete from pharma where Ref=%s"
        val=(self.refMed.get(),)
        mycursor.execute(sql,val)
        conn.commit()
        self.fetch_dataMed()
        conn.close()
        
    def Clear(self):
        self.refMed.set("")
        self.addMed.set("")
    #+++++++++++++++++++++++++++ Main Table SQL code +++++++++++++++++++++++++++
    def AddMed_downTable(self):
        if self.refNo.get()=="" or self.lotNo.get()=="":
            messagebox.showerror("Error","All field are Requird")
        else:
            conn = mysql.connector.connect(host='localhost', username="root", password="", database="mydata", port='3306')
            mycursor = conn.cursor()

                # Inserting data into the database
            mycursor.execute("INSERT INTO pharmacy (Ref,Companyname,TypeMed,Medname,Lotno,Issuedate,Expdate,Uses,Sideeffect,warning,dosage,price,productqt) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s,%s,%s)", (
                        self.refNo.get(),
                        self.compName .get(),
                        self.typeName .get(),
                        self.medName .get(),
                        self.lotNo .get(),
                        self.issDate .get(),
                        self.expDate .get(),
                        self.uses .get(),
                        self.sideEffect .get(),
                        self.waring .get(),
                        self.dosage .get(),
                        self.price .get(),
                        self.proQt .get(),
                ))
            conn.commit()
            self.fetch_dataMed_downTable()
            conn.close()
            messagebox.showerror("Sucess","Data has been Inserted")
            
    def fetch_dataMed_downTable(self):
        conn = mysql.connector.connect(host='localhost', username="root", password="", database="mydata", port='3306')
        mycursor = conn.cursor()
        mycursor.execute("select * from pharmacy ")
        rows =mycursor.fetchall()
        if len(rows)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def Medget_Curser_downTable(self,event=""):
        cursor_row =self.pharmacy_table.focus()
        content =self.pharmacy_table.item(cursor_row)
        row =content["values"]
        self.refNo.set(row[0])
        self.compName.set(row[1])
        self.typeName.set(row[2])
        self.medName.set(row[3])
        self.lotNo.set(row[4])
        self.issDate.set(row[5])
        self.expDate.set(row[6])
        self.uses.set(row[7])
        self.sideEffect.set(row[8])
        self.waring .set(row[9])
        self.dosage.set(row[10])
        self.price.set(row[11])
        self.proQt.set(row[12])
    
    def Update_downTable(self):
        if self.refNo.get=="" or self.lotNo.get()=="":
            messagebox.showerror("eror","All field are requird")
        else:
            conn = mysql.connector.connect(host='localhost', username="root", password="", database="mydata", port='3306')
            mycursor = conn.cursor()
            mycursor.execute("Update pharmacy set Companyname=%s,TypeMed=%s,Medname=%s,Lotno=%s,Issuedate=%s,Expdate=%s,Uses=%s,Sideeffect=%s,warning=%s,dosage=%s,price=%s,productqt=%s where Ref=%s",(
                        self.compName .get(),
                        self.typeName .get(),
                        self.medName .get(),
                        self.lotNo .get(),
                        self.issDate .get(),
                        self.expDate .get(),
                        self.uses .get(),
                        self.sideEffect .get(),
                        self.waring .get(),
                        self.dosage .get(),
                        self.price .get(),
                        self.proQt .get(),
                        self.refNo.get()
            ))
            conn.commit()
            self.fetch_dataMed_downTable()
            conn.close()
            messagebox.showerror("Success","Medicine update")
    def Delete_downTable(self):
        conn = mysql.connector.connect(host='localhost', username="root", password="", database="mydata", port='3306')
        mycursor = conn.cursor()
        sql="delete from pharmacy where Ref=%s"
        val=(self.refNo.get(),)
        mycursor.execute(sql,val)
        conn.commit()
        self.fetch_dataMed_downTable()
        conn.close()
        messagebox.showerror("Delete","Info deleted Successfully")
        
    def Clear_downTable(self):
        self.compName.set("")
        self.lotNo.set("")
        self.issDate.set("")
        self.expDate.set("")
        self.uses.set("")
        self.sideEffect.set("")
        self.waring .set("")
        self.dosage.set("")
        self.price.set("")
        self.proQt.set("")
        
    def Search_downTable(self):
        conn = mysql.connector.connect(host='localhost', username="root", password="", database="mydata", port='3306')
        mycursor = conn.cursor()
        query = "select * from pharmacy where " + str(self.search.get()) + " LIKE '%" + str(self.txtSearch.get()) + "%'"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        if len(rows) != 0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("", END, values=i)
        conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = PharmacyApp(root)
    root.mainloop()
