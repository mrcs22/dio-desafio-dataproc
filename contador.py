import sys
from pyspark import SparkContext, SparkConf

BUCKET_NAME = "desafio-dataproc-22"

if __name__ == "__main__":
    sc = SparkContext("local", "PySpark Exemplo - Desafio Dataproc")
    words = sc.textFile(
        f"gs://{BUCKET_NAME}/livro.txt").flatMap(lambda line: line.split(" "))
    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(
        lambda a, b: a + b).sortBy(lambda a: a[1], ascending=False)
    wordCounts.saveAsTextFile(f"gs://{BUCKET_NAME}/resultado")
