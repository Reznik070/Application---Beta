from tkinter import *
from tkinter import Tk, StringVar, ttk
import datetime
import random
import time
from tkinter import messagebox

#---------- Main winddow Specs -----------#

Met = Tk()
Met.geometry("1495x800+0+0")
Met.title("Metro-Xpress")
Met.configure(background='black')
Met.resizable(0, 0)


#---------- Main winddow Specs -----------#



#----------Calculator Methods-------------#

equa = ""
equation = StringVar()
refx = StringVar()


def btnPress(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)


def EqualPress():
    global equa
    total = str(eval(equa))
    equation.set(total)
    equa = ""


def btnSquareRoot():
    global equa
    sqrt = math.sqrt(x ** (1 / 2))
    equation.set("")
    equa = ""


def ClearPress():
    global equa
    equa = ""
    equation.set("")


def appex():
    Cal.destroy()


def Percent(num):
    global equa


#----------Calculator Methods-------------#






#----------------------------------App Methods-------------------------------------------------------------------------

#-------------------------------------Regular--------------------------------------------------------------------------#

def total_cost():

    if (H.get() == "Warsaw" and A.get() == 1 and E.get() == 1):
        Tcost = float(43.2)
        oneway = float(J.get())
        adulttax = "PLN", str('%.2f' % ((Tcost * oneway)*0.11))
        adultsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway)*0.11))
        Saletax.set(adulttax)
        Subtotal.set(adultsub)
        Totalx.set(Tcost2)
        CL.set("Regular")
        TP.set(Tcost2)
        TTO.set("Warsaw")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Adult Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Warsaw" and A.get() == 1 and F.get() == 1):
        Tcost = float(25.2)
        oneway = float(J.get())
        childtax = "PLN", str('%.2f' % ((Tcost * oneway)*0.11))
        childsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway)*0.11))
        Saletax.set(childtax)
        Subtotal.set(childsub)
        Totalx.set(Tcost2)
        CL.set("Regular")
        TP.set(Tcost2)
        TTO.set("Warsaw")
        FR.set("Poznan")
        ADT.set("No")
        CHLD.set("Yes")
        TKK.set("Child Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Warsaw" and A.get() == 1 and G.get() == 1):
        Tcost = float(10.2)
        oneway = float(J.get())
        seniortax = "PLN", str('%.2f' % ((Tcost * oneway)*0.11))
        seniorsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway)*0.11))
        Saletax.set(seniortax)
        Subtotal.set(seniorsub)
        Totalx.set(Tcost2)
        CL.set("Regular")
        TP.set(Tcost2)
        TTO.set("Warsaw")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Seniors Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Ursus" and A.get() == 1 and E.get() == 1):
        Tcost = float(25)
        oneway = float(J.get())
        adulttax = "PLN", str('%.2f' % ((Tcost * oneway)*0.11))
        adultsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway)*0.11))
        Saletax.set(adulttax)
        Subtotal.set(adultsub)
        Totalx.set(Tcost2)
        CL.set("Regular")
        TP.set(Tcost2)
        TTO.set("Ursus")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Adult Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Ursus" and A.get() == 1 and F.get() == 1):
        Tcost = float(12)
        oneway = float(J.get())
        childtax = "PLN", str('%.2f' % ((Tcost * oneway)*0.11))
        childsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway)*0.11))
        Saletax.set(childtax)
        Subtotal.set(childsub)
        Totalx.set(Tcost2)
        CL.set("Regular")
        TP.set(Tcost2)
        TTO.set("Ursus")
        FR.set("Poznan")
        ADT.set("No")
        CHLD.set("Yes")
        TKK.set("Child Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Ursus" and A.get() == 1 and G.get() == 1):
        Tcost = float(5.2)
        oneway = float(J.get())
        seniortax = "PLN", str('%.2f' % ((Tcost * oneway)*0.11))
        seniorsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway)*0.11))
        Saletax.set(seniortax)
        Subtotal.set(seniorsub)
        Totalx.set(Tcost2)
        CL.set("Regular")
        TP.set(Tcost2)
        TTO.set("Ursus")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Seniors Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Praga-Polnoc" and A.get() == 1 and E.get() == 1):
        Tcost = float(20)
        oneway = float(J.get())
        adulttax = "PLN", str('%.2f' % ((Tcost * oneway)*0.11))
        adultsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway)*0.11))
        Saletax.set(adulttax)
        Subtotal.set(adultsub)
        Totalx.set(Tcost2)
        CL.set("Regular")
        TP.set(Tcost2)
        TTO.set("Praga-Polnoc")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Adult Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Praga-Polnoc" and A.get() == 1 and F.get() == 1):
        Tcost = float(16)
        oneway = float(J.get())
        childtax = "PLN", str('%.2f' % ((Tcost * oneway)*0.11))
        childsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway)*0.11))
        Saletax.set(childtax)
        Subtotal.set(childsub)
        Totalx.set(Tcost2)
        CL.set("Regular")
        TP.set(Tcost2)
        TTO.set("Praga-Polnoc")
        FR.set("Poznan")
        ADT.set("No")
        CHLD.set("Yes")
        TKK.set("Child Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Praga-Polnoc" and A.get() == 1 and G.get() == 1):
        Tcost = float(11)
        oneway = float(J.get())
        seniortax = "PLN", str('%.2f' % ((Tcost * oneway)*0.11))
        seniorsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway)*0.11))
        Saletax.set(seniortax)
        Subtotal.set(seniorsub)
        Totalx.set(Tcost2)
        CL.set("Regular")
        TP.set(Tcost2)
        TTO.set("Parga-Polnoc")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Seniors Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Stare Maisto" and A.get() == 1 and E.get() == 1):
        Tcost = float(35.3)
        oneway = float(J.get())
        adulttax = "PLN", str('%.2f' % ((Tcost * oneway) * 0.11))
        adultsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway) * 0.11))
        Saletax.set(adulttax)
        Subtotal.set(adultsub)
        Totalx.set(Tcost2)
        CL.set("Regular")
        TP.set(Tcost2)
        TTO.set("Stare Maisto")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Adult Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Stare Maisto" and A.get() == 1 and F.get() == 1):
        Tcost = float(29)
        oneway = float(J.get())
        childtax = "PLN", str('%.2f' % ((Tcost * oneway) * 0.11))
        childsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway) * 0.11))
        Saletax.set(childtax)
        Subtotal.set(childsub)
        Totalx.set(Tcost2)
        CL.set("Regular")
        TP.set(Tcost2)
        TTO.set("Stare Maisto")
        FR.set("Poznan")
        ADT.set("No")
        CHLD.set("Yes")
        TKK.set("Child Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Stare Maisto" and A.get() == 1 and G.get() == 1):
        Tcost = float(23)
        oneway = float(J.get())
        seniortax = "PLN", str('%.2f' % ((Tcost * oneway) * 0.11))
        seniorsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway) * 0.11))
        Saletax.set(seniortax)
        Subtotal.set(seniorsub)
        Totalx.set(Tcost2)
        CL.set("Regular")
        TP.set(Tcost2)
        TTO.set("Stare Maisto")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Seniors Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Willanow" and A.get() == 1 and E.get() == 1):
        Tcost = float(55.3)
        oneway = float(J.get())
        adulttax = "PLN", str('%.2f' % ((Tcost * oneway) * 0.11))
        adultsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway) * 0.11))
        Saletax.set(adulttax)
        Subtotal.set(adultsub)
        Totalx.set(Tcost2)
        CL.set("Regular")
        TP.set(Tcost2)
        TTO.set("Willanow")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Adult Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Willanow" and A.get() == 1 and F.get() == 1):
        Tcost = float(34.98)
        oneway = float(J.get())
        childtax = "PLN", str('%.2f' % ((Tcost * oneway) * 0.11))
        childsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway) * 0.11))
        Saletax.set(childtax)
        Subtotal.set(childsub)
        Totalx.set(Tcost2)
        CL.set("Regular")
        TP.set(Tcost2)
        TTO.set("Willanow")
        FR.set("Poznan")
        ADT.set("No")
        CHLD.set("Yes")
        TKK.set("Child Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Willanow" and A.get() == 1 and G.get() == 1):
        Tcost = float(28.45)
        oneway = float(J.get())
        seniortax = "PLN", str('%.2f' % ((Tcost * oneway) * 0.11))
        seniorsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway) * 0.11))
        Saletax.set(seniortax)
        Subtotal.set(seniorsub)
        Totalx.set(Tcost2)
        CL.set("Regular")
        TP.set(Tcost2)
        TTO.set("Willanow")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Seniors Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

