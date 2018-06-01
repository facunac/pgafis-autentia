#!/bin/bash

PSQL='psql afis'

tabla="fingerprints"

for a in ./*.wsq
do
	b="`basename $a`"
	filein="${b/_*.wsq/}"
	dedo="${b/*_/}"
	dedo="${dedo/.wsq/}"
	fileout="$filein.hex"
	echo "fileini:$filein"
	echo "dedo   :$dedo"
	echo "fileout:$fileout"
	xxd -p $a | tr -d "\n" > $fileout
	(echo -ne "now()\t$filein\tCHILE\tWSQ\tAUTENTIA\t$dedo\t\\\\\x"; cat $fileout) | $PSQL -c "COPY $tabla (registrado,id, pais,tecnologia, institucion, dedo, wsq) FROM STDIN"
	$PSQL -c "update fingerprints set mdt = mindt(wsq,true) where id='$filein' and dedo = $dedo;"
done

