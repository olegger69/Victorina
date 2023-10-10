from tkinter import *

root = Tk()
root.title("Викторина")
root.geometry("400x400")

def que_one():
  question = Label(root, text="Висит груша нельзя скушать?")
  answer = Entry()
  btn = Button(root, text="Ответить!")
  question.grid(row=0)
  answer.grid(row=1)
  btn.grid(row=2)
  
def que_two():
  question_2 = Label(root, text="Зимой и летом одним цветом?")
  answer_2 = Entry()
   btn = Button(root, text="Ответить!")
   question_2.grid(row=0)
  answer_2.grid(row=1)
  btn_2.grid(row=2)
  
que_one()


root.mainloop()

