# Simple Log Consolidator

`LogConsolidator` exports a method to generate multiple sample log files in a CSV format like the following one: `date,servername,logtext`. 

```CSV
2020-03-20 20:06:32.093248,server1,this an awesome log 1134
2020-03-20 20:09:26.093248,server1,this an awesome log 4056
2020-03-20 20:11:27.093248,server1,this an awesome log 8258
```

The objective is to merge all the log files in a final one, but all the records must be sorted by date at the end.

`LogConsolidator` merges all the log files, if individual files are already sorted, you can use `consolidate_sorted_logs()` method to generate a **consolidated.log** file like this.

```CSV
2020-03-20 20:08:41.093248,server2,this an awesome log 6306
2020-03-20 20:09:12.093248,server4,this an awesome log 4293
2020-03-20 20:09:26.093248,server1,this an awesome log 4056
2020-03-20 20:10:25.093248,server3,this an awesome log 7043
```

