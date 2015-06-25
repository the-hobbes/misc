# go through each directory and check if there are uncommitted git changes in the repo
# () creates subshell so current dir isn't changed

for dir in *;
do
	echo "*** Dir: ${dir} ***"
	(cd $dir && git status --short | cut -c1-2)
done
