
file=wrapper-`date +'%Y%m%d'`.log
for i in `ls *.log`
   do
     if [ "$i"x  != "$file"x ]
     then  
       name=`echo $i`
       dname=`echo $i".gz"`
       tar zcvf $dname $name
       echo "rm file $name"
       rm -f $name
      else
          echo "$i ==> do nothing"
          continue
      fi
   done
