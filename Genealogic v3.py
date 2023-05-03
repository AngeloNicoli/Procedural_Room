import random
from tkinter import *
import time

People = [None] * 10
counter = [0]
master = Tk()
master.title("3D Projection v0.8")
master.configure(bg="#dddddd")  #3e3e42
master.geometry("600x700")

canvas_width = 600
canvas_height = 500
anagraphic=[]

canvas = Canvas(width=canvas_width, height= canvas_height, bg='gray')  
canvas.grid(row=0,column=0, rowspan=4,columnspan =4)


# Father is generation 1
N_Generations = 4

N_People = (2**N_Generations) -1
People = [None] * N_People

print("Numero di persone da creare: " +str(N_People))

# This class contain information about Person
class Person:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.child_01 = "Chil"
        self.child_02 = "Dren"
        self.abs_share = 1
        self.rel_share = 1
        self.level = 1
        self.rect_area = [0]

    def get_parent(self):
        return self.parent 

    def get_child_Left(self):
        return self.child_01.name
    
    def get_child_Right(self):
        return self.child_02.name
    
    def get_name(self):
        return self.name

    def __str__(self):
        if self.parent != "Nobody":
            return f" Level:{self.level};\n Name: {self.name};\n Father:to fix \n Child 01: {self.get_child_Left()};\n Child 02: {self.get_child_Right()};\n Abs: {self.abs_share};\n Rel: {self.rel_share};\n {self.rect_area}"
        else:
            return f" Level:{self.level};\n Name: {self.name};\n Father: to fix\n Child 01: {self.get_child_Left()};\n Child 02: {self.get_child_Right()};\n Abs: {self.abs_share};\n Rel: {self.rel_share};\n Rel:{self.rect_area}"

Alph_beta = ["AO","BO","CO","DO","EO","FO","GO","AOE","BOE","COE","DOE","EOE","FOE","GOE"]

Father = Person("CLETUS","Nobody")
Father.rect_area = [10,10,canvas_width-10,canvas_height-10]

a = canvas.create_rectangle(Father.rect_area, width=1, fill='#3CB371', tags="Big")

print(Father.rect_area[3])
# Da errore perchè i figli non sono ancora stati creati come classi, ma come stringhe
#print(Father)

def Create_Generations(node,n):
    global counter
    #print("Il valore di n è: " + str(n))
    if n > 0:
        counter[0] += 1
        #print("Il contatore vale: " +str(counter))    
        child = Person(random.choice(Alph_beta),node)
        child.level = 6 - n
        node.child_01 = child 
        share = random.randint(40,60)
        child.parent = node
        child.rel_share =  share
        child.abs_share = (node.abs_share * share)/100 

        Randomness = random.choice((1,0))
        child.rect_area = [None] *4
        print(Randomness)
        if Randomness == 1:
            print("EEEEE")
            child.rect_area[0] = node.rect_area[0]
            child.rect_area[1] = node.rect_area[1] 
            child.rect_area[2] = node.rect_area[2]
            child.rect_area[3] = node.rect_area[1] + ((node.rect_area[3]-node.rect_area[1]) * share/100)
        else: 
            child.rect_area[0] = node.rect_area[0]
            child.rect_area[1] = node.rect_area[1] 
            child.rect_area[2] = node.rect_area[0] + ((node.rect_area[2]-node.rect_area[0]) * share/100)
            child.rect_area[3] = node.rect_area[3] 
        print("rettangplo 1" + str(child.rect_area))
        a =canvas.create_rectangle(child.rect_area, width=2, fill= "#85CBD9", tags="level"+str(child.level))
        b = canvas.create_rectangle(child.rect_area[0]+random.randint(5,10),child.rect_area[1]+random.randint(5,10),child.rect_area[2]-random.randint(5,10),child.rect_area[3]-random.randint(5,10), width=2, fill='gray', tags="level"+str(child.level))
        Create_Generations(child,n-1)

        child = Person(random.choice(Alph_beta),node)
        child.level = 6 - n
        child.rel_share = 100 - share
        node.child_02 = child 
        child.abs_share = ((node.abs_share) * child.rel_share)/100
        child.parent = node
        
        child.rect_area = [None] *4

        if Randomness == 1:
            child.rect_area[0] = node.rect_area[0]
            child.rect_area[1] = node.rect_area[1] + ((node.rect_area[3]-node.rect_area[1]) *  share/100)
            child.rect_area[2] = node.rect_area[2]
            child.rect_area[3] = node.rect_area[3]
        else: 
            child.rect_area[0] = node.rect_area[0] + ((node.rect_area[2]-node.rect_area[0]) * share/100)
            child.rect_area[1] = node.rect_area[1] 
            child.rect_area[2] = node.rect_area[2]
            child.rect_area[3] = node.rect_area[3] 
        a = canvas.create_rectangle(child.rect_area, width=2, fill='#90EE90', tags="level"+str(child.level))
        b = canvas.create_rectangle(child.rect_area[0]+5,child.rect_area[1]+5,child.rect_area[2]-5,child.rect_area[3]-5, width=2, fill='gray', tags="level"+str(child.level))
        print("Rettangplo 2" + str(child.rect_area) + " level "+str(child.level))
        Create_Generations(child,n-1)
        #print(node)
        anagraphic.append(node)

  
    #else:
        #print("Finito")


def delete(layer_num):
    canvas.tag_raise("level" + str(layer_num))  


def create(iteration_time):
    canvas.delete("all")
    Create_Generations(Father,iteration_time)

btn_div =Button(text="Show division", command=lambda: delete(e.get()+1))

btn_new =Button(text="Create new Map", command=lambda: create(w.get()))

w = Scale(master,from_=1, to=6, orient=HORIZONTAL)
w.set(4)

e = Scale(master,from_=1, to=8, orient=HORIZONTAL)
e.set(4)

btn_div.grid(row=5,column=0, sticky = W+E)
e.grid(row=5,column=1)

btn_new.grid(row=6,column=0, sticky = W+E)
w.grid(row=6,column=1)

'''print(Father)
print(type(Father.child_01))

print(Father.get_child_Left())
print(Father.child_01.get_child_Left())

print(Father.child_01)
print(Father.child_02)

print(Father.child_01.child_01)
print(Father.child_01.child_02)'''
Create_Generations(Father,4)
print(anagraphic)
print(anagraphic[0])
print(anagraphic[2])

master.mainloop()