import easygui
easygui.msgbox ("I'm the address printer! Type in the lines of your address. ")
name = easygui.enterbox ("What is your first and last name?" )
address = easygui.enterbox ("What is your house number and street name? ")
cist = easygui.enterbox ("Name your city and state ")
zcode = easygui.enterbox ("What is your zip code? ")
final = (name + address + cist + zcode)
easygui.msgbox ("Here is your address" + final)


