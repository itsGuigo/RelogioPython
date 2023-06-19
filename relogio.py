import tkinter as tk
import time
import math

largura = 400 #width
altura = 400 #height

root = tk.Tk()
root.title("Relógio")
canvas = tk.Canvas(root, width=largura, height=altura, bg="white")
canvas.pack()

def update_relogio():
        canvas.delete("all")
        now = time.localtime()
        hour = now.tm_hour % 12
        minute = now.tm_min
        segundo = now.tm_sec
        
#desenho do relogio
        canvas.create_oval(2,2, largura, altura, outline="black", width=2)

        #desenho das horas
        for i in range(12):
            angle = i * math.pi/6 - math.pi/2
            x = largura/2 + 0.7 * largura/2 * math.cos(angle)
            y = altura/2 + 0.7 * altura/2 * math.sin(angle)
            if i ==0:
                canvas.create_text(x, y-10, text=str(i+12), font = ("Helvetica",12))
                
            else:
                canvas.create_text(x, y, text=str(i), font=("Helvetica",12))

#desenho das linhas do minuto
        for i in range(60):
            angle = i * math.pi/30 - math.pi/2
            x1 = largura/2 + 0.8 * largura/2 * math.cos(angle)
            y1 = altura/2 + 0.8 * altura/2 * math.sin(angle)
            x2 = largura/2 + 0.9 * largura/2 * math.cos(angle)
            y2 = altura/2 + 0.9 * altura/2 * math.sin(angle)
            if i % 5 == 0:
                canvas.create_line(x1, y1, x2, y2, fill = "black", width=3)
            else:
                canvas.create_line(x1, y1, x2, y2, fill = "black", width=1)
        
#desenho dos ponteiros
        hour_angle = (hour + minute/60) * math.pi/6 - math.pi/2
        hour_x = largura/2 + 0.5 * largura/2 * math.cos(hour_angle)
        hour_y = altura/2 + 0.5 * altura/2 * math.sin(hour_angle)
        canvas.create_line(largura/2, altura/2, hour_x, hour_y, fill="black", width=6)
        
        minute_angle = (minute + segundo/60) * math.pi/30 - math.pi/2
        minute_x = largura/2 + 0.7 * largura/2 * math.cos(minute_angle)
        minute_y = altura/2 + 0.7 * altura/2 * math.sin(minute_angle)
        canvas.create_line(largura/2, altura/2, minute_x, minute_y, fill="black", width=4)
        
        second_angle = segundo * math.pi/30 - math.pi/2
        second_x = largura/2 + 0.6 * largura/2 * math.cos(second_angle)
        second_y = altura/2 + 0.6 * altura/2 * math.sin(second_angle)
        canvas.create_line(largura/2, altura/2, second_x, second_y, fill="red", width=2)
        
canvas.after(1000, update_relogio)

update_relogio()
root.mainloop()