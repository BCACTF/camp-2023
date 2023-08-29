Open DevTools and Inspect Element.

The visible inputs for username and password actually have a name property of `notUsername` and `notPassword` respectively. If you unfold a few `<div>`s, you'll find the actual username and password inputs, which have a name property of `username` and `password` respectively. Type the given username and password into those to receive the flag.