// Databricks notebook source
import spark.implicits._
import org.apache.spark.sql.types._
import org.apache.spark.sql.functions
import java.sql.Timestamp
import org.apache.spark.sql.streaming.Trigger.ProcessingTime
import com.google.cloud.spark.bigquery.BigQueryDataFrameReader      
import org.apache.spark.SparkContext
import org.apache.spark.SparkConf

val bucket = "loggbucket"
spark.conf.set("temporaryGcsBucket", bucket)
spark.conf.set("parentProject", "deft-upgrade-380122")

val kafkaDF = spark.readStream.format("kafka").option("kafka.bootstrap.servers","localhost:9092").option("subscribe","quickstart-events").load

val schema = StructType (List(StructField("IP_address", StringType), StructField("date_time", StringType), StructField("method_URL", StringType), StructField("resp_code", StringType)))

val activationDF = kafkaDF.select(from_json($"value".cast("string"),schema).alias("activation"))

val df = activationDF.select($"activation" ("IP_address").alias("IP_address"), $"activation"("date_time").alias("date_time"), $"activation"("method_URL").alias("method_URL"), $"activation"("resp_code").alias("resp_code"))

val modelCountQuery = df.writeStream.outputMode("append").format("bigquery").option("table", "log_dataset.access_log").option("checkpointLocation", "/path/to/checkpoint/dir/in/hdfs").option("credentialsFile","/home/razyergun/deft-upgrade-380122-4b1870267d5a.json").option("failOnDataLoss",false).option("truncate",false).start().awaitTermination()



