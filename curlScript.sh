# use this to check a website for updates
$ curl http://www.somewebsite.com |
grep -A 3 "something you are looking for " | grep "refine it even more"

