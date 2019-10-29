TEMP_OUTPUT_DIR=/user/${USER}/data/temp
OUTPUT_DIR=/user/s1612970/assignment/task4
OUTPUT_FILE=output.out

hdfs dfs -rm -r $OUTPUT_DIR
hdfs dfs -rm -r $TEMP_OUTPUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
    -D mapred.job.name="s1612970's task4" \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D mapreduce.map.output.key.field.separator="|" \
    -D num.key.fields.for.partition=1 \
    -input /data/large/imdb/name.basics.tsv\
    -input /data/large/imdb/title.crew.tsv \
    -input /data/large/imdb/title.ratings.tsv \
    -output $TEMP_OUTPUT_DIR\
    -mapper mapper1.py \
    -combiner combiner1.py \
    -reducer reducer1.py \
    -file mapper1.py \
    -file combiner1.py \
    -file reducer1.py \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
    -D mapred.job.name="s1612970's task4" \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D mapred.reduce.tasks=1 \
    -D mapreduce.map.output.key.field.separator="|" \
    -D mapreduce.partition.keycomparator.options=-k1,1nr \
    -D mapreduce.partition.keypartitioner.options=-k1,1nr \
    -input $TEMP_OUTPUT_DIR/ \
    -output $OUTPUT_DIR \
    -mapper mapper2.py \
    -combiner combiner2.py \
    -reducer reducer2.py \
    -file mapper2.py \
    -file combiner2.py \
    -file reducer2.py \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hdfs dfs -cat ${OUTPUT_DIR}/part-* | head -20 > $OUTPUT_FILE
cat $OUTPUT_FILE