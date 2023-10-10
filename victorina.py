from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Викторина")
root.geometry("300x300")

def que_one():
  question = Label(root, text="Висит груша нельзя скушать?")
  answer = Entry()
  btn = Button(root, text="Ответить!", command=lambda: game1(que_two))
  question.grid()
  answer.grid()
  btn.grid()
  
  def game1(que_two):
      if answer.get().lower() == "лампочка":
          que_two()
      else:
         messagebox.showerror("Ошибка!", "Попробуй еще раз!")
        
def que_two():
  question_2 = Label(root, text="Зимой и летом одним цветом?")
  answer_2 = Entry()
  btn_2 = Button(root, text="Ответить!", command=lambda: game2(que_one))
  question_2.grid()
  answer_2.grid()
  btn_2.grid()
  
  def game2(que_two):
      if answer_2.get().lower() == "ёлка":
          messagebox.showinfo("Победа!", "Ты молодец!")
      else:
          messagebox.showerror("Ошибка!", "Попробуй еще раз!")
          
que_one()

root.mainloop()

