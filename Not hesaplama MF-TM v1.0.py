from tkinter import *
from tkinter import messagebox
pencere = Tk()
pencere.title("Not Hesaplayıcı MF-TM")
pencere.geometry("464x280")
def bilgif():
    messagebox.showinfo("Bilgi", "ebubekir07a@gmail.com")
"""
def temizleyici():
    matnotgir.delete(0, END)
    fiziknotgir.delete(0, END)
    kimyanotgir.delete(0, END)
    biyonotgir.delete(0, END)
    edebnotgir.delete(0, END)
    tarihnotgir.delete(0, END)
    felnotgir.delete(0, END)
    dinnotgir.delete(0, END)
    ingnotgir.delete(0, END)
    bednotgir.delete(0, END)
    muziknotgir.delete(0, END)
    almnotgir.delete(0, END)
"""    
    
def alanmf():
    mf = Button(pencere,text="MF",bg="green",command=alanmf)
    mf.place(relx=0.6,rely=0.90)

    tm = Button(pencere,text="TM",command=alantm)
    tm.place(relx=0.67,rely=0.90)
    

    def girisyapma():
        matnot = int(matnotgir.get())
        fiziknot = int(fiziknotgir.get())
        kimyanot = int(kimyanotgir.get())
        biyonot = int(biyonotgir.get())
        edebnot = int(edebnotgir.get())
        tarihnot = int(tarihnotgir.get())
        felnot = int(felnotgir.get())
        dinnot = int(dinnotgir.get())
        ingnot = int(ingnotgir.get())
        bednot = int(bednotgir.get())
        muziknot = int(muziknotgir.get())
        almnot = int(almnotgir.get())

        mat=matnot*6
        fizik=fiziknot*4
        kimya=kimyanot*4
        biyo=biyonot*4
        edeb=edebnot*5
        tarih=tarihnot*2
        fel=felnot*2
        din=dinnot*2
        ing=ingnot*4
        bed=bednot*2
        muzik=muziknot*2
        alm=almnot*2

        ort=(mat+fizik+kimya+biyo+edeb+tarih+fel+din+ing+bed+muzik+alm)/39
    
        if 70<=ort<85:
            if (matnot<50) or (fiziknot<50) or (kimyanot<50) or (biyonot<50) or (edebnot<50) or (tarihnot<50) or (felnot<50) or (dinnot<50) or (ingnot<50) or (bednot<50) or (muziknot<50) or (almnot<50):
                belgedurum.config(text="Belge yok zayıf var", bg="red")
                tesgos.config(text="Yeterli")
                takgos.config(text="Yeterli")

            else:
                tak=85-ort
                tesgos.config(text="Yeterli")
                takgos.config(text=round(tak, 2))
                belgedurum.config(text="Teşekkür", bg="orange")
            
            
        elif 85<=ort<=100:
            if (matnot<50) or (fiziknot<50) or (kimyanot<50) or (biyonot<50) or (edebnot<50) or (tarihnot<50) or (felnot<50) or (dinnot<50) or (ingnot<50) or (bednot<50) or (muziknot<50) or (almnot<50):
                belgedurum.config(text="Belge yok zayıf var", bg="red")
                tesgos.config(text="Yeterli")
                takgos.config(text="Yeterli")
            
            else:
                belgedurum.config(text="Takdir", bg="green")
                tesgos.config(text="Yeterli")
                takgos.config(text="Yeterli")
            
        else:
            tes=70-ort
            tak=85-ort
            tesgos.config(text=round(tes, 2))
            takgos.config(text=round(tak, 2))
            belgedurum.config(text="Belge yok", bg="red")
      
    
       
    
        girisdurumu.config(text=round(ort, 2))
    def temizleyici():
        matnotgir.delete(0, END)
        fiziknotgir.delete(0, END)
        kimyanotgir.delete(0, END)
        biyonotgir.delete(0, END)
        edebnotgir.delete(0, END)
        tarihnotgir.delete(0, END)
        felnotgir.delete(0, END)
        dinnotgir.delete(0, END)
        ingnotgir.delete(0, END)
        bednotgir.delete(0, END)
        muziknotgir.delete(0, END)
        almnotgir.delete(0, END)

    matisim  = Label(pencere,text = "Matematik=")
    matisim.grid(row=0,column=0)
    matnotgir = Entry(pencere,width="8")
    matnotgir.grid(row=0,column=1)

    fizikisim = Label(pencere,width=10, text="Fizik=")
    fizikisim.grid(row=1,column=0)
    fiziknotgir = Entry(pencere,width="8")
    fiziknotgir.grid(row=1,column=1)

    kimyaisim  = Label(pencere,width=10,text = "Kimya=")
    kimyaisim.grid(row=2,column=0)
    kimyanotgir = Entry(pencere,width="8")
    kimyanotgir.grid(row=2,column=1)

    biyoisim  = Label(pencere,width=10,text = "Biyoloji=")
    biyoisim.grid(row=3,column=0)
    biyonotgir = Entry(pencere,width="8")
    biyonotgir.grid(row=3,column=1)

    edebisim  = Label(pencere,text = "Edebiyat=")
    edebisim.grid(row=4,column=0)
    edebnotgir = Entry(pencere,width="8")
    edebnotgir.grid(row=4,column=1)

    tarihisim  = Label(pencere,text = "Tarih=")
    tarihisim.grid(row=5,column=0)
    tarihnotgir = Entry(pencere,width="8")
    tarihnotgir.grid(row=5,column=1)

    felisim  = Label(pencere,text = "Felsefe=")
    felisim.grid(row=6,column=0)
    felnotgir = Entry(pencere,width="8")
    felnotgir.grid(row=6,column=1)

    dinisim  = Label(pencere,text = "Din K.=")
    dinisim.grid(row=7,column=0)
    dinnotgir = Entry(pencere,width="8")
    dinnotgir.grid(row=7,column=1)

    ingisim  = Label(pencere,text = "İngilizce=")
    ingisim.grid(row=8,column=0)
    ingnotgir = Entry(pencere,width="8")
    ingnotgir.grid(row=8,column=1)

    bedisim  = Label(pencere,text = "Beden=")
    bedisim.grid(row=9,column=0)
    bednotgir = Entry(pencere,width="8")
    bednotgir.grid(row=9,column=1)

    muzikisim  = Label(pencere,text = "Müz/Gör=")
    muzikisim.grid(row=10,column=0)
    muziknotgir = Entry(pencere,width="8")
    muziknotgir.grid(row=10,column=1)

    almisim  = Label(pencere,text = "Almanca=")
    almisim.grid(row=11,column=0)
    almnotgir = Entry(pencere,width="8")
    almnotgir.grid(row=11,column=1)

    pskisim  = Label(pencere,width="8",text = "")
    pskisim.grid(row=12,column=0)
    psknotgir  = Label(pencere,width="8",text = "")
    psknotgir.grid(row=12,column=1)
 

    temizle = Button(pencere,text="Temizle",command=temizleyici)
    temizle.place(relx=0.43,rely=0.90)
    
    giris = Button(pencere,text="Hesapla",command=girisyapma)
    giris.grid(row=12,column=3)
    girisdurumu = Label(pencere,width=15,text="")
    girisdurumu.grid(row=0,column=5)
