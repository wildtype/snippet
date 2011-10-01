cptmp()
{
	td=$(mktemp -d)
	cp $1 $td
	cd $td
}

