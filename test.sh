
list=(t1 t2 t3 t4)
test()
{
local name age
echo $name
	for i in "${list[@]}"; do
		echo $i; done

}



test
