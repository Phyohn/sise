#!/bin/zsh
cd `dirname $0`

cat /Users/mac2018/Applications/Collection/sise/Raw/*.har > new.txt

grep '\?xml\s' new.txt | sed 's/<modelName>/\n/g' | grep -v '<?x'| sed -E 's/^(.*)<\/modelN.*>([0-9]{1,})<\/dai.*>([-0-9]{1,})<\/totalG.*>([-0-9]{1,})<\/bonus.*>([-0-9]{1,})<\/reg.*>([-0-9]{1,})<\/dedam.*param\=(.*)\=<\/graphU.*/\7,\2,\3,\4,\5,000,\6,\1/g'| sed 's/\-\-/0/g'| tr -d '+' | sort -uk 2n -t ,  | > datapy.txt
daisuu=$(grep -c '' datapy.txt)
echo $daisuu

grep -A 5 -B 80 '\"size\"\:\s[2-5][0-9]\{3\}\,' new.txt |tr -d ' \n'|sed -E 's/name":"param","value":"/\n/g'|grep -v 'name\"\:\"big' | grep 'encoding\"\:\"base64' | sed -E 's/(.*)="}],"headersSize.*image\/png","text":"(.*)","encoding":"base64.*/\1,\2/g' |>py.txt

python ver1.py

newcsv=$(ls -1t /Users/mac2018/Applications/Collection/linkdata/*.csv | head -1)

if [ $daisuu -eq 200 ]; then
	echo "inter"
	mv $newcsv /Users/mac2018/Applications/Collection/linkdata/inter.csv
elif [ $daisuu -eq 259 ]; then
	echo "o-ku"
	mv $newcsv /Users/mac2018/Applications/Collection/linkdata/o-kura.csv
elif [ $daisuu -eq 399 ]; then
	echo "KEIX"
	mv $newcsv /Users/mac2018/Applications/Collection/linkdata/ktakaoka.csv
elif [ $daisuu -eq 280 ]; then
	echo "taiyo"
	mv $newcsv /Users/mac2018/Applications/Collection/linkdata/taiyotakaoka.csv
elif [ $daisuu -eq 328 ]; then
	echo "la"
	mv $newcsv /Users/mac2018/Applications/Collection/linkdata/lapark.csv
elif [ $daisuu -eq 324 ]; then
	echo "kake"
	mv $newcsv /Users/mac2018/Applications/Collection/linkdata/kakeo.csv
elif [ $daisuu -eq 225 ]; then
	echo "hi"
	mv $newcsv /Users/mac2018/Applications/Collection/linkdata/himi.csv
elif [ $daisuu -eq 192 ]; then
	echo "yo"
	mv $newcsv /Users/mac2018/Applications/Collection/linkdata/yosi.csv
elif [ $daisuu -eq 156 ]; then
	echo "tonanor"
	mv $newcsv /Users/mac2018/Applications/Collection/linkdata/tonaminorth.csv
elif [ $daisuu -eq 212 ]; then
	echo "tonasupa"
	mv $newcsv /Users/mac2018/Applications/Collection/linkdata/tonasupa.csv
elif [ $daisuu -eq 282 ]; then
	echo "Q"
	mv $newcsv /Users/mac2018/Applications/Collection/linkdata/quatoro.csv
else
	echo "error!"
fi

echo "fin"