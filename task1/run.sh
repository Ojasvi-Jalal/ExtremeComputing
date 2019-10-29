OUTPUT_DIR=/user/s1612970/assignment/task1
OUTPUT_FILE=output.out

hdfs dfs -rm -r $OUTPUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
    -D mapred.job.name="s1612970's task1" \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D mapreduce.map.output.key.field.separator="|" \
    -D num.key.fields.for.partition=1 \
    -input /data/large/imdb/title.basics.tsv \
    -output $OUTPUT_DIR \
    -mapper mapper.py \
    -reducer reducer.py \
    -file reducer.py \
    -file mapper.py \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hdfs dfs -cat ${OUTPUT_DIR}/part-*