##-------------------------------##
def alantm():
    mf = Button(pencere,text="MF",command=alanmf)
    mf.place(relx=0.6,rely=0.90)

    tm = Button(pencere,text="TM",bg="green",command=alantm)
    tm.place(relx=0.67,rely=0.90)
    def girisyapma():
        matnot = int(matnotgir.get())
        cognot = int(cognotgir.get())
        secedbnot = int(secedbnotgir.get())
        tkmtnot = int(tkmtnotgir.get())
        edebnot = int(edebnotgir.get())
        tarihnot = int(tarihnotgir.get())
        felnot = int(felnotgir.get())
        dinnot = int(dinnotgir.get())
        ingnot = int(ingnotgir.get())
        bednot = int(bednotgir.get())
        muziknot = int(muziknotgir.get())
        almnot = int(almnotgir.get())
        psknot = int(psknotgir.get())

        mat=matnot*6
        cog=cognot*4
        secedb=secedbnot*3
        tkmt=tkmtnot*2
        edeb=edebnot*5
        tarih=tarihnot*2
        fel=felnot*2
        din=dinnot*2
        ing=ingnot*4
        bed=bednot*2
        muzik=muziknot*2
        alm=almnot*2
        psk=psknot*2

        ort=(mat+cog+secedb+tkmt+edeb+tarih+fel+din+ing+bed+muzik+alm+psk)/38
    
        if 70<=ort<85:
            if (matnot<50) or (cognot<50) or (psknot<50) or (secedbnot<50) or (tkmtnot<50) or (edebnot<50) or (tarihnot<50) or (felnot<50) or (dinnot<50) or (ingnot<50) or (bednot<50) or (muziknot<50) or (almnot<50):
                belgedurum.config(text="Belge yok zayıf var", bg="red")
                tesgos.config(text="Yeterli")
                takgos.config(text="Yeterli")

            else:
                tak=85-ort
                tesgos.config(text="Yeterli")
                takgos.config(text=round(tak, 2))
                belgedurum.config(text="Teşekkür", bg="orange")
            
            
        elif 85<=ort<=100:
            if (matnot<50) or (cognot<50) or (psknot<50) or (secedbnot<50) or (tkmtnot<50) or (edebnot<50) or (tarihnot<50) or (felnot<50) or (dinnot<50) or (ingnot<50) or (bednot<50) or (muziknot<50) or (almnot<50):
                belgedurum.config(text="Belge yok zayıf var", bg="red")
                tesgos.config(text="Yeterli")
                takgos.config(text="Yeterli")
            
            else:
                belgedurum.config(text="Takdir", bg="green")
                tesgos.config(text="Yeterli")
                takgos.config(text="Yeterli")
            
        else:
            tes=70-ort
            tak=85-ort
            tesgos.config(text=round(tes, 2))
            takgos.config(text=round(tak, 2))
            belgedurum.config(text="Belge yok", bg="red")
      
    
       
    
        girisdurumu.config(text=round(ort, 2))
    def temizleyici():
        matnotgir.delete(0, END)
        cognotgir.delete(0, END)
        secedbnotgir.delete(0, END)
        tkmtnotgir.delete(0, END)
        edebnotgir.delete(0, END)
        tarihnotgir.delete(0, END)
        felnotgir.delete(0, END)
        dinnotgir.delete(0, END)
        ingnotgir.delete(0, END)
        bednotgir.delete(0, END)
        muziknotgir.delete(0, END)
        almnotgir.delete(0, END)
        psknotgir.delete(0, END)
    
    matisim  = Label(pencere,text = "Matematik=")
    matisim.grid(row=0,column=0)
    matnotgir = Entry(pencere,width="8")
    matnotgir.grid(row=0,column=1)

    cogisim = Label(pencere,width=10, text="Coğrafya=")
    cogisim.grid(row=1,column=0)
    cognotgir = Entry(pencere,width="8")
    cognotgir.grid(row=1,column=1)

    secedbisim  = Label(pencere,width=10,text = "Seçmeli Edb.=")
    secedbisim.grid(row=2,column=0)
    secedbnotgir = Entry(pencere,width="8")
    secedbnotgir.grid(row=2,column=1)

    tkmtisim  = Label(pencere,width=10,text = "Tkmt=")
    tkmtisim.grid(row=3,column=0)
    tkmtnotgir = Entry(pencere,width="8")
    tkmtnotgir.grid(row=3,column=1)

    edebisim  = Label(pencere,text = "Edebiyat=")
    edebisim.grid(row=4,column=0)
    edebnotgir = Entry(pencere,width="8")
    edebnotgir.grid(row=4,column=1)

    tarihisim  = Label(pencere,text = "Tarih=")
    tarihisim.grid(row=5,column=0)
    tarihnotgir = Entry(pencere,width="8")
    tarihnotgir.grid(row=5,column=1)

    felisim  = Label(pencere,text = "Felsefe=")
    felisim.grid(row=6,column=0)
    felnotgir = Entry(pencere,width="8")
    felnotgir.grid(row=6,column=1)

    dinisim  = Label(pencere,text = "Din K.=")
    dinisim.grid(row=7,column=0)
    dinnotgir = Entry(pencere,width="8")
    dinnotgir.grid(row=7,column=1)

    ingisim  = Label(pencere,text = "İngilizce=")
    ingisim.grid(row=8,column=0)
    ingnotgir = Entry(pencere,width="8")
    ingnotgir.grid(row=8,column=1)

    bedisim  = Label(pencere,text = "Beden=")
    bedisim.grid(row=9,column=0)
    bednotgir = Entry(pencere,width="8")
    bednotgir.grid(row=9,column=1)

    muzikisim  = Label(pencere,text = "Müz/Gör=")
    muzikisim.grid(row=10,column=0)
    muziknotgir = Entry(pencere,width="8")
    muziknotgir.grid(row=10,column=1)

    almisim  = Label(pencere,text = "Almanca=")
    almisim.grid(row=11,column=0)
    almnotgir = Entry(pencere,width="8")
    almnotgir.grid(row=11,column=1)

    pskisim  = Label(pencere,text = "Psikoloji=")
    pskisim.grid(row=12,column=0)
    psknotgir = Entry(pencere,width="8")
    psknotgir.grid(row=12,column=1)

    temizle = Button(pencere,text="Temizle",command=temizleyici)
    temizle.place(relx=0.43,rely=0.90)
    
    giris = Button(pencere,text="Hesapla",command=girisyapma)
    giris.grid(row=12,column=3)
    girisdurumu = Label(pencere,width=15,text="")
    girisdurumu.grid(row=0,column=5)



##----------------------------------------------------------------------------------------------

bilgi = Button(pencere,text="Bilgi",command=bilgif)
bilgi.place(relx=0.92,rely=0.9)


command=alanmf()
tesk = Label(pencere,width=22,text="Teşekkür için gereken puan=")
tesk.grid(row=1,column=4)
tesgos=Label(pencere,width=15,text="")
tesgos.grid(row=1,column=5)

takd = Label(pencere,width=22,text="Takdir için gereken puan=")
takd.grid(row=2,column=4)
takgos=Label(pencere,width=15,text="")
takgos.grid(row=2,column=5)

belge = Label(pencere,width=22,text="Belge=")
belge.grid(row=3,column=4)
belgedurum=Label(pencere,width=15,text="")
belgedurum.grid(row=3,column=5)


sonuc = Label(pencere,width=22,text="Ortalama=")
sonuc.grid(row=0,column=4)

mf = Button(pencere,text="MF",bg="green",command=alanmf)
mf.place(relx=0.6,rely=0.90)

tm = Button(pencere,text="TM",command=alantm)
tm.place(relx=0.67,rely=0.90)


pencere.mainloop()
