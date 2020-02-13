#!/usr/bin/env bash
# SET PATH OF EXECUTABLES
CCMPRED='PATH/TO/CCMPRED'
FREECONTACT='PATH/TO/FREECONTACT'
PLMDCA='PATH/TO/PLMDCA'
GDCA='PATH/TO/GDCA'
HHBLITS='PATH/TO/HHBLITS'

# SET PATH OF DIRECTORIES
DB='PATH/TO/HHBLITS/DB/'
TMHMM='PATH/TO/TMHMM/ROOT/'

while getopts ":n:c:i:" opt
do
    case $opt in
        n)
        ps=$OPTARG
        ;;
        c)
        pc=$OPTARG
        ;;
        i)
        in=$OPTARG
        ;;
        ?)
        echo "parameter errors, please see https://github.com/2003100127/deephelicon."
        exit 1;;
    esac
done

cat $in$ps$pc'.fasta' | $TMHMM'/bin/decodeanhmm.Linux_x86_64' -f $TMHMM'/lib/TMHMM2.0.options' -modelfile $TMHMM'/lib/TMHMM2.0.model' -noPrintSeq -noPrintScores -noPrintID -noPrintStat > $in$ps$pc'.tmhmm'
$HHBLITS -i $in$ps$pc'.fasta' -maxfilt 100000 -realign_max 100000 -d $DB -all -B 100000 -Z 100000 -n 3 -e 0.001 -oa3m $in$ps$pc'.a3m'
egrep -v "^>" $in$ps$pc'.a3m' | sed 's/[a-zA-Z]//g' > $in$ps$pc'.aln'
egrep -v "^>" $in$ps$pc'.a3m' | sed 's/[a-z]//g' > $in$ps$pc'.faln'
$CCMPRED $in$ps$pc'.aln' $in$ps$pc'.ccmpred'
$FREECONTACT < $in$ps$pc'.aln' > $in$ps$pc'.evfold'
$PLMDCA -o $in$ps$pc'.params' -c $in$ps$pc'.plmc' -n 4 $in$ps$pc'.faln'