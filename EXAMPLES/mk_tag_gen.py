def make_tag_generator(tag_name):  # Define outer function -- this will return the function to use
    def tg(text):  # Define inner function -- this will be the function actually used
        return f"<{tag_name}>{text}<{tag_name}>"  # Inner function returns text wrapped in specified tag
    return tg  # Outer function returns inner function


h1 = make_tag_generator('h1')  # Call outer function to get an instance of the inner function which "knows" the tag and saves the inner function in a variable
div = make_tag_generator('div')

print(h1('Welcome to my web page'))    # Call the created copy of the inner function, which wraps its "baked-in" tag around the text which was passed in
print(div('some excellent content'))

print(div(h1('All about Weasels')))

