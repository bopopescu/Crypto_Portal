
import tkinter as tk
import urllib.request, json


# The page where our wallets portfolios will be created
class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.options_frame = tk.LabelFrame(self, text="")
        self.options_frame.grid(column="0", columnspan="2", row="0")

        profile = tk.Button(self.options_frame, text="Profile Setteings", command=lambda: controller.show_frame("Profile"))
        profile.grid(column="0", columnspan="2", row="0")

        log_out = tk.Button(self.options_frame, text="Logout", command=lambda: self.controller.show_frame("StartPage"))
        log_out.grid(column="3", row="0")

        json_url = "https://newsapi.org/v2/everything?q=bitcoin&apiKey=628da1c052e745c7a577c25bfc504d49"

        with urllib.request.urlopen(json_url) as url:
            self.data = json.loads(url.read().decode())

        self.article_values = self.data["articles"]

        self.default_font = font = tk.font.Font(family="Times", size=10)
        self.default_bg = "yellow green"

        #creating a container to hold market news
        self.newsFrame = tk.LabelFrame(self,text="Market News", bg=self.default_bg)
        self.newsFrame.grid(column="1",columnspan="2",row="2")
        self.options = []

        self.tkinter_text = tk.Text(self.newsFrame, bg=self.default_bg, font=tk.font.Font(family="Times", size=12) , wrap=tk.WORD )
        #self.tkinter_text.config(state=tk.DISABLED)
        self.tkinter_text.grid(row=2)



        for i in range(0,5):
            test_string = self.article_values[i]["title"]
            self.options.append( test_string )

        self.create_dropdown()


        self.config(bg="yellow green")


    def get_desription(self, title):
         result = None
         for i in range(0,20):
             if title == self.article_values[i]["title"] :
                 result = self.article_values[i]["description"]

         if result==None:
             return " cannnot find description "
         else:
            #print( "returning ->\"", result,"\"" )
            return result


    def create_dropdown(self):
        tkvar = tk.StringVar(self.newsFrame)
        choices = self.options
        tkvar.set(choices[0])
        self.popupMenu = tk.OptionMenu(self.newsFrame,tkvar, *choices)
        self.popupMenu.config(bg="green")
        self.tkinter_text.insert(tk.END, self.get_desription( choices[0] ) )

        def change_dropdown(*args):
            self.tkinter_text.config(state=tk.NORMAL)
            self.tkinter_text.delete(1.0,tk.END)
            self.tkinter_text.insert(tk.END, self.get_desription( tkvar.get() ) )
            self.tkinter_text.config(state=tk.DISABLED)

        tkvar.trace('w', change_dropdown)
        self.popupMenu.grid(row=1, sticky="WE")
