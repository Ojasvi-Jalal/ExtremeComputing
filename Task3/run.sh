OUTPUT_DIR=/user/${USER}/data/output
OUTPUT_FILE=output.out

hdfs dfs -rm -r $OUTPUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
    -D mapred.job.name="s1612970's task2" \
    -input /data/small/imdb/title.basics.tsv \
    -input /data/small/imdb/title.ratings.tsv \
    -output $OUTPUT_DIR \
    -mapper mapper.py \
    -file mapper.py \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hdfs dfs -cat ${OUTPUT_DIR}/part-* | sort > $OUTPUT_FILE
cat $OUTPUT_FILE