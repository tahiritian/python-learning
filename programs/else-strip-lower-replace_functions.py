# else function
# Strip function (Means input + strip) strip will take out something like ignore Spaces etc.
# .lower()  function for all lower letters
# .replace (' ','')   replace something with something
# palindrom: a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam or nurses run.

ui = input ("Enter your string: ").strip( )
#in separate line:  ui = ui.strip
if ui == ui[::-1]:
	print("Its a palindrom! ")
else:
	print("Its NOT a palindrom! ")