#!/bin/bash 
echo "start"

./voicetotext.sh

Q=$(cat stt.txt)
echo "Me:" ,$Q

if [[ $Q =~ .*light.* ]]
then
A="Switching off lights"
./wemo.py
else 
A=$(python queryprocess.py $Q)
echo "Robo",$A

fi

./text2speech.sh $A
