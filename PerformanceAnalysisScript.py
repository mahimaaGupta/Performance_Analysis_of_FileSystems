"""
Author : Mahima Gupta (T22055) Date of Start : 01-May-2023
Last Modified Date : 05-May-2023
Script to measure the performance of a file system 
------------------------------------------------------ 
Operations performed :
1. Creating 50 files
2. Writing to a file
3. Appending a file
4. Reading a file
5. Reading from a random index in a file 6. Renaming 50 files
7. Duplicating 5 files
8. Deleting 50 files
Full Factorial Design -
File Size = [100MB, 1GB, 5GB]
Processor = [Silicon Chip, Intel, Ryzen]
Performance Metrics - Response time
    Read Throughoput
    Write Throughput
    CPU Utilization
"""
import os
import shutil
import timeit
import psutil

#--------------------------------
# Function to create directory #
# --------------------------------

def make_directory():
    path = os.path.join(os.getcwd(), 'Experiment') 
    os.makedirs(path)
    #print("Directory created") 
    os.chdir('Experiment')

#--------------------------------------- 
# Function to create multiple files. 
#---------------------------------------
    
def create_file():
    for i in range(0,50):
        filename = "sample" + str(i) + ".txt" 
        with open(filename, 'w') as fr:
            pass
        fr.close()

#---------------------------------- 
# Function to write in a file.
#---------------------------------
        
lines = ['Hello! This is a demo file. We are writing here to get more content. This file will be used as basic file for read and write file operations.', 'This will increase the text file size. We will create file size in such a manner that minimum iterations are required to increase file size.\n']
def write_file(iterations):
    write_start_time = timeit.default_timer() 
    with open("sample0.txt", 'w') as fr:
        for i in range(0, iterations): 
             fr.writelines(lines)
    write_end_time = timeit.default_timer()
    fr.close()
    fileSize = os.stat("sample0.txt").st_size 
    return(write_end_time - write_start_time, fileSize)

#--------------------------------- 
# Function to append a file. 
#---------------------------------

lines = ['These lines are different than the previous one and have been written to further increase the size of the file.', 'These lines will be used only for appending text to a file.\n']
def append_file(iterations):
    write_start_time = timeit.default_timer()
    fileSize = os.stat("sample0.txt").st_size 
    with open("sample0.txt", 'a') as fr:
        for i in range(0, iterations): fr.writelines(lines)
    write_end_time = timeit.default_timer()
    fr.close()
    fileSize = os.stat("sample0.txt").st_size - fileSize 
    return(write_end_time - write_start_time, fileSize)

#--------------------------------- 
# Function to read a file. 
#---------------------------------

def read_file():
    read_start_time = timeit.default_timer() 
    with open('sample0.txt', 'r') as fr:
        body = fr.readlines()
    read_end_time = timeit.default_timer()
    fr.close()
    fileSize = os.stat("sample0.txt").st_size 
    return(read_end_time - read_start_time, fileSize)

#------------------------------------------------- 
# Function to read from a random index in a file. 
#-------------------------------------------------

def random_read():
    read_start_time = timeit.default_timer() 
    with open('sample0.txt', 'r') as fr:
          fr.seek(5000)
    body = fr.readlines()
    read_end_time = timeit.default_timer()
    fr.close()
    fileSize = os.stat("sample0.txt").st_size - 5000 
    return((read_end_time - read_start_time), fileSize)

#--------------------------------- 
# Function to rename 50 files. 
#---------------------------------

def rename_files():
    for i in range(0, 50):
        filename = "sample" + str(i) + ".txt" 
        newFilename = "demo" + str(i) + ".txt" 
        os.rename(filename, newFilename)
    #print("Files renamed successfully")
        
#--------------------------------- 
# Function to duplicate 5 files. 
#---------------------------------
        
def duplicate_files():
    for i in range(1, 6):
        filename = "sample0.txt"
        newFileName = "copied" + str(i) + ".txt" 
        shutil.copy(filename, newFileName)

#--------------------------------- 
# Function to delete 50 files. 
#---------------------------------
        
def delete_files():
    for i in range(0, 50):
        filename = "demo" + str(i) + ".txt"
        os.remove(filename) 
    for i in range(1,6):
        filename = "copied" + str(i) + ".txt"
        os.remove(filename) #print("Files deleted successfully")

def calculate_throughput(total_read_time, total_MB_read, total_MB_written, total_write_time): 
    total_read_time = round(total_read_time, 3)
    total_write_time = round(total_write_time, 3)
    total_MB_read = round(total_MB_read/(10 ** 6), 3)
    total_MB_written = round(total_MB_written/(10 ** 6), 3) 
    read_th = round(total_MB_read/ total_read_time, 3) 
    write_th = round(total_MB_written/ total_write_time, 3) 
    return(read_th, write_th)

#----------------- 
# Main Function 
#-----------------
if __name__ == "__main__":
    total_read_time, total_MB_read, total_MB_written, total_write_time, read_throughput, write_throughput = 0, 0, 0, 0, 0, 0
    #fileSizeFactor = [300000, 3000000, 15000000] 
    fileSizeFactor = [300000, 3000000, 15000000, 30000000] 
    #files = ["100MB", "1GB", "5GB"]
    files = ["100MB", "1GB", "5GB", "10GB"]
    make_directory()
    for x in range(0, 4):
        print(f"For File Size : {files[x]}") 
        for repetitions in range (0, 3):
            start_time = timeit.default_timer() 
            create_file()
            write_time, size = write_file(fileSizeFactor[x]) 
            total_write_time = total_write_time + write_time 
            total_MB_written = total_MB_written + size 
            write_time, size = append_file(fileSizeFactor[x]) 
            total_MB_written = total_MB_written + size
            read_time, size = read_file()
            total_read_time = total_read_time + read_time 
            total_MB_read = total_MB_read + size 
            read_time, size = random_read() 
            total_read_time = total_read_time + read_time 
            total_MB_read = total_MB_read + size
            duplicate_files()
            rename_files()
            delete_files()
            end_time = timeit.default_timer() 
            #cpu = psutil.getloadavg()[1]
            cpu = psutil.cpu_percent()
            execution_time = round((end_time - start_time) * 10 ** 3, 3)
            read_throughput, write_throughput = calculate_throughput(total_read_time, total_MB_read,total_MB_written, total_write_time)
            print(f"[{execution_time} ms], [{read_throughput} MBps], [{write_throughput} MBps], [{cpu}%]")