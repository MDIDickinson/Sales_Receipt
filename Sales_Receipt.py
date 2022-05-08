import Sales_Receipt_Module.py #Importing the module with the class needed
from tkinter import * #Importing tkinter
from tkinter import filedialog #Importing filedialog from tkinter
import os #Importing needed operating system components


sale = Sales_Receipt_Module.SalesReceipt() #Instantiating the class from other module

def Total(): #Function for the total button
    txtExtPrice.configure(text = sale.ExtPrice)
    txtSalesTotal.configure(text = sale.SaleTotal)
    txtSalesTax.configure(text = sale.SalesTax)
    txtGrandTotal.configure(text = sale.FinalSaleAmt)
    for eachline in sale.SalesDetail(): #For loop for writing to the file
        newFile.write(eachline + "\n") #Writing the information to the new file
    return

def AddItem(): #Function for the add item button
    sale.itemName = txtItemName.get()
    sale.itemPrice = float(txtItemPrice.get())
    sale.itemQty = int(txtItemQty.get())
    lblExtPrice.configure(text = sale.AddItem())
    return

def SaveFile(): #Function to save the file and get the information to write
    GUI.filename = filedialog.asksaveasfilename(parent = GUI,
                                                initialdir = os.getcwd(),
                                                title = "Please name your new file",
                                                filetypes = (("text files", "*.txt"), ("All Files", "*.*")))
    fileContents = GUI.filename + ".txt"
    global newFile #Makes the new file global in scope
    newFile = open(fileContents, "w")
    itemName = txtItemName.get() #Gets the data from the text field and assigns it to itemName
    itemQty = txtItemQty.get() #Gets the data from the text field and assigns it to itemQty
    itemPrice = txtItemPrice.get() #Gets the data from the text field and assigns it to itemPrice
    extPrice = txtExtPrice.get() #Gets the data from the text field and assigns it to extPrice
    salesTotal = txtSalesTotal.get() #Gets the data from the text field and assigns it to salesTotal
    salesTax = txtSalesTax.get() #Gets the data from the text field and assigns it to salesTax
    grandTotal = txtGrandTotal.get() #Gets the data from the text field and assigns it to grandTotal
    newFile.write(itemName + ", " + itemQty + ", " + itemPrice + ", " + extPrice + ", " + salesTotal + ", " + salesTax + ", " + grandTotal + "\n") #Writes to the new file

def ClearData(): #Function that erases the inputs and outputs from the GUI window
    txtItemName.delete(0, END) #Clears the item name textbox input
    txtItemQty.delete(0, END) #Clears the item quantity textbox input
    txtItemPrice.delete(0, END) #Clears the item price textbox input
    txtExtPrice.delete(0, END) #Clears the extended price textbox output
    txtSalesTotal.delete(0, END) #Clears the sales total textbox output
    txtSalesTax.delete(0, END) #Clears the sales tax textbox output
    txtGrandTotal.delete(0, END) #Clears the grand total textbox output



def ExitApp():
    newFile.close() #Closes the newly created file
    GUI.destroy() #Destroys the GUI program window
                       

#Creating main GUI Window
GUI = Tk()
GUI.title("Sales Receipt Calculator") #Sets the GUI title
GUI.geometry("800x400") #Sets size of the main GUI window

#Creating textboxes
txtItemName = Entry(GUI, width = 30) #Item name textbox
txtItemName.grid(column = 50, row = 2) #Item name textbox and placement
txtItemQty = Entry(GUI, width = 30) #Item quantity textbox
txtItemQty.grid(column = 50, row = 3) #Item Quantity textbox and placement
txtItemPrice = Entry(GUI, width = 30) #Item price textbox
txtItemPrice.grid(column = 50, row = 4) #Item price textbox and placement
txtExtPrice = Entry(GUI, width = 40, state = 'disabled') #Extended price textbox
txtExtPrice.grid(column = 50, row = 6) #Extended price textbox and placement
txtSalesTotal = Entry(GUI, width = 40, state = 'disabled') #Sales total textbox
txtSalesTotal.grid(column = 50, row = 7) #Sales total textbox and placement
txtSalesTax = Entry(GUI, width = 40, state = 'disabled') #Sales tax textbox
txtSalesTax.grid(column = 50, row = 8) #Sales tax textbox and placement
txtGrandTotal = Entry(GUI, width = 40, state = 'disabled') #Grand total textbox
txtGrandTotal.grid(column = 50, row = 9) #Grand total textbox and placement

#Creating Labels
lblItemName = Label(GUI, text = "Item name: ") #Label for item name
lblItemName.grid(column = 20, row = 2) #Item name label placement
lblItemQty = Label(GUI, text = "Item quantity: ") #Label for item quantity
lblItemQty.grid(column = 20, row = 3) #Item quantity label placement
lblItemPrice = Label(GUI, text = "Item price: ") #Label for item price
lblItemPrice.grid(column = 20, row = 4) #Item price label placement
lblExtPrice = Label(GUI, text = "Extended Price: ") #Label for extended price
lblExtPrice.grid(column = 20, row = 6) #Extended price label placement
lblSalesTotal = Label(GUI, text = "Sales Total: ") #Label for sales total
lblSalesTotal.grid(column = 20, row = 7) #Sales total label placement
lblSalesTax = Label(GUI, text = "Sales Tax: ") #Label for sales tax
lblSalesTax.grid(column = 20, row = 8) #Sales tax label placement
lblGrandTotal = Label(GUI, text = "Grand Total: ") #Label for grand total
lblGrandTotal.grid(column = 20, row = 9) #Grand total label placement

#Creating Buttons
btnAddItem = Button(GUI, text = "Add Item", command = Sales_Receipt_Module.SalesReceipt.AddItem) #Creates the add item button
btnAddItem.grid(column = 60, row = 2) #Add item button placement
btnClearText = Button(GUI, text = "Clear Text", command = ClearData) #Creates the clear text button
btnClearText.grid(column = 60, row = 3) #Clear text button placement
btnSaveToFile = Button(GUI, text = "Save To File", command = SaveFile) #Creates the save to file button
btnSaveToFile.grid(column = 60, row = 4) #Save to file button pllacement
btnTotal = Button(GUI, text = "Total", command = Total) #Creates the total button
btnTotal.grid(column = 60, row = 6) #Total button placement
btnExitProgram = Button(GUI, text = "Exit Program", command = ExitApp) #Creates the exit program button
btnExitProgram.grid(column = 60, row = 8) #Exit program button placement


#Executable Code that starts the program
txtItemName.focus() #Focuses the cursor on the first textbox
GUI.mainloop()