#-------------------------------------Regular--------------------------------------------------------------------------#


#-------------------------------------First Class--------------------------------------------------------------------------#

    elif (H.get() == "Warsaw" and C.get() == 1 and E.get() == 1):
        Tcost = float(73.2)
        oneway = float(J.get())
        adulttax = "PLN", str('%.2f' % ((Tcost * oneway)*0.11))
        adultsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway)*0.11))
        Saletax.set(adulttax)
        Subtotal.set(adultsub)
        Totalx.set(Tcost2)
        CL.set("First")
        TP.set(Tcost2)
        TTO.set("Warsaw")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Adult Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Warsaw" and C.get() == 1 and F.get() == 1):
        Tcost = float(35.2)
        oneway = float(J.get())
        childtax = "PLN", str('%.2f' % ((Tcost * oneway)*0.11))
        childsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway)*0.11))
        Saletax.set(childtax)
        Subtotal.set(childsub)
        Totalx.set(Tcost2)
        CL.set("First")
        TP.set(Tcost2)
        TTO.set("Warsaw")
        FR.set("Poznan")
        ADT.set("No")
        CHLD.set("Yes")
        TKK.set("Child Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Warsaw" and C.get() == 1 and G.get() == 1):
        Tcost = float(19.2)
        oneway = float(J.get())
        seniortax = "PLN", str('%.2f' % ((Tcost * oneway)*0.11))
        seniorsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway)*0.11))
        Saletax.set(seniortax)
        Subtotal.set(seniorsub)
        Totalx.set(Tcost2)
        CL.set("First")
        TP.set(Tcost2)
        TTO.set("Warsaw")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Seniors Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Ursus" and C.get() == 1 and E.get() == 1):
        Tcost = float(49.01)
        oneway = float(J.get())
        adulttax = "PLN", str('%.2f' % ((Tcost * oneway)*0.11))
        adultsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway)*0.11))
        Saletax.set(adulttax)
        Subtotal.set(adultsub)
        Totalx.set(Tcost2)
        CL.set("First")
        TP.set(Tcost2)
        TTO.set("Ursus")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Adult Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Ursus" and C.get() == 1 and F.get() == 1):
        Tcost = float(22.5)
        oneway = float(J.get())
        childtax = "PLN", str('%.2f' % ((Tcost * oneway)*0.11))
        childsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway)*0.11))
        Saletax.set(childtax)
        Subtotal.set(childsub)
        Totalx.set(Tcost2)
        CL.set("First")
        TP.set(Tcost2)
        TTO.set("Ursus")
        FR.set("Poznan")
        ADT.set("No")
        CHLD.set("Yes")
        TKK.set("Child Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Ursus" and C.get() == 1 and G.get() == 1):
        Tcost = float(9.2)
        oneway = float(J.get())
        seniortax = "PLN", str('%.2f' % ((Tcost * oneway)*0.11))
        seniorsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway)*0.11))
        Saletax.set(seniortax)
        Subtotal.set(seniorsub)
        Totalx.set(Tcost2)
        CL.set("First")
        TP.set(Tcost2)
        TTO.set("Ursus")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Seniors Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Praga-Polnoc" and C.get() == 1 and E.get() == 1):
        Tcost = float(39.21)
        oneway = float(J.get())
        adulttax = "PLN", str('%.2f' % ((Tcost * oneway)*0.11))
        adultsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway)*0.11))
        Saletax.set(adulttax)
        Subtotal.set(adultsub)
        Totalx.set(Tcost2)
        CL.set("First")
        TP.set(Tcost2)
        TTO.set("Praga-Polnoc")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Adult Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Praga-Polnoc" and C.get() == 1 and F.get() == 1):
        Tcost = float(30)
        oneway = float(J.get())
        childtax = "PLN", str('%.2f' % ((Tcost * oneway)*0.11))
        childsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway)*0.11))
        Saletax.set(childtax)
        Subtotal.set(childsub)
        Totalx.set(Tcost2)
        CL.set("First")
        TP.set(Tcost2)
        TTO.set("Praga-Polnoc")
        FR.set("Poznan")
        ADT.set("No")
        CHLD.set("Yes")
        TKK.set("Child Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Praga-Polnoc" and C.get() == 1 and G.get() == 1):
        Tcost = float(18)
        oneway = float(J.get())
        seniortax = "PLN", str('%.2f' % ((Tcost * oneway)*0.11))
        seniorsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway)*0.11))
        Saletax.set(seniortax)
        Subtotal.set(seniorsub)
        Totalx.set(Tcost2)
        CL.set("First")
        TP.set(Tcost2)
        TTO.set("Parga-Polnoc")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Seniors Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Stare Maisto" and C.get() == 1 and E.get() == 1):
        Tcost = float(71.3)
        oneway = float(J.get())
        adulttax = "PLN", str('%.2f' % ((Tcost * oneway) * 0.11))
        adultsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway) * 0.11))
        Saletax.set(adulttax)
        Subtotal.set(adultsub)
        Totalx.set(Tcost2)
        CL.set("First")
        TP.set(Tcost2)
        TTO.set("Stare Maisto")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Adult Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Stare Maisto" and C.get() == 1 and F.get() == 1):
        Tcost = float(49)
        oneway = float(J.get())
        childtax = "PLN", str('%.2f' % ((Tcost * oneway) * 0.11))
        childsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway) * 0.11))
        Saletax.set(childtax)
        Subtotal.set(childsub)
        Totalx.set(Tcost2)
        CL.set("First")
        TP.set(Tcost2)
        TTO.set("Stare Maisto")
        FR.set("Poznan")
        ADT.set("No")
        CHLD.set("Yes")
        TKK.set("Child Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Stare Maisto" and C.get() == 1 and G.get() == 1):
        Tcost = float(33)
        oneway = float(J.get())
        seniortax = "PLN", str('%.2f' % ((Tcost * oneway) * 0.11))
        seniorsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway) * 0.11))
        Saletax.set(seniortax)
        Subtotal.set(seniorsub)
        Totalx.set(Tcost2)
        CL.set("First")
        TP.set(Tcost2)
        TTO.set("Stare Maisto")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Seniors Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Willanow" and C.get() == 1 and E.get() == 1):
        Tcost = float(100.3)
        oneway = float(J.get())
        adulttax = "PLN", str('%.2f' % ((Tcost * oneway) * 0.11))
        adultsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway) * 0.11))
        Saletax.set(adulttax)
        Subtotal.set(adultsub)
        Totalx.set(Tcost2)
        CL.set("First")
        TP.set(Tcost2)
        TTO.set("Willanow")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Adult Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Willanow" and C.get() == 1 and F.get() == 1):
        Tcost = float(70.98)
        oneway = float(J.get())
        childtax = "PLN", str('%.2f' % ((Tcost * oneway) * 0.11))
        childsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway) * 0.11))
        Saletax.set(childtax)
        Subtotal.set(childsub)
        Totalx.set(Tcost2)
        CL.set("First")
        TP.set(Tcost2)
        TTO.set("Willanow")
        FR.set("Poznan")
        ADT.set("No")
        CHLD.set("Yes")
        TKK.set("Child Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Willanow" and C.get() == 1 and G.get() == 1):
        Tcost = float(48.45)
        oneway = float(J.get())
        seniortax = "PLN", str('%.2f' % ((Tcost * oneway) * 0.11))
        seniorsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway) * 0.11))
        Saletax.set(seniortax)
        Subtotal.set(seniorsub)
        Totalx.set(Tcost2)
        CL.set("First")
        TP.set(Tcost2)
        TTO.set("Willanow")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Seniors Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

