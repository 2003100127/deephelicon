#!/usr/bin/env bash
# SET PATH OF EXECUTABLES
#CCMPRED='PATH/TO/CCMPRED'
#FREECONTACT='PATH/TO/FREECONTACT'
#PLMDCA='PATH/TO/PLMDCA'
#GDCA='PATH/TO/GDCA'
#HHBLITS='PATH/TO/HHBLITS'

CCMPRED='/home/students/j.sun/store/CCMpred/bin/ccmpred'
FREECONTACT='/home/software/BioInformatics/Fedora28/bin/freecontact'
PLMDCA='/home/students/j.sun/store/plmc/bin/plmc'
GDCA='/home/students/j.sun/store/PconsC3/rungdca.py'
HHBLITS='/home/students/j.sun/store/hhblits/bin/hhblits'

# SET PATH OF DIRECTORIES
#DB='PATH/TO/HHBLITS/DB'
#TMHMM='PATH/TO/TMHMM/ROOT_DIRECTORY/'

DB='/home/students/j.sun/store/uniprot20_2016_02/uniprot20_2016_02'
TMHMM='/home/students/j.sun/store/software/tmhmm-2.0c/'

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

$HHBLITS -i $in$ps$pc'.fasta' -maxfilt 100000 -realign_max 100000 -d $DB -all -B 100000 -Z 100000 -n 3 -e 0.001 -oa3m $in$ps$pc'.a3m'
egrep -v "^>" $in$ps$pc'.a3m' | sed 's/[a-z]//g' > $in$ps$pc'.aln'
sed 's/[a-z]//g' $in$ps$pc'.a3m' > $in$ps$pc'.faln'
$CCMPRED $in$ps$pc'.aln' $in$ps$pc'.ccmpred'
$FREECONTACT -f $in$ps$pc'.aln' > $in$ps$pc'.evfold'
$PLMDCA -o $in$ps$pc'.params' -c $in$ps$pc'.plmc' -le 16.0 -lh 0.01 -m 200 $in$ps$pc'.faln'
$GDCA $in$ps$pc'.faln'
cat $in$ps$pc'.fasta' | $TMHMM'/bin/decodeanhmm.Linux_x86_64' -f $TMHMM'/lib/TMHMM2.0.options' -modelfile $TMHMM'/lib/TMHMM2.0.model' -noPrintSeq -noPrintScores -noPrintID -noPrintStat > $in$ps$pc'.tmhmm'
