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
I am starting out verifying the existence of docker
```
docker run hello-world
```

I'll use Hadoop sandbox to set it up so I am cloning this into my environment with the following command.
```
git clone https://github.com/hadoop-sandbox/hadoop-sandbox.git
```
I must then compose the Docker container
```
docker compose up -d
```
And Verify that the cluster is up and running
```
docker ps
```
We need to have python installed on these nodes so I will install python by running these commands
```
docker exec -it hadoop-sandbox-datanode-1 apt-get update
docker exec -it hadoop-sandbox-datanode-1 apt-get -y install python3
docker exec -it hadoop-sandbox-namenode-1 apt-get update
docker exec -it hadoop-sandbox-namenode-1 apt-get -y install python3
docker exec -it hadoop-sandbox-clientnode-1 apt-get update
docker exec -it hadoop-sandbox-clientnode-1 apt-get -y install python3
docker exec -it hadoop-sandbox-nodemanager-1 apt-get update
docker exec -it hadoop-sandbox-nodemanager-1 apt-get -y install python3
```
I now need to enter the container
```
ssh -p 2222 sandbox@localhost
```
Once I am in the container I start by verifying that mapred streaming is supported
```
mapred streaming --help
```
Then I will create the directory where my sample data will live and then bring in my sample data into my container.
```
mkdir books
curl https://raw.githubusercontent.com/cd-public/books/main/pg1342.txt -o books/austen.txt
curl https://raw.githubusercontent.com/cd-public/books/main/pg84.txt -o books/shelley.txt
curl https://raw.githubusercontent.com/cd-public/books/main/pg768.txt -o books/bronte.txt
ls books
```
Now I will begin creating folders in the cluster and moving data from the container into the hadoop cluster
```
hdfs dfs -mkdir /user/sandbox/books
hdfs dfs -copyFromLocal -f books/* /user/sandbox/books
hdfs dfs -ls /user/sandbox/books
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
Before I can run this I need to give the container permission to run the file with the following line
```
chmod 777 scripts/mrps.sh
```
Once I run this, to retest my MapReduce functions I only have to run the following line
```
scripts/mrps.sh
```
