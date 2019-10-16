TEMP_OUTPUT_DIR=/user/${USER}/data/temp
OUTPUT_DIR=/user/${USER}/data/output
OUTPUT_FILE=output.out

hdfs dfs -rm -r $OUTPUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
    -D mapred.job.name="s1612970's task3" \
    -D mapreduce.map.output.key.field.separator="|" \
    -D num.key.fields.for.partition=1 \
    -D mapreduce.partition.keycomparator.options="-k1,1n -k2,2" \
    -D mapreduce.partition.keypartitioner.options=-k1,1 \
    -input /data/large/imdb/title.basics.tsv \
    -input /data/large/imdb/title.ratings.tsv \
    -output $TEMP_OUTPUT_DIR \
    -mapper mapper.py \
    -file mapper.py \
    -reducer reducer.py \
    -file reducer.py \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner


hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
    -D mapred.job.name="s1612970's task3" \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D mapred.reduce.tasks=1 \
    -D mapreduce.map.output.key.field.separator="|" \
    -D num.key.fields.for.partition=2 \
    -D mapreduce.partition.keycomparator.options="-k1,1n -k2,2 -k3,3nr -k4,4" \
    -D mapreduce.partition.keypartitioner.options="-k1,1" \
    -input $TEMP_OUTPUT_DIR/ \
    -output $OUTPUT_DIR \
    -mapper mapper2.py \
    -file mapper2.py \
    -reducer reducer2.py \
    -file reducer2.py \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hdfs dfs -cat ${OUTPUT_DIR}/part-* > final_output

