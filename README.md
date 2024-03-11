Experiment designed to draw comparitive study of Mac APFS against Windows NTFS. 

To design the experiment, two factor full factorial design has been implemented. This model has been borrowed from book by Raj Jain[Art of Computer Systems Performance Analysis Techniques for Experimental Design Measurements Simulation And Modeling]. Following metrics are being considered for the experiment:
1. Response Time
2. Read Throughput
3. Write Throughput
4. CPU Utilization

Read Throughput = Total Bytes Read / Total Read Time

Write Throughput = Total Bytes Written / Total Write Time

Two Factors are being considered:
1. File Size
2. Type of Processor

There are 4 levels in file size –
1. 100 MB
2. 1GB
3. 5GB
4. 10GB

There are 3 levels in type of processors –
1. Apple M1 Pro
2. Ryzen 7 6800H
3. Intel i9 10th Generation

Machines used :
• Apple Macbook Pro
• ROG Strix G17
• Custom PC i9 10th Gen 24GB RTX 3090

In each iteration, three repetitions have been done for all four metrics. Average values for read throughput, write throughput and CPU Utilization have been displayed in the table for simplicity. 
