# move every file in the current directory that has the word hacker in it to a directory called hackerrank
for file in *; do cat "$file" | grep hacker && cp "$file" ../hackerrank/; done

# remove every file in the current directory that has the word hacker in it
for file in *; do cat "$file" | grep hacker && rm "$file"; done