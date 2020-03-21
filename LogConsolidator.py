import heapq
import os
import shutil
from datetime import datetime, timedelta
import random
from loguru import logger

class LogConsolidator:
    """Builds demo logs and merges them sorted into a new log file"""
    dir_files_in = './in/'
    dir_files_out = './out/'
    files = []

    def __init__(self):
        # Create in and out directories
        if os.path.exists(self.dir_files_in):
            shutil.rmtree(self.dir_files_in)
        os.mkdir(self.dir_files_in)
        if os.path.exists(self.dir_files_out):
            shutil.rmtree(self.dir_files_out)
        os.mkdir(self.dir_files_out)

    def generate_logs(self, number_of_files=5, number_of_lines=700, delta_lines=0, time_delta=300):
        """
        Generate demo log files
        :param number_of_files:
        :param number_of_lines:
        :param delta_lines:
        :param time_delta:
        :return:
        """
        date_start = datetime.now()
        logger.info(f"I'll generate {number_of_files} files with {number_of_lines} lines each")
        for idx_file in range(0, number_of_files):
            filename = f"server{idx_file + 1}"
            with open(f"{self.dir_files_in}{filename}.log", 'a+') as f:
                date = date_start
                for idx_line in range(0, number_of_lines + random.randint(0, delta_lines)):
                    date = date + timedelta(seconds=random.randint(0, time_delta))
                    f.write(f"{date},{filename},this an awesome log {random.randint(0, 8374)}\n")
                logger.info(f"Generated log file: {filename}.log")
        logger.info('All log files generated.')

    def consolidate_sorted_logs(self):
        """
        Merge log files in a final sorted log
        WARNING: This method works for already sorted individual logs
        :return:
        """
        # get log files
        for (dirpath, dirnames, files) in os.walk(self.dir_files_in):
            self.files = files
        logger.info(f"The following files are going to be merged: {self.files}")
        file_heap = []
        for file in self.files:
            f = open(self.dir_files_in + file)
            # get first line of each file
            self.push_to_heap(f, file_heap)

        final_file_name = 'consolidated.log'
        final_file = open(self.dir_files_out + final_file_name, 'a+')

        # while heap is not empty
        while len(file_heap) > 0:
            # pop value from heap
            pop_date, pop_line, pop_file = heapq.heappop(file_heap)
            final_file.write(pop_line)
            # push next line of file to heap
            self.push_to_heap(pop_file, file_heap)
        logger.info(f"Files were merged at {self.dir_files_out}{final_file_name}")

    def push_to_heap(self, file, files_heap):
        line = file.readline()
        if line == '':
            # EOF
            file.close()
        else:
            # parse date from line
            current_date = datetime.fromisoformat(line.split(',')[0])
            # add it to the heap
            heapq.heappush(files_heap, (current_date, line, file))
