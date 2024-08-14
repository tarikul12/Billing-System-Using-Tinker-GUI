import tkinter as tk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector
from tkinter import ttk,HORIZONTAL, VERTICAL,BOTTOM,X,Y,END

class BillingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Billing Software System")
        self.root.geometry("1900x800+0+0")
        
        image1 = Image.open("C:/Users/tarik/Desktop/code/RAW_python/Billing_System/bil.png")
        image1 =image1.resize((650,200),Image.Resampling.LANCZOS)
        self.photoimage1 =ImageTk.PhotoImage(image1)
        button1 =tk.Button(self.root,image=self.photoimage1,borderwidth=0)
        button1.place(x=0,y=0)
        
        image2 = Image.open("C:/Users/tarik/Desktop/code/RAW_python/Billing_System/shop.png")
        image2 =image2.resize((650,200),Image.Resampling.LANCZOS)
        self.photoimage2 =ImageTk.PhotoImage(image2)
        button1 =tk.Button(self.root,image=self.photoimage2,borderwidth=0)
        button1.place(x=650,y=0)
        
        image3 = Image.open("C:/Users/tarik/Desktop/code/RAW_python/Billing_System/super.png")
        image3 =image3.resize((650,200),Image.Resampling.LANCZOS)
        self.photoimage3 =ImageTk.PhotoImage(image3)
        button1 =tk.Button(self.root,image=self.photoimage3,borderwidth=0)
        button1.place(x=1300,y=0)
        
        # Title label using grid instead of pack
        lbltitle = tk.Label(self.root, text="BILLING SOFTWARE SYSTEM", relief=tk.RIDGE, bg="White",fg="red", font=("times new roman", 40, "bold"), padx=2, pady=4)
        lbltitle.place(x=0, y=200, width=1920)
        
        #########################  Customer Details +++++++++++++++++++++
        lblCustomer = tk.Label(root, text="Customer",fg="red", font=("arial", 15, "bold"), padx=2)
        lblCustomer.place(x=0, y=275)
        
        lblMobileNo = tk.Label(root, text="Mobile No:", font=("arial", 12, "bold"), padx=2)
        lblMobileNo.place(x=0, y=310)
        txtMobileNo = tk.Entry(root, bd=3, relief=tk.RIDGE, width=25, font=("arial", 12, "bold"))
        txtMobileNo.place(x=150, y=310)

      
        lblCustomName = tk.Label(root, text="Customer Name:", font=("arial", 12, "bold"), padx=2)
        lblCustomName.place(x=0, y=360)
        txtCustomName = tk.Entry(root, bd=3, relief=tk.RIDGE, width=25, font=("arial", 12, "bold"))
        txtCustomName.place(x=150, y=360)

        
        lblEmail = tk.Label(root,text="Email:",font=("arial", 12, "bold"), padx=2)
        lblEmail.place(x=0, y=410)
        txtEmail = tk.Entry(root,font=("arial", 12, "bold"), bg="white", bd=2, relief=tk.RIDGE, width=25)
        txtEmail.place(x=150, y=410)
        
         #########################  Product Details +++++++++++++++++++++
        lblProduct = tk.Label(root, text="Product",fg="red", font=("arial", 15, "bold"), padx=2)
        lblProduct.place(x=470, y=275)
        
        lblSelectCat = tk.Label(root, text="Select Category:", font=("arial", 12, "bold"), padx=2)
        lblSelectCat.place(x=470, y=310)
        select_combo = ttk.Combobox(root, width=23, font=("arial", 12, "bold"), state="readonly")
        select_combo["values"] = ("ref")
        select_combo.place(x=640, y=310)
        select_combo.current(0)
        
        lblSubCategory = tk.Label(root, text="Sub Category:", font=("arial", 12, "bold"), padx=2)
        lblSubCategory.place(x=470, y=360)
        SubCategory_combo = ttk.Combobox(root, width=23, font=("arial", 12, "bold"), state="readonly")
        SubCategory_combo["values"] = ("ref")
        SubCategory_combo.place(x=640, y=360)
        SubCategory_combo.current(0)

      
        lblProductName = tk.Label(root, text="Product Name:", font=("arial", 12, "bold"), padx=2)
        lblProductName.place(x=470, y=410)
        productName_combo = ttk.Combobox(root, width=23, font=("arial", 12, "bold"), state="readonly")
        productName_combo["values"] = ("ref")
        productName_combo.place(x=640, y=410)
        productName_combo.current(0)
        
        lblPrice = tk.Label(root, text="Price:", font=("arial", 12, "bold"), padx=2)
        lblPrice.place(x=920, y=310)
        Price_combo = ttk.Combobox(root, width=23, font=("arial", 12, "bold"), state="readonly")
        Price_combo["values"] = ("ref")
        Price_combo.place(x=1000, y=310)
        Price_combo.current(0)

        
        lblQty = tk.Label(root,text="Quantity:",font=("arial", 12, "bold"), padx=2)
        lblQty.place(x=920, y=360)
        txtQty = tk.Entry(root,font=("arial", 12, "bold"), bg="white", bd=2, relief=tk.RIDGE, width=25)
        txtQty.place(x=1000, y=360)
        
        #+++++++++++++++++++++ Bill Section +++++++++++++++++++
        
        btnBilNumber = tk.Button(root, text="Bill Number",font=("arial", 12, "bold"), bg="red", fg="white",width=15)
        btnBilNumber.place(x=1260, y=280)
        
        txtSearch = tk.Entry(root,font=("arial", 15, "bold"), bg="white", bd=2, relief=tk.RIDGE,width=20)
        txtSearch.place(x=1450, y=280)
        
        btnBilSrarch = tk.Button(root, text="Search",font=("arial", 12, "bold"), bg="red", fg="white",width=15,cursor="hand2")
        btnBilSrarch.place(x=1700, y=280)
        
        
        
        lblBill = tk.Label(root, text="Bill Area",fg="red", font=("arial", 9, "bold"), padx=2)
        lblBill.place(x=1260, y=330)
        
        Side_Frame = tk.Frame(root, bd=4, relief=tk.RIDGE, bg="white")
        Side_Frame.place(x=1250, y=360, width=640, height=450)
        
    
        sc_y = ttk.Scrollbar(Side_Frame, orient=tk.VERTICAL)
        sc_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.Bill_table = ttk.Treeview(Side_Frame, yscrollcommand=sc_y.set)
        
        sc_y.config(command=self.Bill_table.yview)
        self.Bill_table.pack(fill=tk.BOTH,expand=1)
        
        image4 = Image.open("C:/Users/tarik/Desktop/code/RAW_python/Billing_System/g.jpg")
        image4 =image4.resize((600,350),Image.Resampling.LANCZOS)
        self.photoimage4 =ImageTk.PhotoImage(image4)
        button1 =tk.Button(self.root,image=self.photoimage4,borderwidth=0)
        button1.place(x=0,y=450)
        
        image5 = Image.open("C:/Users/tarik/Desktop/code/RAW_python/Billing_System/H.jpg")
        image5 =image5.resize((630,350),Image.Resampling.LANCZOS)
        self.photoimage5 =ImageTk.PhotoImage(image5)
        button1 =tk.Button(self.root,image=self.photoimage5,borderwidth=0)
        button1.place(x=600,y=450)
        
        #########################  Bill Counter  +++++++++++++++++++++
        lblCustomer = tk.Label(root, text="Bill Counter",fg="red", font=("arial", 15, "bold"), padx=2)
        lblCustomer.place(x=0, y=800)
        
        lblMobileNo = tk.Label(root, text="Sub Total:", font=("arial", 12, "bold"), padx=2)
        lblMobileNo.place(x=0, y=850)
        txtMobileNo = tk.Entry(root, bd=3, relief=tk.RIDGE, width=25, font=("arial", 12, "bold"))
        txtMobileNo.place(x=120, y=850)

      
        lblCustomName = tk.Label(root, text="Gov Tax:", font=("arial", 12, "bold"), padx=2)
        lblCustomName.place(x=0, y=900)
        txtCustomName = tk.Entry(root, bd=3, relief=tk.RIDGE, width=25, font=("arial", 12, "bold"))
        txtCustomName.place(x=120, y=900)

        
        lblEmail = tk.Label(root,text="Total:",font=("arial", 12, "bold"), padx=2)
        lblEmail.place(x=0, y=950)
        txtEmail = tk.Entry(root,font=("arial", 12, "bold"), bg="white", bd=2, relief=tk.RIDGE, width=25)
        txtEmail.place(x=120, y=950)
        
        #+++++++++++++++++++++++++++++++++++++++++ Down Button ++++++++++++++++++++++++++++++++++++++
        btnAddCart = tk.Button(root, text="Add to Cart",font=("arial", 12, "bold"), bg="orangered", fg="white", padx=10, pady=5,width=25,height=3,cursor="hand2")
        btnAddCart.place(x=400, y=880)

        btnGenBill = tk.Button(root, text="Generate Bill",font=("arial", 12, "bold"), bg="orangered", fg="white", padx=10, pady=5,width=25,height=3,cursor="hand2")
        btnGenBill.place(x=660, y=880)

        btnSaveBill = tk.Button(root, text="Save Bill",font=("arial", 12, "bold"), bg="orangered", fg="white", padx=10, pady=5,width=25,height=3,cursor="hand2")
        btnSaveBill.place(x=920, y=880)

        btnPrint = tk.Button(root, text="Print",font=("arial", 12, "bold"), bg="orangered", fg="white", padx=10, pady=5,width=25,height=3,cursor="hand2")
        btnPrint.place(x=1180, y=880)
        
        btnClear = tk.Button(root, text="Clear", font=("arial", 12, "bold"),bg="orangered", fg="white", padx=10, pady=5,width=25,height=3,cursor="hand2")
        btnClear.place(x=1440, y=880)
        
        btnExit = tk.Button(root, text="Exit",font=("arial", 12, "bold"), bg="orangered", fg="white", padx=10, pady=5,width=25,height=3,cursor="hand2")
        btnExit.place(x=1700, y=880)
      
     
    
if __name__ == "__main__":
    root = tk.Tk()
    app = BillingSystem(root)
    root.mainloop()