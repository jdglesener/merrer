# merrer
M(app)er (and) R(educ)er

[G4G](https://www.geeksforgeeks.org/hadoop-streaming-using-python-word-count-problem/) with comments removed, utf tag added, and converted to Python3. 

Works over text files with a Python3 installed and execute permissions.

```
mapred streaming \
  -input ??? \
  -output ??? \
  -mapper mapper.py \
  -reducer reducer.py \
  -file mapper.py \
  -file reducer.py
```




I used this command to write create a new file mrps.sh into the scripts folder
```
echo 
"rm scripts/mapper.py
rm scripts/reducer.py
curl https://github.com/jdglesener/merrer/edit/main/mapper.py -o scripts/mapper.py
curl https://raw.githubusercontent.com/jdglesener/merrer/main/reducer.py -o scripts/reducer.py
hdfs dfs -rm -r /user/sandbox/words
mapred streaming \
  -input /user/sandbox/books \
  -output /user/sandbox/words -mapper mapper.py \
  -reducer reducer.py \
  -file scripts/mapper.py \
  -file scripts/reducer.py"
> scripts/mrps.sh
```
Once I run this, to retest my MapReduce functions I only have to run the following line.
```
scripts/mrps.sh
```
