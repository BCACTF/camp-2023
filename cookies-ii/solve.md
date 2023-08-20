# Cookies Solution

Only the admin is allowed to access the flag. When we try to login, the failed attempt sets our user cookie to "plebian". We can change this to "admin" and then navigate back to `/` so we can access the flag.

This time, the page tells us that we already have the flag. If you look in the cookies, there is a cookie called `flag`. This is encoded in base64 which we can decode using either python or a useful online utility, like [https://www.base64decode.org/](https://www.base64decode.org/).

This gets us our flag.