#--------------------------------------------First--------------------------------------------------------------------#


#--------------------------------------------Student------------------------------------------------------------------#


    elif (H.get() == "Warsaw" and D.get() == 1 and E.get() == 1):
        Tcost = float(73.2/2)
        oneway = float(J.get())
        adulttax = "PLN", str('%.2f' % ((Tcost * oneway)*0.11))
        adultsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway)*0.11))
        Saletax.set(adulttax)
        Subtotal.set(adultsub)
        Totalx.set(Tcost2)
        CL.set("Student")
        TP.set(Tcost2)
        TTO.set("Warsaw")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Adult Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Warsaw" and D.get() == 1 and F.get() == 1):
        Tcost = float(35.2/2)
        oneway = float(J.get())
        childtax = "PLN", str('%.2f' % ((Tcost * oneway)*0.11))
        childsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway)*0.11))
        Saletax.set(childtax)
        Subtotal.set(childsub)
        Totalx.set(Tcost2)
        CL.set("Student")
        TP.set(Tcost2)
        TTO.set("Warsaw")
        FR.set("Poznan")
        ADT.set("No")
        CHLD.set("Yes")
        TKK.set("Child Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Warsaw" and D.get() == 1 and G.get() == 1):
        Tcost = float(19.2/2)
        oneway = float(J.get())
        seniortax = "PLN", str('%.2f' % ((Tcost * oneway)*0.11))
        seniorsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway)*0.11))
        Saletax.set(seniortax)
        Subtotal.set(seniorsub)
        Totalx.set(Tcost2)
        CL.set("Student")
        TP.set(Tcost2)
        TTO.set("Warsaw")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Seniors Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Ursus" and D.get() == 1 and E.get() == 1):
        Tcost = float(49.01/2)
        oneway = float(J.get())
        adulttax = "PLN", str('%.2f' % ((Tcost * oneway)*0.11))
        adultsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway)*0.11))
        Saletax.set(adulttax)
        Subtotal.set(adultsub)
        Totalx.set(Tcost2)
        CL.set("Student")
        TP.set(Tcost2)
        TTO.set("Ursus")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Adult Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Ursus" and D.get() == 1 and F.get() == 1):
        Tcost = float(22.5/2)
        oneway = float(J.get())
        childtax = "PLN", str('%.2f' % ((Tcost * oneway)*0.11))
        childsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway)*0.11))
        Saletax.set(childtax)
        Subtotal.set(childsub)
        Totalx.set(Tcost2)
        CL.set("Student")
        TP.set(Tcost2)
        TTO.set("Ursus")
        FR.set("Poznan")
        ADT.set("No")
        CHLD.set("Yes")
        TKK.set("Child Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Ursus" and D.get() == 1 and G.get() == 1):
        Tcost = float(9.2/2)
        oneway = float(J.get())
        seniortax = "PLN", str('%.2f' % ((Tcost * oneway)*0.11))
        seniorsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway)*0.11))
        Saletax.set(seniortax)
        Subtotal.set(seniorsub)
        Totalx.set(Tcost2)
        CL.set("Student")
        TP.set(Tcost2)
        TTO.set("Ursus")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Seniors Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Praga-Polnoc" and D.get() == 1 and E.get() == 1):
        Tcost = float(39.21/2)
        oneway = float(J.get())
        adulttax = "PLN", str('%.2f' % ((Tcost * oneway)*0.11))
        adultsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway)*0.11))
        Saletax.set(adulttax)
        Subtotal.set(adultsub)
        Totalx.set(Tcost2)
        CL.set("Student")
        TP.set(Tcost2)
        TTO.set("Praga-Polnoc")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Adult Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Praga-Polnoc" and D.get() == 1 and F.get() == 1):
        Tcost = float(30/2)
        oneway = float(J.get())
        childtax = "PLN", str('%.2f' % ((Tcost * oneway)*0.11))
        childsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway)*0.11))
        Saletax.set(childtax)
        Subtotal.set(childsub)
        Totalx.set(Tcost2)
        CL.set("Child")
        TP.set(Tcost2)
        TTO.set("Praga-Polnoc")
        FR.set("Poznan")
        ADT.set("No")
        CHLD.set("Yes")
        TKK.set("Child Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Praga-Polnoc" and D.get() == 1 and G.get() == 1):
        Tcost = float(18/2)
        oneway = float(J.get())
        seniortax = "PLN", str('%.2f' % ((Tcost * oneway)*0.11))
        seniorsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway)*0.11))
        Saletax.set(seniortax)
        Subtotal.set(seniorsub)
        Totalx.set(Tcost2)
        CL.set("Student")
        TP.set(Tcost2)
        TTO.set("Parga-Polnoc")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Seniors Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Stare Maisto" and D.get() == 1 and E.get() == 1):
        Tcost = float(71.3/2)
        oneway = float(J.get())
        adulttax = "PLN", str('%.2f' % ((Tcost * oneway) * 0.11))
        adultsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway) * 0.11))
        Saletax.set(adulttax)
        Subtotal.set(adultsub)
        Totalx.set(Tcost2)
        CL.set("Student")
        TP.set(Tcost2)
        TTO.set("Stare Maisto")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Adult Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Stare Maisto" and D.get() == 1 and F.get() == 1):
        Tcost = float(49/2)
        oneway = float(J.get())
        childtax = "PLN", str('%.2f' % ((Tcost * oneway) * 0.11))
        childsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway) * 0.11))
        Saletax.set(childtax)
        Subtotal.set(childsub)
        Totalx.set(Tcost2)
        CL.set("Student")
        TP.set(Tcost2)
        TTO.set("Stare Maisto")
        FR.set("Poznan")
        ADT.set("No")
        CHLD.set("Yes")
        TKK.set("Child Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Stare Maisto" and D.get() == 1 and G.get() == 1):
        Tcost = float(33/2)
        oneway = float(J.get())
        seniortax = "PLN", str('%.2f' % ((Tcost * oneway) * 0.11))
        seniorsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway) * 0.11))
        Saletax.set(seniortax)
        Subtotal.set(seniorsub)
        Totalx.set(Tcost2)
        CL.set("Student")
        TP.set(Tcost2)
        TTO.set("Stare Maisto")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Seniors Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Willanow" and D.get() == 1 and E.get() == 1):
        Tcost = float(100.3/2)
        oneway = float(J.get())
        adulttax = "PLN", str('%.2f' % ((Tcost * oneway) * 0.11))
        adultsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway) * 0.11))
        Saletax.set(adulttax)
        Subtotal.set(adultsub)
        Totalx.set(Tcost2)
        CL.set("Student")
        TP.set(Tcost2)
        TTO.set("Willanow")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Adult Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Willanow" and D.get() == 1 and F.get() == 1):
        Tcost = float(70.98/2)
        oneway = float(J.get())
        childtax = "PLN", str('%.2f' % ((Tcost * oneway) * 0.11))
        childsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway) * 0.11))
        Saletax.set(childtax)
        Subtotal.set(childsub)
        Totalx.set(Tcost2)
        CL.set("Student")
        TP.set(Tcost2)
        TTO.set("Willanow")
        FR.set("Poznan")
        ADT.set("No")
        CHLD.set("Yes")
        TKK.set("Child Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

    elif (H.get() == "Willanow" and D.get() == 1 and G.get() == 1):
        Tcost = float(48.45/2)
        oneway = float(J.get())
        seniortax = "PLN", str('%.2f' % ((Tcost * oneway) * 0.11))
        seniorsub = "PLN", str('%.2f' % (Tcost * oneway))
        Tcost2 = "PLN", str('%.2f' % ((Tcost * oneway) + (Tcost * oneway) * 0.11))
        Saletax.set(seniortax)
        Subtotal.set(seniorsub)
        Totalx.set(Tcost2)
        CL.set("Student")
        TP.set(Tcost2)
        TTO.set("Willanow")
        FR.set("Poznan")
        ADT.set("Yes")
        CHLD.set("No")
        TKK.set("Seniors Fee")

        x = random.randint(109, 5000)
        randomRef = str(x)
        refx.set("TLK" + randomRef)

#------------------------------------------------------Student---------------------------------------------------------#


def check_butt():


    if (Z.get() == 1):
        J.set("")
        E1.configure(state=NORMAL)
        E2.configure(state=DISABLED)
    elif Z.get() == 0:
        E1.configure(state=DISABLED)
        E2.configure(state=DISABLED)
        J.set("0")
def check_butt1():

    if (K.get() == 1):
        L.set("")
        E2.configure(state=NORMAL)
        E1.configure(state=DISABLED)

    elif K.get() == 0:
        E2.configure(state=DISABLED)
        E1.configure(state=DISABLED)
        L.set("0")

def check_off():


    if   A.get() == 1:
        checkcStudent.configure(state=DISABLED)
        checkcFirst.configure(state=DISABLED)
    elif A.get() == 0:
         checkcFirst.configure(state=ACTIVE)
         checkcStudent.configure(state=ACTIVE)
def check_offf():

    if  C.get() == 1:
        checkcRegular.configure(state=DISABLED)
        checkcStudent.configure(state=DISABLED)
    elif C.get() == 0:
         checkcRegular.configure(state=ACTIVE)
         checkcStudent.configure(state=ACTIVE)

def check_offff():

    if  D.get() == 1:
        checkcFirst.configure(state=DISABLED)
        checkcRegular.configure(state=DISABLED)
    elif D.get() == 0:
         checkcRegular.configure(state=ACTIVE)
         checkcFirst.configure(state=ACTIVE)


def exitnow():

        mess = messagebox.askyesno(title='quit', message='Are you sure?')
        if mess == 1:
            Met.destroy()

def cls():

    A.set("0")
    #B.set("0")
    C.set("0")
    D.set("0")
    E.set("0")
    F.set("0")
    G.set("0")
    H.set("")
    Z.set("0")
    J.set("0")
    K.set("0")
    L.set("0")
    CL.set("")
    Saletax.set("0")
    Subtotal.set("0")
    Totalx.set("0")
    TKK.set("")
    CHLD.set("")
    ADT.set("")
    TTO.set("")
    FR.set("")
    TP.set("")
    refx.set("")


#---------- VARIABLES

A = IntVar()
Z = IntVar()
C = IntVar()
D = IntVar()
E = IntVar()
F = IntVar()
G = IntVar()
H = StringVar()
Z = IntVar()
J = StringVar()
K = IntVar()
L = StringVar()
M = StringVar()
N = StringVar()
timer = StringVar()
Saletax = StringVar()
Subtotal = StringVar()
Totalx = StringVar()
CL = StringVar()
TTO = StringVar()
TP = StringVar()
FR = StringVar()
CHLD = StringVar()
ADT = StringVar()
TKK = StringVar()








#Checkbox_set_off--------------------------------------------------------------------------------------

A.set("0")
#B.set("0")
C.set("0")
D.set("0")
E.set("0")
F.set("0")
G.set("0")
Z.set("0")
J.set("0")
L.set("0")
K.set("0")
refx.set("")









#---------- Frames --------------#

Top = Frame(Met, width=1900, height=110, bd=14, relief="raise")
Top.pack(side=TOP)

f1 = Frame(Met, width=1000, height=800, bd=9, relief='raise')
f1.pack(side=LEFT)

f2 = Frame(Met, width=500, height=900, bd=9, relief='raise')
f2.pack(side=RIGHT)

f2i = Frame(f2, width=500, height=700, bd=16, relief='raise')
f2i.pack(side=TOP)
f2j = Frame(f2, width=500, height=600, bd=14, relief='raise')
f2j.pack(side=BOTTOM)

f1i = Frame(f1, width=1000, height=400, bd=9, relief='raise')
f1i.pack(side=TOP)
f1j = Frame(f1, width=1000, height=360, bd=8, relief='raise')
f1j.pack(side=BOTTOM)


topleft1 = Frame(f1i, width=333.3, height=220, bd=15, relief='raise')
topleft1.pack(side=LEFT)
topleft2 = Frame (f1i, width=333.3, height=220, bd=15, relief='raise')
topleft2.pack(side=RIGHT)
topleft3 = Frame(f1i, width=333.3, height=220, bd=15, relief='raise')
topleft3.pack(side=RIGHT)

Top.configure(background='black')
f1.configure(background='black')
f2.configure(background='black')

bottomleft1 = Frame(f1j, width=500, height=500, bd=13, relief='raise')
bottomleft1.pack(side=LEFT)
bottomleft2 = Frame(f1j, width=500, height=500, bd=13, relief='raise')
bottomleft2.pack(side=RIGHT)

#---------- Frames --------------#

Toptitle = Label(Top, font=('arial', 65, 'bold'), text="METRO -EXPRESS SELF SERVICE", bd=14, anchor='w')
Toptitle.grid(row=0, column=0)








#------------------------------------Date of order---------------------------------------------------------------------

timer.set(time.strftime("%d:%m:%Y"))
N.set(time.strftime('%H:%M:%S'))



#---------- VARIABLES

#----------Widget for topleft1

Label_class = Label(topleft1, font=('arial', 15, 'bold'), text="Class", bd=8)
Label_class.grid(row=0,column=0, sticky=W)
checkcRegular = Checkbutton(topleft1, font=('arial', 15, 'bold'), text='Regular', variable=A, onvalue=1, offvalue=0,
                            command=check_off)
checkcRegular.grid(row=1, column=0, sticky=W)
#checkcEconomy = Checkbutton(topleft1, font=('arial', 15, 'bold'), text='Economy', variable=B, onvalue=1, offvalue=0)
#checkcEconomy.grid(row=2, column=0, sticky=W)
checkcFirst = Checkbutton(topleft1, font=('arial', 15, 'bold'), text='First Class', variable=C, onvalue=1, offvalue=0,
                          command=check_offf)
checkcFirst.grid(row=3, column=0, sticky=W)
checkcStudent= Checkbutton(topleft1, font=('arial', 15, 'bold'), text='Student', variable=D, onvalue=1, offvalue=0,
                           command=check_offff)
checkcStudent.grid(row=4, column=0, sticky=W)

#-----------Widget for topleft1

#------------Widget for topleft2

Label_destination = Label(topleft3, font=('arial', 15, 'bold'), text="Destination", bd=8)
Label_destination.grid(row=0, column=0, sticky=W)
checkcadult = Checkbutton(topleft3, font=('arial', 15, 'bold'), text='Adult', variable=E, onvalue=1, offvalue=0)
checkcadult.grid(row=1, column=0, sticky=W)
checkchild= Checkbutton(topleft3, font=('arial', 15, 'bold'), text='Child', variable=F, onvalue=1, offvalue=0)
checkchild.grid(row=2, column=0, sticky=W)
checksenior = Checkbutton(topleft3, font=('arial', 15, 'bold'), text='Seniors', variable=G, onvalue=1, offvalue=0)
checksenior.grid(row=3, column=0, sticky=W)

cmbx_destination = ttk.Combobox(topleft3, textvariable=H, state='readonly', font=('arial', 15, 'bold'), width=20)
cmbx_destination['value'] = ('', 'Warsaw', 'Ursus', 'Praga-Polnoc', 'Stare Maisto', 'Willanow')
cmbx_destination.current(0)
cmbx_destination.grid(row=0, column=1, sticky=W)

#------------Widget for topleft2

#------------Widget for topleft3


Label_tcktyp = Label(topleft2, font=('arial', 15, 'bold'), text="Ticket Type", bd=8)
Label_tcktyp.grid(row=0, column=0, sticky=W)

checkoneway = Checkbutton(topleft2, font=('arial', 15, 'bold'), variable=Z, text='One Way', onvalue=1, offvalue=0, command=check_butt)
checkoneway.grid(row=1, column=0, sticky=W)

E1 = Entry(topleft2, font=('arial', 15, 'bold'), textvariable=J, bd=4, width=15, state=DISABLED)
E1.grid(row=1, column=1, sticky=W)

checkreturn= Checkbutton(topleft2, font=('arial', 15, 'bold'), text='Return', variable=K, onvalue=1, offvalue=0, command=check_butt1)
checkreturn.grid(row=2, column=0, sticky=W)

E2 = Entry(topleft2, font=('arial', 15, 'bold'), textvariable=L, bd=4, width=15, state=DISABLED)
E2.grid(row=2, column=1, sticky=W)

Label_empty = Label(topleft2, font=('arial', 15, 'bold'), bd=8)
Label_empty.grid(row=3, column=0, sticky=W)

#------------Widget for topleft2


#-------------Calculator



Lcal = Label(bottomleft2, textvariable = equation,width=30,height=2,background="white")
Lcal.grid(columnspan=6, ipady=4)

B1 = Button(bottomleft2, text="Clear", borderwidth=3, width=5, height=2, relief=RAISED, command=ClearPress)
B1.grid(row=1, column=0)
B2 = Button(bottomleft2, text="%", borderwidth=3, command=Percent, width=15, height=2, relief=RAISED)
B2.grid(row=1, column=1, padx=3, pady=3)

B3 = Button(bottomleft2, text="I/O", borderwidth=3, command=appex, width=15, height=2, relief=RAISED)
B3.grid(row=1, column=2, padx=3, pady=3)
B0 = Button(bottomleft2,text="X",borderwidth=3,command =lambda: btnPress("*"),width=15,height=2,relief=RAISED)
B0.grid(row=1,column=3,padx=3,pady=3)


B4 = Button(bottomleft2,text="9",borderwidth=3,command = lambda:btnPress(9),width=15,height=2,relief=RAISED)
B4.grid(row=2,column=0,padx=3,pady=3)

B5 = Button(bottomleft2,text="8",borderwidth=3,command = lambda:btnPress(8),width=15,height=2,relief=RAISED)
B5.grid(row=2,column=1,padx=3,pady=3)
B6 = Button(bottomleft2,text="7",borderwidth=3,command = lambda:btnPress(7),width=15,height=2,relief=RAISED)
B6.grid(row=2,column=2,padx=3,pady=3)

B7 = Button(bottomleft2,text="-",borderwidth=3,command = lambda:btnPress("-"),width=15,height=2,relief=RAISED)
B7.grid(row=2,column=3,padx=3,pady=3)
B8 = Button(bottomleft2,text="6",borderwidth=3,command = lambda:btnPress(6),width=15,height=2,relief=RAISED)
B8.grid(row=3,column=0,padx=3,pady=3)

B9 = Button(bottomleft2,text="5",borderwidth=3,command = lambda:btnPress(5),width=15,height=2,relief=RAISED)
B9.grid(row=3,column=1,padx=3,pady=3)
B10 = Button(bottomleft2,text="4",borderwidth=3,command = lambda:btnPress(4),width=15,height=2,relief=RAISED)
B10.grid(row=3,column=2,padx=3,pady=3)

B11 = Button(bottomleft2,text="+",borderwidth=3,command = lambda:btnPress("+"),width=15,height=2,relief=RAISED)
B11.grid(row=3,column=3,padx=3,pady=3)
B12 = Button(bottomleft2,text="3",borderwidth=3,command = lambda:btnPress(3),width=15,height=2,relief=RAISED)
B12.grid(row=4,column=0,padx=3,pady=3)

B13 = Button(bottomleft2,text="2",borderwidth=3,command = lambda:btnPress(2),width=15,height=2,relief=RAISED)
B13.grid(row=4,column=1,padx=3,pady=3)
B14 = Button(bottomleft2,text="1",borderwidth=3,command = lambda:btnPress(1),width=15,height=2,relief=RAISED)
B14.grid(row=4,column=2,padx=3,pady=3)

B15 = Button(bottomleft2,text="/",borderwidth=3,command = lambda:btnPress("/"),width=15,height=2,relief=RAISED)
B15.grid(row=4,column=3,padx=3,pady=3)
B16 = Button(bottomleft2,text="0",borderwidth=3,command = lambda:btnPress(0),width=15,height=2,relief=RAISED)
B16.grid(row=5,column=0,padx=3,pady=3)

B17 = Button(bottomleft2,text=".",borderwidth=3,command = lambda:btnPress("."),width=15,height=2,relief=RAISED)
B17.grid(row=5,column=1,padx=3,pady=3)
B18 = Button(bottomleft2,text="=",borderwidth=3,command=EqualPress,width=15,height=5,relief=RAISED)
B18.grid(row=5,column=2,padx=3,pady=3)

B19 = Button(bottomleft2,text="Sq",borderwidth=3,command = btnSquareRoot,width=15,height=2,relief=RAISED)
B19.grid(row=5,column=3,padx=3,pady=3)


#--------------------------------------------SALE AND TAXES---------------------------------------------------------------------------

Label_saleTax = Label(bottomleft1, font=('arial', 15, 'bold'), text="Sales Tax", bd=8)
Label_saleTax.grid(row=0 ,column=0)

Label2_saletax = Label(bottomleft1, font=('arial', 15, 'bold'), textvariable=Saletax, bd=4, width=20)
Label2_saletax.grid(row=0, column=1)

Label_subtotal = Label(bottomleft1, font=('arial', 15, 'bold'), text="Sub Total", bd=8)
Label_subtotal.grid(row=1, column=0)

Label2_subtotal = Label(bottomleft1, font=('arial', 15, 'bold'), textvariable=Subtotal, bd=4, width=20)
Label2_subtotal.grid(row=1, column=1)

Label_total = Label(bottomleft1, font=('arial', 15, 'bold'), text="Total", bd=8)
Label_total.grid(row=2, column=0)

Label2_total = Label(bottomleft1, font=('arial', 15, 'bold'), textvariable=Totalx, bd=4, width=20)
Label2_total.grid(row=2, column=1)


#-------------------------------------------CLIENT VIEW------------------------------------------------------------------------------------------


Labelhead = Label(f2i, font=('arial', 15, 'bold'), text="Client Information", bd=4, width=42)
Labelhead.grid(row=0, column=0)


Labelclass = Label(f2j, font=('arial', 15, 'bold'), text="Class", width=10,relief='sunken')
Labelclass.grid(row=0, column=0)
Labelclass1 = Label(f2j, font=('arial', 15, 'bold'), width=10, textvariable=CL, relief='sunken')
Labelclass1.grid(row=1, column=0)

Labelticket = Label(f2j, font=('arial', 15, 'bold'), text="Ticket", width=10,relief='sunken')
Labelticket.grid(row=0, column=1)
Labelticket1 = Label(f2j, font=('arial', 15, 'bold'), textvariable= TKK, width=10,relief='sunken')
Labelticket1.grid(row=1, column=1)

Labelchild = Label(f2j, font=('arial', 15, 'bold'), text="Child", width=10,relief='sunken')
Labelchild.grid(row=0, column=2)
Labelchild1 = Label(f2j, font=('arial', 15, 'bold'), width=10, textvariable= CHLD, relief='sunken')
Labelchild1.grid(row=1, column=2)

Labeladult = Label(f2j, font=('arial', 15, 'bold'), text="Adult", width=10, relief='sunken')
Labeladult.grid(row=0, column=3)
Labeladult1 = Label(f2j, font=('arial', 15, 'bold'), width=10, textvariable= ADT, relief='sunken')
Labeladult1.grid(row=1, column=3)

Labelfrom = Label(f2j, font=('arial', 15, 'bold'),text="From", width=10,relief='sunken')
Labelfrom.grid(row=3, column=0)
Labelfrom1 = Label(f2j, font=('arial', 15, 'bold'), textvariable=FR, width=10,relief='sunken')
Labelfrom1.grid(row=3, column=1)

Labelto = Label(f2j, font=('arial', 15, 'bold'),text="To", width=10,relief='sunken')
Labelto.grid(row=4, column=0)
Labelto1 = Label(f2j, font=('arial', 15, 'bold'), width=10, textvariable=TTO, relief='sunken')
Labelto1.grid(row=4, column=1)

Labelprice = Label(f2j, font=('arial', 15, 'bold'),text="Price", width=10,relief='sunken')
Labelprice.grid(row=5, column=0)
Labelprice1 = Label(f2j, font=('arial', 15, 'bold'), width=10, textvariable= TP, relief='sunken')
Labelprice1.grid(row=5, column=1)

Labelref = Label(f2j, font=('arial', 15, 'bold'),text="Reference no.", width=11,relief='sunken')
Labelref.grid(row=6, column=0)
Labelref1 = Label(f2j, font=('arial', 15, 'bold'), width=10, textvariable= refx, relief='sunken')
Labelref1.grid(row=6, column=1)

Labeltime = Label(f2j, font=('arial', 15, 'bold'),text="Time", width=10,relief='sunken')
Labeltime.grid(row=7, column=0)
Labeltime1 = Label(f2j, font=('arial', 15, 'bold'), width=10, textvariable=N, relief='sunken')
Labeltime1.grid(row=7, column=1)

Labeldate = Label(f2j, font=('arial', 15, 'bold'),text="Date", width=10,relief='sunken')
Labeldate.grid(row=8, column=0,pady=3)
Labeldate1 = Label(f2j, font=('arial', 15, 'bold'), width=10, textvariable=timer, relief='sunken')
Labeldate1.grid(row=8, column=1,pady=2)

#-------------------------------------------Buttons---------------------------------------------------------------------

B1 = Button(f2j, width=8, bd=3, fg="blue", text="Total", command=total_cost)
B1.grid(row=9, column=0, padx=2, pady=100)
B2 = Button(f2j, width=8, bd=2, fg="blue", text="Clear", command=cls)
B2.grid(row=9, column=1, padx=2, pady=3)
B3 = Button(f2j, width=8, bd=3, fg="blue", text="Exit", command=exitnow)
B3.grid(row=9, column=2, padx=2, pady=3)
B4 = Button(f2j, width=8, bd=3, fg="blue", text="Checkout")
B4.grid(row=9, column=3, padx=2, pady=3)

#-----------------------------------------Info--------------------------------------------------------------------------

#Labelinfo = Label(f2j, font=('arial', 15, 'bold'),text="Client Receipt", width=13)
#Labelinfo.grid(row=10, column=0, pady=5)

#Textinfo = Text(f2j, width=30, height=7, bg="white",  font=('arial', 15, 'bold'), bd=8)
#Textinfo.grid(row=11, column=0, columnspan=4)

Met.mainloop()