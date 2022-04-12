import tkinter as tk
class OnScreenPet:
    def __init__(self):
        # create a stand alone window
        self.window = tk.Tk()

        # create a canvas (widget to allow drawing and holding other widgets)
        self.canvas = tk.Canvas(master=self.window, bg='black', width=800, height=600)

        #face and nose
        self.face_outer = self.canvas.create_oval(200, 115, 600, 490, fill='#1E96D5', outline='#1E96D5')
        self.face_inner = self.canvas.create_oval(235, 225, 565, 470, fill='white', outline='black', width = 2)
        self.nose = self.canvas.create_oval(380, 250, 420, 290, fill='red', outline='red')

        # mustache
        self.canvas.create_line(400, 290, 400, 385, fill='black', width=2)
        self.canvas.create_line(300, 290, 360, 310, fill='black', width=2)
        self.canvas.create_line(280, 330, 360, 330, fill='black', width=2)
        self.canvas.create_line(300, 370, 360, 350, fill='black', width=2)
        self.canvas.create_line(440, 310, 500, 290, fill='black', width=2)
        self.canvas.create_line(440, 330, 520, 330, fill='black', width=2)
        self.canvas.create_line(440, 350, 500, 370, fill='black', width=2)

        #eyes
        self.left_eye = self.canvas.create_oval(305, 150, 400, 270, fill='white', outline='black', width=2)
        self.left_eye_pupil = self.canvas.create_oval(340, 220, 365, 245, fill='black', outline='black')
        self.right_eye = self.canvas.create_oval(400, 150, 495, 270, fill='white', outline='black', width=2)
        self.right_eye_pupil = self.canvas.create_oval(435, 220, 460, 245, fill='black', outline='black')

        # mouth
        self.regular_mouth = self.canvas.create_line(300, 388, 400, 500, 500, 388, width = 2, fill='red', smooth=1, state='normal')
        self.smiling_mouth = self.canvas.create_arc(300, 325, 500, 450, start=180, extent=180, fill='red', outline = 'red', state = 'hidden')

        #requesting goemetry manager to size and position the canvas into the window
        self.canvas.pack(fill = tk.BOTH, expand = True)

        #bind some events
        #requesting mainloop to observe user actions on the window, on action call as said method (event method)
        self.window.bind('<Motion>', self.mouse_move)
        self.window.bind('<Leave>', self.mouse_out)
        self.window.bind('<Enter>', self.mouse_over)

        #variables
        self.keep_blinking = True
        self.coords_left_eye_pupil = self.canvas.coords(self.left_eye_pupil)
        self.coords_right_eye_pupil = self.canvas.coords(self.right_eye_pupil)

        #schedule a method call
        self.window.after(1000, self.blink)
        # keep the window alive and let it destory only on explict close
        self.window.mainloop()

    def mouse_move(self, event):
        if event.x >= self.coords_left_eye_pupil[0] and event.x <= self.coords_right_eye_pupil[2] and event.y >= self.coords_left_eye_pupil[1] and event.y <= self.coords_right_eye_pupil[3]:
            # center
            self.canvas.coords(self.left_eye_pupil, self.coords_left_eye_pupil)
            self.canvas.coords(self.right_eye_pupil, self.coords_right_eye_pupil)

        elif event.x >= self.coords_left_eye_pupil[0] and event.x <= self.coords_right_eye_pupil[2]:
            if event.y < self.coords_left_eye_pupil[1]:
                # up
                self.canvas.coords(self.left_eye_pupil, self.coords_left_eye_pupil[0], self.coords_left_eye_pupil[1] - 40, self.coords_left_eye_pupil[2], self.coords_left_eye_pupil[3] - 40)
                self.canvas.coords(self.right_eye_pupil, self.coords_right_eye_pupil[0], self.coords_right_eye_pupil[1] - 40, self.coords_right_eye_pupil[2], self.coords_right_eye_pupil[3] - 40)
            elif event.y > self.coords_left_eye_pupil[3]:
                # down
                self.canvas.coords(self.left_eye_pupil, self.coords_left_eye_pupil[0], self.coords_left_eye_pupil[1] + 20, self.coords_left_eye_pupil[2], self.coords_left_eye_pupil[3] + 20)
                self.canvas.coords(self.right_eye_pupil, self.coords_right_eye_pupil[0], self.coords_right_eye_pupil[1] + 20, self.coords_right_eye_pupil[2], self.coords_right_eye_pupil[3] + 20)
        elif event.y >= self.coords_left_eye_pupil[1] and event.y <= self.coords_right_eye_pupil[3]:
            if event.x < self.coords_left_eye_pupil[0]:
                # left
                self.canvas.coords(self.left_eye_pupil, self.coords_left_eye_pupil[0] - 20, self.coords_left_eye_pupil[1], self.coords_left_eye_pupil[2] - 20, self.coords_left_eye_pupil[3])
                self.canvas.coords(self.right_eye_pupil, self.coords_right_eye_pupil[0] - 20, self.coords_right_eye_pupil[1], self.coords_right_eye_pupil[2] - 20, self.coords_right_eye_pupil[3])
            elif event.x > self.coords_left_eye_pupil[3]:
                # right
                self.canvas.coords(self.left_eye_pupil, self.coords_left_eye_pupil[0] + 20, self.coords_left_eye_pupil[1], self.coords_left_eye_pupil[2] + 20, self.coords_left_eye_pupil[3])
                self.canvas.coords(self.right_eye_pupil, self.coords_right_eye_pupil[0] + 20, self.coords_right_eye_pupil[1], self.coords_right_eye_pupil[2] + 20, self.coords_right_eye_pupil[3])

        elif event.x < self.coords_left_eye_pupil[0]:
            if event.y < self.coords_left_eye_pupil[1]:
                # up left
                self.canvas.coords(self.left_eye_pupil, self.coords_left_eye_pupil[0] - 20,self.coords_left_eye_pupil[1] - 40, self.coords_left_eye_pupil[2] - 20,self.coords_left_eye_pupil[3] - 40)
                self.canvas.coords(self.right_eye_pupil, self.coords_right_eye_pupil[0] - 20, self.coords_right_eye_pupil[1] - 40, self.coords_right_eye_pupil[2] - 20, self.coords_right_eye_pupil[3] - 40)
            elif event.y > self.coords_left_eye_pupil[3]:
                # down left
                self.canvas.coords(self.left_eye_pupil, self.coords_left_eye_pupil[0] - 20, self.coords_left_eye_pupil[1] + 20, self.coords_left_eye_pupil[2] - 20, self.coords_left_eye_pupil[3] + 20)
                self.canvas.coords(self.right_eye_pupil, self.coords_right_eye_pupil[0] - 20, self.coords_right_eye_pupil[1] + 20, self.coords_right_eye_pupil[2] - 20, self.coords_right_eye_pupil[3] + 20)
        elif event.x > self.coords_right_eye_pupil[2]:
            if event.y < self.coords_left_eye_pupil[1]:
                # up right
                self.canvas.coords(self.left_eye_pupil, self.coords_left_eye_pupil[0] + 20, self.coords_left_eye_pupil[1] - 40, self.coords_left_eye_pupil[2] + 20, self.coords_left_eye_pupil[3] - 40)
                self.canvas.coords(self.right_eye_pupil, self.coords_right_eye_pupil[0] + 20, self.coords_right_eye_pupil[1] - 40, self.coords_right_eye_pupil[2] + 20, self.coords_right_eye_pupil[3] - 40)
            elif event.y > self.coords_left_eye_pupil[3]:
                # down right
                self.canvas.coords(self.left_eye_pupil, self.coords_left_eye_pupil[0] + 20, self.coords_left_eye_pupil[1] + 20, self.coords_left_eye_pupil[2] + 20, self.coords_left_eye_pupil[3] + 20)
                self.canvas.coords(self.right_eye_pupil, self.coords_right_eye_pupil[0] + 20, self.coords_right_eye_pupil[1] + 20, self.coords_right_eye_pupil[2] + 20, self.coords_right_eye_pupil[3] + 20)

    def mouse_over(self, event):
        self.keep_blinking = False
        #ensure that the eyes are open
        self.canvas.itemconfig(self.left_eye, fill='white')
        self.canvas.itemconfig(self.right_eye, fill='white')
        self.canvas.itemconfig(self.left_eye_pupil, state='normal')
        self.canvas.itemconfig(self.right_eye_pupil, state='normal')
        #ensure that pet smiles
        self.canvas.itemconfig(self.regular_mouth, state='hidden')
        self.canvas.itemconfig(self.smiling_mouth, state = 'normal')

    def mouse_out(self, event):
        self.keep_blinking = True
        # ensure that pet stops smiling
        self.canvas.itemconfig(self.regular_mouth, state='normal')
        self.canvas.itemconfig(self.smiling_mouth, state='hidden')
        # ensure that pupils are centered
        self.canvas.coords(self.left_eye_pupil, self.coords_left_eye_pupil)
        self.canvas.coords(self.right_eye_pupil, self.coords_right_eye_pupil)

    def blink(self):
        if self.keep_blinking == True:#toggle
            #fetch the eye color
            current_color = self.canvas.itemcget(self.left_eye, 'fill')
            if current_color == 'white':
                new_color = '#1E96D5'
                pupil_state = 'hidden'
            else:
                new_color = 'white'
                pupil_state = 'normal'

            #apply the new color and pupil state
            self.canvas.itemconfig(self.left_eye, fill = new_color)
            self.canvas.itemconfig(self.right_eye, fill=new_color)
            self.canvas.itemconfig(self.left_eye_pupil, state=pupil_state)
            self.canvas.itemconfig(self.right_eye_pupil, state=pupil_state)

        #schedule a method call
        self.window.after(1000, self.blink)


OnScreenPet() #object creation: mem alloc + exec of init
