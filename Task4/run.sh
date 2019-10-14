TEMP_OUTPUT_DIR=/user/${USER}/data/temp
OUTPUT_DIR=/user/${USER}/data/output
OUTPUT_FILE=output.out

hdfs dfs -rm -r $OUTPUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
    -D mapred.job.name="s1612970's task4" \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D mapreduce.map.output.key.field.separator="|" \
    -D num.key.fields.for.partition=2 \
    -D mapreduce.partition.keypartitioner.options=-k1,2 \
    -input /data/small/imdb/name.basics.tsv\
    -input /data/small/imdb/title.crew.tsv \
    -input /data/small/imdb/title.ratings.tsv \
    -output $TEMP_OUTPUT_DIR \
    -mapper mapper1.py \
    -file mapper1.py \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
    -D mapred.job.name="s1612970's task4" \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D mapreduce.map.output.key.field.separator="|" \
    -D num.key.fields.for.partition=2 \
    -D mapreduce.partition.keypartitioner.options=-k1,2 \
    -input $TEMP_OUTPUT_DIR/ \
    -output $OUTPUT_DIR \
    -mapper mapper2.py \
    -file mapper2.py \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hdfs dfs -cat ${OUTPUT_DIR}/part-* | sort > $OUTPUT_FILE
cat $OUTPUT_FILE