from tkinter import *
import webbrowser


class Linkopener():
    #functions
    def openchem():
        chemwin=Toplevel()
        chemwin.title("Pick a Chemistry Note!")
        def a():
            webbrowser.open_new(D["C"]["Cptep"])
        def b():
            webbrowser.open_new(D["C"]["Crr"])
        def c():
            webbrowser.open_new(D["C"]["Csbe"])
        def d():
            webbrowser.open_new(D["C"]["Csom"])
        def e():
            webbrowser.open_new(D["C"]["Cequ"])
        A=Button(chemwin,text="Periodic Table Elements and Properties",command=a)
        B=Button(chemwin,text="Redox Reactions",width=29,command=b)
        C=Button(chemwin,text="S - Block Elements",width=29,command=c)
        D=Button(chemwin,text="States of Matter",width=29,command=d)
        E=Button(chemwin,text="Equilibrium",width=29,command=e)
        A.grid(row=1)
        B.grid(row=2)
        C.grid(row=3)
        D.grid(row=4)
        E.grid(row=5)

    def openphy():
        phywin=Toplevel()
        phywin.title("Pick a Physics Note!")
        def f():
            webbrowser.open_new(D["P"]["Ppos"])
        def g():
            webbrowser.open_new(D["P"]["Ppof"])
        def h():
            webbrowser.open_new(D["P"]["Ptpom"])
        F=Button(phywin,text="Mechanical Properties of Solids",width=29,command=f)
        G=Button(phywin,text="Mechanical Properties of Fluids",width=29,command=g)
        H=Button(phywin,text="Thermal Properties of Matter",width=29,command=h)
        F.grid(row=1)
        G.grid(row=2)
        H.grid(row=3)
    
    def openmaths():
        mathwin=Toplevel()
        mathwin.title("Pick a Mathematics Note!")
        def i():
            webbrowser.open_new(D["M"]["Msas"])
        def j():
            webbrowser.open_new(D["M"]["Mlad"])
        def k():
            webbrowser.open_new(D["M"]["Mstat"])
        def l():
            webbrowser.open_new(D["M"]["MTrigo"])
        def m():
            webbrowser.open_new(D["M"]["MPandC"])
        I=Button(mathwin,text="Sequence and Series",width=29,command=i)
        J=Button(mathwin,text="Limits and Derivatives",width=29,command=j)
        K=Button(mathwin,text="Statistics",width=29,command=k)
        L=Button(mathwin,text="Trigonometry",width=29,command=l)
        M=Button(mathwin,text="Permutations and Combinations",width=29,command=m)
        I.grid(row=1)
        J.grid(row=2)
        K.grid(row=3)
        L.grid(row=4)
        M.grid(row=5)


global D
#urls
D = {
"C":
{   #Periodic Table Elements and Properties
    "Cptep":"https://adventurous-experience-634.notion.site/57bfe372a53d455d94af6a8557513545?v=f5aef227c7524f889764dd86ca99b644",
    #Redox Reactions
    "Crr":"https://adventurous-experience-634.notion.site/Redox-Reactions-e0f7b2e779c040578978843475c02909",
    #S - Block Elements
    "Csbe":"https://adventurous-experience-634.notion.site/S-Block-Elements-b175d5c6d0a3485da45f2347b1635fa5",
    #States of Matter
    "Csom":"https://adventurous-experience-634.notion.site/8948292858984f8090800d78b5e5ded3",
    #Equilibrium
    "Cequ":"https://adventurous-experience-634.notion.site/Equillibrium-561b75e279d94c0fba5abf0454b1ab66",
    #Thermodynamics
    "Ctherm":"https://adventurous-experience-634.notion.site/Thermodynamics-254cd8dec2f04d04bf17fe5584252683"
},
"P":
{
    #Mechanical properties of solids
    "Ppos":"https://irradiated-mechanic-943.notion.site/Mechanical-Properties-of-Solids-ec4ed58925d84dd5881659065e2c9926",
    #Mechanical properties of fluids
    "Ppof":"https://irradiated-mechanic-943.notion.site/Mechanical-Properties-of-Fluids-2866c0265c144372be5c32a1e88dcfa4",
    #Thermal properties of matter
    "Ptpom":"https://www.notion.so/Thermal-Properties-of-Matter-9377a9b85c1f4f599fb4e830bd22f456"
},
"M":
{
    #Sequence and Series
    "Msas":"https://www.notion.so/Sequences-And-Series-ba3a4b3e329842c8b0463d0756a2cb51",
    #Limits and derivatives
    "Mlad":"https://www.notion.so/Limits-and-Derivatives-5a25556c3c1342f088a3c3839e3429a6",
    #Statistics
    "Mstat":"https://www.notion.so/Statistics-02095af4dd2d412a8cf669da6d1087ba",
    #Trigonometry
    "MTrigo":"https://hilarious-lentil-236.notion.site/Trigonometry-6e07b618ab0346f4a7a18b4ff196a6de",
    #Permutations and combinations
    "MPandC":"https://hilarious-lentil-236.notion.site/Permutations-and-Combinations-710e1a5639ce45c984c24866dfc84750"
}
}
