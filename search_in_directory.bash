# run a command against everything in a directory, excluding some files
# and grepping for multiple things.
for file in *
do
	if [ "$file" == "unwanted_file.txt" ]; then
		continue;
	fi
	cat "$file" | grep -Hn "match1\|match2\|match3\|match4";
done