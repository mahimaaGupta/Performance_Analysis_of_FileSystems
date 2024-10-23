<H1> Comparative Analysis of Apple APFS and Windows NTFS </H1>

This study shows the comparative analysis of Apple APFS and Windows NTFS. A full factorial experiment has been designed for analysis. It also discusses how ExFAT bridges the gap between NTFS and APFS. 

<H2> Design </H2>
Full Factorial Design.<br>
w.r.f Design Model mentioned in  Art of Computer Systems Performance Analysis Techniques[Raj Jain]
Machines used :
<ul>
<li> Apple Macbook Pro </li>
<li> ROG Strix G17 </li>
<li> Custom PC i9 10th Gen 24GB RTX 3090 </li>
</ul>
In each iteration, three repetitions have been done for all four metrics. Average values for read throughput, write throughput and CPU Utilization have been displayed in the table for simplicity. 
<H3> Metrics </H3>
Following metrics are being considered for the experiment:<br>
<ul>
  <li> Response Time </li>
  <li> Read Throughput </li>
  <li> Write Throughput </li>
  <li> CPU Utilization </li>
</ul>

Read Throughput = Total Bytes Read / Total Read Time

Write Throughput = Total Bytes Written / Total Write Time
<H3> Factors and Levels </H3>
For understanding the behavior of the file systems, various operations must be performed on the files of different sizes. Operations such as reading a file, writing a file, renaming a file, copy/cut/paste a file, changing permissions of a file have been performed. We also need to taken the processor power into consideration. Faster processors would result in faster queries. The processors should be of comparable capacity and power. Therefore, the Two Factors that are being considered are:
<ol>
<li> File Size </li>
<li> Type of Processor </li>
</ol>

Four levels for file size have been selected - 
<ul>
  Small File Sizes 
  <li> 100 MB </li>
  <li> 1GB </li>
  Large File Sizes
  <li> 5GB </li>
  <li> 10GB </li>
</ul>

Three levels for processors have been selected which represent three different types of processors with comparable processing power - 
<ul>
  <li> Apple M1 Pro </li>
  <li> Ryzen 7 6800H </li>
  <li> Intel i9 10th Generation </li>
</ul>
