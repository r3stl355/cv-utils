#!/bin/bash

root_dir=$1
src_file=$2
if [[ "$3" == "gshuf" ]]
then
  echo "Using Gshuf"
  gshuf $root_dir/$src_file > $root_dir/shuffled.lst
else
  echo "Using shuf"
  shuf $root_dir/$src_file > $root_dir/shuffled.lst
fi
ALL_COUNT=$(wc -l < $root_dir/$src_file)
TRAIN_PART=`echo "$ALL_COUNT * 0.9" | bc -l`
TRAIN_COUNT=${TRAIN_PART%.*}
VAL_COUNT=`echo "$ALL_COUNT - $TRAIN_COUNT" | bc -l`
echo "Splitting train(90)/val(10)"

head -n ${TRAIN_COUNT} $root_dir/shuffled.lst > $root_dir/train.lst
tail -n ${VAL_COUNT} $root_dir/shuffled.lst > $root_dir/val.lst

wc -l $root_dir/$src_file
wc -l $root_dir/train.lst
wc -l $root_dir/val.lst