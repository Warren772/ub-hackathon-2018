import speech as SR
from tkinter import *

# declaring variables
root = Tk()
var1 = StringVar()
var1.set("We are happy to serve you")
var2 = StringVar()
var2.set("click here to get nearest store")
var3 = StringVar()
var3.set("click to select your store")
var4 = StringVar()
var4.set("Do you want to search product or check availability ?")
var5 = StringVar()
var5.set("place your order ?")



def welcome(event):
    SR.speak("Hello welcome to the wegmans's voice chat")
    SR.speak("Please tell us your zip code")
    zip_code = SR.listen()
    #send this to server
    var2.set("searching in "+ zip_code)
    #zip_button.configure(bg = "red")

    #receive from the server
    nearest_store(["JOHN GLENN", "CHERRY HILL WINE", "EASTWAY", "FAIRPORT", "WOODBRIDGE WINE"])
    # root.update(1000)



def your_choice(event):
    SR.speak("Please speak the serial number of your preferred store")
    selected_store = SR.listen()

   # send to the server
   # var3.set("you selected: " + selected_store)
    var3.set(selected_store)

def nearest_store(stores):

    listbox = Listbox(root)
    listbox.pack()
    listbox.insert(END, "Nearest Store")

    for item in stores:
        listbox.insert(END, item)

def select_item(event):
    SR.speak("Say search to search a product in inventory. Or say check for product availability")
    query = SR.listen()
    SR.speak("Please name the item you are looking for")
    if query == "search":
        item = SR.listen()
        SR.speak("looking "+ item + " in our inventory")
        #data = Search.wegmanSearchProduct(item)

    elif query == "check":
        item = SR.listen()
        SR.speak("checking the availibility of " + item )
        #data = Search.wegmanSearchProduct(item, 1, 1)
     #   data = yes

    #if data != NO:
        SR.speak(item + "is currenlty available")
        #print(data)
    #else:
     #   SR.speak("Sorry " + item + "is not currently available")

    var4.set(item)
    print("var4 : "+var4.get())


def place_order(event):
    SR.speak("the cost of "+ var4.get() + " is 2 dollars") #+ Price.wegmanGetPrices("123",var3.get()))
    SR.speak("Say yes if you want to place your order else say no")
    result = SR.listen()
    SR.speak("Thanks for placing your order please wait while we confirm it")
    # check if its placed
    SR.speak("your order has been placed successfully thanks for shopping at Wegmens")
    var5.set("your order id is 234987")



zip_button = Button(root, textvariable=var2)
zip_button.bind("<Button>", welcome)
root.update()

store_button = Button(root, textvariable=var3)
store_button.bind("<Button>", your_choice)
root.update()

item_button = Button(root, textvariable=var4)
item_button.bind("<Button>", select_item)
root.update()

place_button = Button(root, textvariable=var5)
place_button.bind("<Button>", place_order)
root.update()

location_label = Label(root, textvariable=var1)


location_label.pack()
zip_button.pack()
store_button.pack()
item_button.pack()
place_button.pack()
Button(root, text="Quit", command=root.destroy).pack()



root.title("your bot")
root.geometry("500x500")
root.mainloop()